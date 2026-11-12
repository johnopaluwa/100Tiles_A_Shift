"""Engineering drawings: A3 part sheets (3 views + iso, dimensions, hole table) and assembly sheets (ballooned iso + parts list)."""
import math, textwrap, datetime
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle, Circle
import cadquery as cq
from OCP.HLRBRep import HLRBRep_Algo, HLRBRep_HLRToShape
from OCP.HLRAlgo import HLRAlgo_Projector
from OCP.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCP.BRepLib import BRepLib
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE, TopAbs_REVERSED
from OCP.TopoDS import TopoDS
from OCP.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCP.GCPnts import GCPnts_QuasiUniformDeflection
from OCP.GeomAbs import GeomAbs_Line, GeomAbs_Cylinder
from .core import PARTS, ASMS, Asm, exact_bb
from . import render

VIEWS = {'front': ((0, -1, 0), (1, 0, 0)), 'top': ((0, 0, 1), (1, 0, 0)), 'side': ((-1, 0, 0), (0, -1, 0)),
         'iso': ((1, -1, 0.8), (1, 1, 0))}
SCALES = [(10, '10:1'), (5, '5:1'), (2, '2:1')] + [(1 / k, f'1:{k:g}') for k in (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100, 150, 200)]
INK = '#10263b'; HID = '#8a96a3'; DIMC = '#b3261e'
DATE = datetime.date.today().isoformat()
PROJECT = 'SOLAR PLASTIC-SAND ROOF TILE MICROFACTORY'


def _polys(comp, defl):
    out = []
    if comp is None or comp.IsNull():
        return out
    BRepLib.BuildCurves3d_s(comp)
    ex = TopExp_Explorer(comp, TopAbs_EDGE)
    while ex.More():
        c = BRepAdaptor_Curve(TopoDS.Edge_s(ex.Current()))
        try:
            if c.GetType() == GeomAbs_Line:
                p1 = c.Value(c.FirstParameter()); p2 = c.Value(c.LastParameter())
                out.append(np.array([(p1.X(), p1.Y()), (p2.X(), p2.Y())]))
            else:
                d = GCPnts_QuasiUniformDeflection(c, defl)
                if d.IsDone() and d.NbPoints() > 1:
                    out.append(np.array([(d.Value(i).X(), d.Value(i).Y()) for i in range(1, d.NbPoints() + 1)]))
        except Exception:
            pass
        ex.Next()
    return out


def hlr(shape, view, hidden=True):
    n, xd = VIEWS[view]
    h = HLRBRep_Algo()
    h.Add(shape.wrapped)
    h.Projector(HLRAlgo_Projector(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(*n), gp_Dir(*xd))))
    h.Update(); h.Hide()
    s = HLRBRep_HLRToShape(h)
    defl = min(max(shape.BoundingBox().DiagonalLength / 4000.0, 0.02), 1.5)
    vis = _polys(s.VCompound(), defl) + _polys(s.OutLineVCompound(), defl)
    hid = (_polys(s.HCompound(), defl) + _polys(s.OutLineHCompound(), defl)) if hidden else []
    return vis, hid


def ext(polys):
    if not polys:
        return (0, 0, 0, 0)
    a = np.concatenate(polys)
    return a[:, 0].min(), a[:, 0].max(), a[:, 1].min(), a[:, 1].max()


def find_holes(shape):
    """internal cylindrical faces -> {(dia, axis): [positions]}"""
    e = exact_bb(shape)
    seen = {}
    for f in shape.Faces():
        try:
            s = BRepAdaptor_Surface(f.wrapped)
            if s.GetType() != GeomAbs_Cylinder:
                continue
            cyl = s.Cylinder(); ax = cyl.Axis(); d = ax.Direction(); l = ax.Location()
            dv = np.array([d.X(), d.Y(), d.Z()]); k = int(np.argmax(np.abs(dv)))
            v = f.Vertices()[0].Center(); pv = np.array([v.x, v.y, v.z]); lv = np.array([l.X(), l.Y(), l.Z()])
            radial = (pv - lv) - np.dot(pv - lv, dv) * dv
            nrm = f.normalAt(v); nv = np.array([nrm.x, nrm.y, nrm.z])
            if np.dot(nv, radial) >= 0:
                continue                      # outside surface of a shaft / tube, not a hole
            if abs(dv[k]) < 0.999:
                axis = 'oblique'; pos = (round(l.X() - e[0], 1), round(l.Y() - e[1], 1), round(l.Z() - e[2], 1))
            else:
                axis = 'XYZ'[k]
                p = [l.X() - e[0], l.Y() - e[1], l.Z() - e[2]]
                pos = tuple(round(p[j], 1) for j in range(3) if j != k)
            seen.setdefault((round(2 * cyl.Radius(), 2), axis), set()).add(pos)
        except Exception:
            pass
    return {k: sorted(v) for k, v in seen.items()}


def holes_text(holes):
    rows = []
    for (d, axis), pos in sorted(holes.items(), key=lambda kv: (-len(kv[1]), kv[0][0])):
        other = {'X': 'y,z', 'Y': 'x,z', 'Z': 'x,y'}.get(axis, 'x,y,z')
        p = '; '.join('(' + ', '.join(f'{c:g}' for c in q) + ')' for q in pos[:10]) + (' ...' if len(pos) > 10 else '')
        rows.append((f'{len(pos)} x Ø{d:g}', f'axis {axis}', f'{other} = {p}'))
    return rows


# ------------------------------------------------------------------ page primitives
def new_page():
    fig = plt.figure(figsize=(420 / 25.4, 297 / 25.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 420); ax.set_ylim(0, 297); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Rectangle((8, 8), 404, 281, fill=False, lw=1.2, ec=INK))
    return fig, ax


def lines(ax, polys, ox, oy, s, color=INK, lw=0.45, ls='-'):
    if polys:
        ax.add_collection(LineCollection([p * s + (ox, oy) for p in polys], colors=color, linewidths=lw, linestyles=ls, capstyle='round'))


def txt(ax, x, y, s, size=7, color=INK, ha='left', va='baseline', weight='normal', rot=0):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, fontweight=weight, rotation=rot, family='DejaVu Sans')


def dim_h(ax, x1, x2, y, val, off=7):
    yy = y - off
    ax.plot([x1, x1], [y - 1, yy - 1.5], color=DIMC, lw=0.25); ax.plot([x2, x2], [y - 1, yy - 1.5], color=DIMC, lw=0.25)
    ax.annotate('', xy=(x1, yy), xytext=(x2, yy), arrowprops=dict(arrowstyle='<|-|>', color=DIMC, lw=0.35, mutation_scale=5, shrinkA=0, shrinkB=0))
    txt(ax, (x1 + x2) / 2, yy + 0.8, f'{val:g}', 6.5, DIMC, 'center')


def dim_v(ax, y1, y2, x, val, off=7):
    xx = x - off
    ax.plot([x - 1, xx - 1.5], [y1, y1], color=DIMC, lw=0.25); ax.plot([x - 1, xx - 1.5], [y2, y2], color=DIMC, lw=0.25)
    ax.annotate('', xy=(xx, y1), xytext=(xx, y2), arrowprops=dict(arrowstyle='<|-|>', color=DIMC, lw=0.35, mutation_scale=5, shrinkA=0, shrinkB=0))
    txt(ax, xx - 0.8, (y1 + y2) / 2, f'{val:g}', 6.5, DIMC, 'right', 'center', rot=90)


def title_block(ax, pn, name, rows, scale, sheet=''):
    x0, y0, w, h = 228, 10, 182, 48
    ax.add_patch(Rectangle((x0, y0), w, h, fill=False, lw=0.9, ec=INK))
    ax.plot([x0, x0 + w], [y0 + 30, y0 + 30], color=INK, lw=0.5)
    ax.plot([x0 + 118, x0 + 118], [y0, y0 + 30], color=INK, lw=0.5)
    txt(ax, x0 + 3, y0 + 43, PROJECT, 6, HID)
    txt(ax, x0 + 3, y0 + 33.5, name[:58], 10.5, INK, weight='bold')
    txt(ax, x0 + w - 3, y0 + 42, pn, 13, DIMC, 'right', weight='bold')
    yy = y0 + 25
    for k, v in rows[:5]:
        txt(ax, x0 + 3, yy, k, 5.5, HID); txt(ax, x0 + 27, yy, str(v)[:60], 6.5, INK)
        yy -= 5.2
    txt(ax, x0 + 121, y0 + 25, 'SCALE', 5.5, HID); txt(ax, x0 + 140, y0 + 25, scale, 8, INK, weight='bold')
    txt(ax, x0 + 121, y0 + 19.8, 'UNITS', 5.5, HID); txt(ax, x0 + 140, y0 + 19.8, 'mm  |  first-angle projection', 6, INK)
    txt(ax, x0 + 121, y0 + 14.6, 'TOL.', 5.5, HID); txt(ax, x0 + 140, y0 + 14.6, 'ISO 2768-mK unless stated', 6, INK)
    txt(ax, x0 + 121, y0 + 9.4, 'DATE', 5.5, HID); txt(ax, x0 + 140, y0 + 9.4, DATE + '   ' + sheet, 6, INK)
    txt(ax, x0 + 121, y0 + 4.2, 'STATUS', 5.5, HID); txt(ax, x0 + 140, y0 + 4.2, 'CONCEPT - validate before build', 6, DIMC, weight='bold')


def wrap_block(ax, x, y, title, text, width_chars=118, size=6.2, max_lines=9):
    txt(ax, x, y, title, 6, HID, weight='bold')
    yy = y - 4
    n = 0
    for para in text if isinstance(text, list) else [text]:
        for ln in textwrap.wrap(str(para), width_chars) or ['']:
            if n >= max_lines:
                txt(ax, x, yy, '... (continued in the manufacturing guide)', size, HID); return
            txt(ax, x, yy, ln, size); yy -= 3.3; n += 1


def table(ax, x, y, title, rows, colw, size=6.0, max_rows=30, lead=3.4):
    txt(ax, x, y, title, 6, HID, weight='bold')
    yy = y - 4.2
    for i, r in enumerate(rows[:max_rows]):
        xx = x
        for c, wcol in zip(r, colw):
            s = str(c)
            mx = int(wcol / (size * 0.19))
            txt(ax, xx, yy, s if len(s) <= mx else s[:mx - 1] + '…', size)
            xx += wcol
        yy -= lead
    if len(rows) > max_rows:
        txt(ax, x, yy, f'... +{len(rows) - max_rows} more (see BOM / guide)', size, HID); yy -= lead
    return yy


class _BB:
    def __init__(self, shape, exact):
        if exact:
            self.xmin, self.ymin, self.zmin, self.xmax, self.ymax, self.zmax = exact_bb(shape)
        else:
            q = shape.BoundingBox()
            self.xmin, self.ymin, self.zmin, self.xmax, self.ymax, self.zmax = q.xmin, q.ymin, q.zmin, q.xmax, q.ymax, q.zmax
        self.xlen, self.ylen, self.zlen = self.xmax - self.xmin, self.ymax - self.ymin, self.zmax - self.zmin


def ortho_layout(ax, shape, zone=(14, 66, 268, 218), hidden=True, dims=True, exact=True):
    """draw front / top / side views in first-angle arrangement; returns the scale label"""
    bb = _BB(shape, exact)
    dx, dy, dz = max(bb.xlen, 1e-3), max(bb.ylen, 1e-3), max(bb.zlen, 1e-3)
    zx, zy, zw, zh = zone
    gap, dm = 20, 12
    sc, lab = SCALES[-1]
    for s, l in SCALES:
        if s * (dx + dy) + gap + 2 * dm <= zw and s * (dz + dy) + gap + 2 * dm <= zh:
            sc, lab = s, l; break
    fx0 = zx + dm; fy0 = zy + zh - sc * dz - 4          # front view lower-left corner on the page
    V = {k: hlr(shape, k, hidden) for k in ('front', 'top', 'side')}
    # front: page x = (X - xmin), y = (Z - zmin)
    lines(ax, V['front'][1], fx0 - sc * bb.xmin, fy0 - sc * bb.zmin, sc, HID, 0.25, (0, (3, 2)))
    lines(ax, V['front'][0], fx0 - sc * bb.xmin, fy0 - sc * bb.zmin, sc)
    ty0 = fy0 - gap - sc * dy                            # top view below
    lines(ax, V['top'][1], fx0 - sc * bb.xmin, ty0 - sc * bb.ymin, sc, HID, 0.25, (0, (3, 2)))
    lines(ax, V['top'][0], fx0 - sc * bb.xmin, ty0 - sc * bb.ymin, sc)
    sx0 = fx0 + sc * dx + gap                            # left-side view to the right: page x = -(Y) -> ymax at left
    lines(ax, V['side'][1], sx0 + sc * bb.ymax, fy0 - sc * bb.zmin, sc, HID, 0.25, (0, (3, 2)))
    lines(ax, V['side'][0], sx0 + sc * bb.ymax, fy0 - sc * bb.zmin, sc)
    if dims:
        rd = (lambda v: round(v, 2)) if exact else (lambda v: round(v))
        dim_h(ax, fx0, fx0 + sc * dx, fy0, rd(dx))
        dim_v(ax, fy0, fy0 + sc * dz, fx0, rd(dz))
        dim_v(ax, ty0, ty0 + sc * dy, fx0, rd(dy))
        dim_h(ax, sx0, sx0 + sc * dy, fy0, rd(dy))
    txt(ax, fx0, fy0 + sc * dz + 1.5, 'FRONT', 5, HID); txt(ax, fx0, ty0 + sc * dy + 1.5, 'TOP', 5, HID); txt(ax, sx0, fy0 + sc * dz + 1.5, 'LEFT SIDE', 5, HID)
    return lab


def iso_lines(ax, shape, box):
    x, y, w, h = box
    vis, _ = hlr(shape, 'iso', False)
    x0, x1, y0, y1 = ext(vis)
    s = min((w - 6) / max(x1 - x0, 1e-6), (h - 6) / max(y1 - y0, 1e-6))
    lines(ax, vis, x + w / 2 - s * (x0 + x1) / 2, y + h / 2 - s * (y0 + y1) / 2, s, INK, 0.35)
    ax.add_patch(Rectangle((x, y), w, h, fill=False, lw=0.3, ec=HID))
    txt(ax, x + 2, y + h - 4, 'ISOMETRIC (not to scale)', 5, HID)


PROC_NAME = {'SAW': 'Saw to length', 'LASER': 'Laser / plasma profile cut', 'ROLL': 'Cut blank, roll, weld seam', 'BEND': 'Cut blank, fold',
             'TURN': 'Lathe turned', 'MILL': 'Milled', 'CNC3D': '3-axis CNC surface machined', 'CAST': 'Sand cast + CNC finish', 'WELD': 'Plate fabrication',
             'FLIGHT': 'Sectional flight, cut + formed', 'MESH': 'Cut to size', 'BOARD': 'Cut to size (saw/router)', 'BUY': 'Purchased item',
             'MOULD': 'Compression moulded', 'MOD': 'Purchased + modified on site'}


def part_sheet(pn, qty=None):
    p = PARTS[pn]
    sh = p.shape()
    fig, ax = new_page()
    try:
        lab = ortho_layout(ax, sh)
    except Exception as e:
        lab = '-'; txt(ax, 20, 150, 'view generation failed: ' + str(e)[:80], 7, DIMC)
    try:
        iso_lines(ax, sh, (292, 208, 116, 77))
    except Exception:
        pass
    bb = p.bbox(); kg = p.kg()
    drows = [(k, v) for k, v in p.dims.items()]
    drows.append(('Envelope X x Y x Z', f'{bb[0]:.1f} x {bb[1]:.1f} x {bb[2]:.1f}'.replace('.0 ', ' ').replace('.0', '') if False else f'{bb[0]:.1f} x {bb[1]:.1f} x {bb[2]:.1f}'))
    y = table(ax, 292, 202, 'KEY DIMENSIONS (mm)', drows, (46, 72), max_rows=14)
    holes = find_holes(sh) if p.kind != 'buy' else {}
    hrows = holes_text(holes)
    p.holes_txt = [' | '.join(r) for r in hrows]
    if hrows:
        y = table(ax, 292, y - 3, 'HOLES / BORES (positions from the min-X, min-Y, min-Z corner)', [(a, b) for a, b, c in hrows], (26, 20), max_rows=8)
        yy = y
        for a, b, c in hrows[:6]:
            for ln in textwrap.wrap(f'{a}: {c}', 82)[:3]:
                txt(ax, 292, yy, ln, 5.2, INK); yy -= 2.9
        y = yy
    files = f'STEP: models/step/parts/{pn}.step     STL: models/stl/{pn}.stl' + (f'     DXF (flat, 1:1): models/dxf/{pn}.dxf' if getattr(p, 'has_dxf', False) else '')
    txt(ax, 14, 61, files, 5.5, HID)
    note = []
    if p.kind == 'buy':
        note.append('PURCHASE SPECIFICATION: ' + p.spec)
    if p.notes:
        note.append(p.notes)
    route = getattr(p, 'route_final', None)
    if route:
        note.append('HOW TO MAKE: ' + '  '.join(f'({i + 1}) {s}' for i, s in enumerate(route)))
    wrap_block(ax, 14, 54, 'NOTES', note, 150, 5.6, 13)
    rows = [('MATERIAL', p.mat), ('STOCK', p.stock), ('PROCESS', PROC_NAME.get(p.proc, p.proc)),
            ('MASS', '-' if kg is None else f'{kg:.2f} kg'), ('QTY (PLANT)', qty if qty is not None else '-')]
    title_block(ax, pn, p.name, rows, lab)
    return fig


def _balloons(ax, pts, labels, box, r=2.7):
    """pts: page coords of targets; place balloons with simple repulsion inside box"""
    P0 = np.array(pts, dtype=float)
    Q = P0 + np.array([6.0, 6.0])
    x, y, w, h = box
    for it in range(200):
        moved = False
        for i in range(len(Q)):
            for j in range(i + 1, len(Q)):
                d = Q[i] - Q[j]; dist = np.hypot(*d)
                if dist < 2 * r + 1.2:
                    if dist < 1e-6:
                        d = np.array([1.0, 0.3 * (i - j)]); dist = np.hypot(*d)
                    push = (2 * r + 1.2 - dist) / 2 * d / dist
                    Q[i] += push; Q[j] -= push; moved = True
        Q[:, 0] = np.clip(Q[:, 0], x + r + 1, x + w - r - 1); Q[:, 1] = np.clip(Q[:, 1], y + r + 1, y + h - r - 1)
        if not moved:
            break
    for p0, q, lab in zip(P0, Q, labels):
        ax.plot([p0[0], q[0]], [p0[1], q[1]], color=DIMC, lw=0.3, zorder=5)
        ax.add_patch(Circle(p0, 0.5, color=DIMC, zorder=6))
        ax.add_patch(Circle(q, r, fc='white', ec=DIMC, lw=0.5, zorder=7))
        txt(ax, q[0], q[1], str(lab), 5.8, DIMC, 'center', 'center', 'bold'); ax.texts[-1].set_zorder(8)


def child_point(asm, ref):
    """world-space representative point of the first instance of a direct child"""
    for r, loc in asm.items:
        if (r is ref) or (r == ref):
            if isinstance(r, Asm):
                pts = []
                for pn, l2, _ in r.flat(loc):
                    c = PARTS[pn].shape().moved(l2).BoundingBox()
                    pts.append(((c.xmin + c.xmax) / 2, (c.ymin + c.ymax) / 2, (c.zmin + c.zmax) / 2))
                return np.mean(pts, axis=0)
            c = PARTS[r].shape().moved(loc).BoundingBox()
            return np.array(((c.xmin + c.xmax) / 2, (c.ymin + c.ymax) / 2, (c.zmin + c.zmax) / 2))


def asm_sheets(asm, view=(1, 1.7, 1.0), png_path=None, hlr_ok=True):
    """-> list of figures: ballooned iso + parts list, then orthographic GA"""
    figs = []
    skip = [pn for pn, p in PARTS.items() if p.alpha < 1]
    tri, col, ids = render.scene_tris(asm, skip)
    im, proj = render.render(tri, col, ids, view, (1500, 1040), bg=(255, 255, 255), ss=2, return_proj=True)
    if png_path:
        im.save(png_path)
    children = asm.direct()
    items = []
    for k, (ref, qty) in enumerate(children):
        if isinstance(ref, Asm):
            items.append((k + 1, ref.code, ref.name + (' (weldment)' if ref.kind == 'weldment' else ' (sub-assembly)'), qty, ref))
        else:
            items.append((k + 1, ref, PARTS[ref].name, qty, ref))
    fig, ax = new_page()
    bx = (12, 62, 260, 180.3)
    ax.imshow(np.asarray(im), extent=(bx[0], bx[0] + bx[2], bx[1], bx[1] + bx[3]), zorder=1, interpolation='bilinear')
    ax.set_xlim(0, 420); ax.set_ylim(0, 297)
    pts = []
    for it in items:
        w = child_point(asm, it[4])
        px = proj(np.array([w]))[0]
        pts.append((bx[0] + px[0] / 1500 * bx[2], bx[1] + bx[3] - px[1] / 1040 * bx[3]))
    _balloons(ax, pts, [it[0] for it in items], bx)
    txt(ax, 14, 280, f'{asm.code}   {asm.name}', 12, INK, weight='bold')
    wrap_block(ax, 14, 274, '', asm.desc or '', 150, 6.5, 4)
    rows = [(a, b, c, d) for a, b, c, d, _ in items]
    per = 52
    table(ax, 278, 283, 'PARTS LIST   item | number | description | qty', rows[:per], (8, 21, 96, 8), 5.6, per, 4.05)
    if asm.kind == 'weldment':
        wrap_block(ax, 14, 54, 'WELDING / ASSEMBLY', asm.weld, 150, 5.8, 12)
    else:
        wrap_block(ax, 14, 54, 'NOTE', 'Item numbers refer to the parts list. Weldments and sub-assemblies have their own sheets. Fasteners and bought-out '
                   'consumables are in the hardware list of the manufacturing guide. Full geometry: models/step/assemblies/' + asm.code + '.step', 150, 5.8, 6)
    c = asm.counts()
    kg = sum((PARTS[pn].kg() or 0) * n for pn, n in c.items())
    title_block(ax, asm.code, asm.name, [('TYPE', 'Weldment' if asm.kind == 'weldment' else 'General arrangement'), ('PARTS', f'{len(c)} unique / {sum(c.values())} pieces'),
                                         ('MASS', f'approx. {kg:.0f} kg'), ('STEP', f'models/step/assemblies/{asm.code}.step'), ('', '')], 'NTS', 'sheet 1')
    figs.append(fig)
    for k0 in range(per, len(rows), 110):
        fig, ax = new_page()
        table(ax, 14, 283, 'PARTS LIST (continued)', rows[k0:k0 + 55], (8, 21, 96, 8), 5.6, 55, 4.05)
        table(ax, 160, 283, '', rows[k0 + 55:k0 + 110], (8, 21, 96, 8), 5.6, 55, 4.05)
        title_block(ax, asm.code, asm.name, [('TYPE', 'Parts list')], '-', 'continued')
        figs.append(fig)
    if hlr_ok:
        fig, ax = new_page()
        comp = cq.Compound.makeCompound([PARTS[pn].shape().moved(loc) for pn, loc, _ in asm.flat() if PARTS[pn].alpha == 1])
        try:
            lab = ortho_layout(ax, comp, zone=(14, 62, 392, 222), hidden=False, exact=False)
        except Exception as e:
            lab = '-'; txt(ax, 20, 150, 'view generation failed: ' + str(e)[:80], 7, DIMC)
        title_block(ax, asm.code, asm.name, [('TYPE', 'Orthographic views, overall dimensions'), ('', ''), ('', ''), ('', ''), ('', '')], lab, 'sheet 2')
        figs.append(fig)
    return figs
