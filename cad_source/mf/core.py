"""Core framework: part registry, assemblies, stock-shape helpers.

Conventions (all dimensions in millimetres):
  * linear members (hollow sections, tubes, bars, angles) run along local +X from x=0 to x=L
  * plates lie flat in local XY (centred on the origin), thickness from z=0 up to z=t
  * Asm.add(ref, pos, rot): rot=(rx, ry, rz) in degrees, applied X then Y then Z, then translated
      member along +Y : rot=(0, 0, 90)      member vertical (+Z): rot=(0, -90, 0)
"""
import math
from dataclasses import dataclass
import cadquery as cq

V = cq.Vector

# ---------------------------------------------------------------- colours
GREEN = (0.12, 0.54, 0.36); ORANGE = (0.93, 0.49, 0.13); BLUE = (0.13, 0.30, 0.55)
STEEL = (0.62, 0.65, 0.68); DARK = (0.27, 0.29, 0.32); WHITE = (0.93, 0.93, 0.90)
YELLOW = (0.95, 0.75, 0.10); RED = (0.80, 0.20, 0.15); ALU = (0.80, 0.82, 0.84)
TILE = (0.72, 0.25, 0.16); CREAM = (0.90, 0.84, 0.62); BLACK = (0.12, 0.12, 0.13)
NAVY = (0.10, 0.14, 0.24); GLASS = (0.62, 0.80, 0.88); PV = (0.10, 0.16, 0.42)
WOOD = (0.72, 0.55, 0.33); BRONZE = (0.72, 0.50, 0.20); CTGREEN = (0.10, 0.42, 0.30)
LGREY = (0.80, 0.81, 0.80); SKY = (0.20, 0.45, 0.78)

# ---------------------------------------------------------------- materials (density g/cm3)
DENS = {
    'S235JR': 7.85, 'S355J2': 7.85, 'C45': 7.85, 'C45 chromed': 7.85, '42CrMo4': 7.85,
    'Hardox 450': 7.85, 'AISI 304': 7.9, 'DC01 galv.': 7.85, 'P20 tool steel': 7.85,
    'Al A356-T6': 2.68, 'Al 5083': 2.66, 'Bronze CuSn12': 8.7, 'HDPE': 0.95,
    'Polycarbonate': 1.2, 'Plastic-sand composite': 1.72, 'Plywood': 0.65, 'Timber': 0.5,
    'Woven wire 304': 7.9, 'EN-GJL-250': 7.2,
}


def L(x=0, y=0, z=0, rx=0, ry=0, rz=0):
    loc = cq.Location(V(x, y, z))
    if rz: loc = loc * cq.Location(V(0, 0, 0), V(0, 0, 1), rz)
    if ry: loc = loc * cq.Location(V(0, 0, 0), V(0, 1, 0), ry)
    if rx: loc = loc * cq.Location(V(0, 0, 0), V(1, 0, 0), rx)
    return loc


def exact_bb(shape):
    """tight bounding box (xmin, ymin, zmin, xmax, ymax, zmax) without OCC's tolerance padding"""
    from OCP.Bnd import Bnd_Box
    from OCP.BRepBndLib import BRepBndLib
    try:
        b = Bnd_Box(); b.SetGap(0.0)
        BRepBndLib.AddOptimal_s(shape.wrapped, b, False, False)
        return tuple(b.Get())
    except Exception:
        q = shape.BoundingBox()
        return (q.xmin, q.ymin, q.zmin, q.xmax, q.ymax, q.zmax)


# ---------------------------------------------------------------- registry
@dataclass
class Part:
    pn: str
    name: str
    wp: object
    mat: str
    stock: str
    proc: str
    color: tuple
    kind: str = 'fab'          # 'fab' fabricated in-house | 'buy' purchased
    dims: dict = None          # key dimensions shown on the drawing / in the guide
    notes: str = ''
    route: list = None         # custom manufacturing steps (overrides the process template)
    flat: object = None        # flat blank (Workplane) for rolled / formed sheet parts -> DXF
    mass: float = None         # override mass in kg (purchased items)
    spec: str = ''             # purchase specification
    alpha: float = 1.0

    def shape(self):
        vals = self.wp.vals() if hasattr(self.wp, 'vals') else [self.wp]
        vals = [v for v in vals if isinstance(v, cq.Shape)]
        return vals[0] if len(vals) == 1 else cq.Compound.makeCompound(vals)

    def bbox(self):
        b = exact_bb(self.shape())
        return (b[3] - b[0], b[4] - b[1], b[5] - b[2])

    def kg(self):
        if self.mass is not None:
            return self.mass
        d = DENS.get(self.mat)
        if d is None:
            return None
        return self.shape().Volume() * d / 1e6


PARTS = {}
ASMS = {}
HARDWARE = {}   # asm code -> list of (description, qty)


def P(pn, name, wp, mat, stock, proc, color, kind='fab', dims=None, notes='', route=None,
      flat=None, mass=None, spec='', alpha=1.0):
    if pn in PARTS:
        raise ValueError('duplicate part number ' + pn)
    PARTS[pn] = Part(pn, name, wp, mat, stock, proc, color, kind, dims or {}, notes, route,
                     flat, mass, spec, alpha)
    return pn


def buy(pn, name, wp, spec, color=DARK, mass=None, notes=''):
    return P(pn, name, wp, 'Purchased', spec, 'BUY', color, kind='buy', mass=mass, spec=spec,
             notes=notes)


class Asm:
    def __init__(self, code, name, kind='machine', desc='', weld=''):
        if code in ASMS:
            raise ValueError('duplicate assembly ' + code)
        self.code = code; self.name = name; self.kind = kind; self.desc = desc
        self.weld = weld
        self.items = []
        ASMS[code] = self

    def add(self, ref, pos=(0, 0, 0), rot=(0, 0, 0)):
        self.items.append((ref, L(*pos, *rot)))
        return self

    def hw(self, desc, qty):
        HARDWARE.setdefault(self.code, []).append((desc, qty))
        return self

    def flat(self, base=None, path=()):
        base = base or cq.Location()
        for ref, loc in self.items:
            if isinstance(ref, Asm):
                yield from ref.flat(base * loc, path + (ref.code,))
            else:
                yield ref, base * loc, path

    def counts(self):
        c = {}
        for pn, _, _ in self.flat():
            c[pn] = c.get(pn, 0) + 1
        return c

    def direct(self):
        """direct children with quantities: [(ref, qty)] preserving first-seen order"""
        order, c = [], {}
        for ref, _ in self.items:
            k = ref.code if isinstance(ref, Asm) else ref
            if k not in c:
                order.append(ref)
            c[k] = c.get(k, 0) + 1
        return [(r, c[r.code if isinstance(r, Asm) else r]) for r in order]

    def compound(self):
        shapes = [PARTS[pn].shape().moved(loc) for pn, loc, _ in self.flat()]
        return cq.Compound.makeCompound(shapes)


# ---------------------------------------------------------------- raw shapes
def box(lx, ly, lz, c=(True, True, False)):
    return cq.Workplane('XY').box(lx, ly, lz, centered=c)


def shs(Lg, a, b=None, t=3.0):
    b = b or a
    return cq.Workplane('YZ').rect(a, b).rect(a - 2 * t, b - 2 * t).extrude(Lg)


def tube(od, t, Lg):
    return cq.Workplane('YZ').circle(od / 2).circle(od / 2 - t).extrude(Lg)


def rod(d, Lg):
    return cq.Workplane('YZ').circle(d / 2).extrude(Lg)


def flatbar(Lg, w, t):
    """flat bar along X, width w in Y, thickness t in Z (centred)"""
    return cq.Workplane('YZ').rect(w, t).extrude(Lg)


def angle(Lg, a, b, t):
    """angle section along X; heel at origin, leg a along +Y, leg b along +Z"""
    return cq.Workplane('YZ').polyline([(0, 0), (a, 0), (a, t), (t, t), (t, b), (0, b)]).close().extrude(Lg)


def channel(Lg, h, b, t):
    """U channel along X; web on the XZ... web vertical at y=0, flanges toward +Y, height h centred on Z"""
    pts = [(0, -h / 2), (b, -h / 2), (b, -h / 2 + t), (t, -h / 2 + t), (t, h / 2 - t), (b, h / 2 - t), (b, h / 2), (0, h / 2)]
    return cq.Workplane('YZ').polyline(pts).close().extrude(Lg)


def plate(lx, ly, t, holes=(), rects=(), slots=()):
    """flat plate centred in XY, z 0..t. holes [(x,y,d)], rects [(x,y,w,h)] cut-outs,
    slots [(x,y,length,width,angle)]"""
    w = cq.Workplane('XY').rect(lx, ly).extrude(t)
    by_d = {}
    for x, y, d in holes:
        by_d.setdefault(d, []).append((x, y))
    for d, pts in by_d.items():
        w = w.cut(cq.Workplane('XY').pushPoints(pts).circle(d / 2).extrude(t))
    for x, y, rw, rh in rects:
        w = w.cut(cq.Workplane('XY').center(x, y).rect(rw, rh).extrude(t))
    for x, y, sl, sw, ang in slots:
        w = w.cut(cq.Workplane('XY').center(x, y).transformed(rotate=(0, 0, ang)).slot2D(sl, sw).extrude(t))
    return w


def poly_plate(pts, t, holes=()):
    w = cq.Workplane('XY').polyline(pts).close().extrude(t)
    by_d = {}
    for x, y, d in holes:
        by_d.setdefault(d, []).append((x, y))
    for d, p in by_d.items():
        w = w.cut(cq.Workplane('XY').pushPoints(p).circle(d / 2).extrude(t))
    return w


def disc(od, t, bore=0, holes=()):
    w = cq.Workplane('XY').circle(od / 2)
    if bore:
        w = w.circle(bore / 2)
    w = w.extrude(t)
    by_d = {}
    for x, y, d in holes:
        by_d.setdefault(d, []).append((x, y))
    for d, p in by_d.items():
        w = w.cut(cq.Workplane('XY').pushPoints(p).circle(d / 2).extrude(t))
    return w


def pcd(n, dia, d, start=0):
    """n holes of diameter d on pitch circle dia -> list of (x,y,d)"""
    return [(dia / 2 * math.cos(math.radians(start + i * 360 / n)),
             dia / 2 * math.sin(math.radians(start + i * 360 / n)), d) for i in range(n)]


def rect_pattern(nx, ny, px, py, d):
    return [((i - (nx - 1) / 2) * px, (j - (ny - 1) / 2) * py, d) for i in range(nx) for j in range(ny)]


def stepped(sections, keys=()):
    """turned shaft along X from stepped sections [(dia, length), ...].
    keys: [(x_start, length, width, depth, dia_at_key)] keyways cut on +Z"""
    w = None; x = 0
    for d, lg in sections:
        s = cq.Workplane('YZ').workplane(offset=x).circle(d / 2).extrude(lg)
        w = s if w is None else w.union(s)
        x += lg
    for xs, kl, kw, kd, dk in keys:
        w = w.cut(cq.Workplane('XY').box(kl, kw, kd + 5, centered=(False, True, False)).translate((xs, 0, dk / 2 - kd)))
    return w


def flight(od, id_, pitch, t, hand=1):
    """one pitch of sectional screw flighting, axis along +X starting at x=0"""
    rm = (od + id_) / 4
    helix = cq.Wire.makeHelix(pitch, pitch, rm, lefthand=(hand < 0))
    f = cq.Workplane('XZ').center(rm, 0).rect((od - id_) / 2, t).sweep(cq.Workplane('XY').add(helix), isFrenet=True)
    return f.rotate((0, 0, 0), (0, 1, 0), 90)


def flight_blank(od, id_, pitch, t):
    """developed flat blank (annular sector) for one pitch of flighting"""
    w = (od - id_) / 2
    lo = math.hypot(math.pi * od, pitch); li = math.hypot(math.pi * id_, pitch)
    r = w * li / (lo - li); R = r + w
    ang = 360 * lo / (2 * math.pi * R)           # included angle of the blank
    a0 = math.radians((360 - ang) / 2); a1 = math.radians(360 - (360 - ang) / 2)
    n = 48
    outer = [(R * math.cos(a0 + (a1 - a0) * i / n), R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
    inner = [(r * math.cos(a0 + (a1 - a0) * i / n), r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
    pts = outer + inner[::-1]
    return cq.Workplane('XY').polyline(pts).close().extrude(t), dict(R=round(R, 1), r=round(r, 1), angle=round(ang, 1))


# ---------------------------------------------------------------- registered stock parts
def p_shs(pn, name, Lg, a, b=None, t=3.0, color=GREEN, mat='S235JR', notes='', holes=None):
    b = b or a
    w = shs(Lg, a, b, t)
    if holes:      # [(x, d, axis)] axis 'y' or 'z' through both walls
        for x, d, ax in holes:
            if ax == 'z':
                w = w.cut(cq.Workplane('XY').center(x, 0).circle(d / 2).extrude(b).translate((0, 0, -b / 2)))
            else:
                w = w.cut(cq.Workplane('XZ').center(x, 0).circle(d / 2).extrude(a).translate((0, a / 2, 0)))
    nm = 'SHS' if a == b else 'RHS'
    return P(pn, name, w, mat, f'{nm} {a:g}x{b:g}x{t:g}', 'SAW', color,
             dims={'Cut length': Lg, 'Section': f'{a:g} x {b:g} x {t:g} wall'}, notes=notes)


def p_tube(pn, name, od, t, Lg, color=STEEL, mat='S235JR', notes='', proc='SAW'):
    return P(pn, name, tube(od, t, Lg), mat, f'Tube OD{od:g} x {t:g}', proc, color,
             dims={'Cut length': Lg, 'OD': od, 'Wall': t}, notes=notes)


def p_rod(pn, name, d, Lg, color=STEEL, mat='S235JR', notes='', proc='SAW'):
    return P(pn, name, rod(d, Lg), mat, f'Round bar dia {d:g}', proc, color,
             dims={'Cut length': Lg, 'Diameter': d}, notes=notes)


def p_flat(pn, name, Lg, w, t, color=GREEN, mat='S235JR', notes=''):
    return P(pn, name, flatbar(Lg, w, t), mat, f'Flat bar {w:g}x{t:g}', 'SAW', color,
             dims={'Cut length': Lg, 'Section': f'{w:g} x {t:g}'}, notes=notes)


def p_angle(pn, name, Lg, a, b, t, color=GREEN, mat='S235JR', notes=''):
    return P(pn, name, angle(Lg, a, b, t), mat, f'Angle {a:g}x{b:g}x{t:g}', 'SAW', color,
             dims={'Cut length': Lg, 'Section': f'L {a:g} x {b:g} x {t:g}'}, notes=notes)


def p_plate(pn, name, lx, ly, t, holes=(), rects=(), slots=(), color=STEEL, mat='S235JR', notes='',
            proc='LASER', dims=None):
    d = {'Length': lx, 'Width': ly, 'Thickness': t}
    d.update(dims or {})
    return P(pn, name, plate(lx, ly, t, holes, rects, slots), mat, f'Plate {t:g} mm', proc, color,
             dims=d, notes=notes)


def p_disc(pn, name, od, t, bore=0, holes=(), color=STEEL, mat='S235JR', notes='', proc='LASER'):
    d = {'OD': od, 'Thickness': t}
    if bore: d['Bore'] = bore
    return P(pn, name, disc(od, t, bore, holes), mat, f'Plate {t:g} mm', proc, color, dims=d, notes=notes)


def p_shell(pn, name, od, t, Lg, color=STEEL, mat='S235JR', notes='', cut=None):
    """rolled & seam welded cylinder shell along X; registers flat blank for the DXF"""
    w = tube(od, t, Lg)
    if cut is not None:
        w = w.cut(cut)
    dev = math.pi * (od - t)
    return P(pn, name, w, mat, f'Sheet {t:g} mm', 'ROLL', color,
             dims={'OD': od, 'Wall': t, 'Length': Lg, 'Developed blank': f'{dev:.0f} x {Lg:g}'},
             notes=notes, flat=plate(dev, Lg, t))


# ---------------------------------------------------------------- purchased envelopes
def gearmotor_shape(kw=0.37, hollow=25):
    """shaft-mounted gearmotor envelope. Hollow output axis along X through origin,
    gearbox centred on origin, motor pointing +Z."""
    s = {0.18: (110, 90, 110, 200), 0.37: (120, 100, 125, 220), 0.75: (150, 120, 145, 260),
         2.2: (200, 160, 180, 330), 4.0: (240, 190, 220, 380)}[kw]
    g, gw, md, ml = s
    w = cq.Workplane('XY').box(gw, g, g, centered=True)
    w = w.cut(cq.Workplane('YZ').circle(hollow / 2).extrude(gw).translate((-gw / 2, 0, 0)))
    w = w.union(cq.Workplane('XY').workplane(offset=g / 2).circle(md / 2).extrude(ml))
    w = w.union(cq.Workplane('XY').workplane(offset=g / 2 + ml * 0.35).center(0, md / 2).rect(md * 0.5, md * 0.4).extrude(md * 0.45))
    return w


def ucf_shape(d):
    """4-bolt square flange bearing unit; shaft axis X, flange face at x=0, body toward +X"""
    sq, bc, th, hub = {20: (86, 64, 12, 34), 25: (95, 70, 13, 36), 30: (108, 83, 13, 40), 35: (117, 92, 14, 44),
                       40: (130, 102, 15, 51), 50: (143, 111, 16, 55)}[d]
    w = cq.Workplane('YZ').rect(sq, sq).extrude(th)
    w = w.union(cq.Workplane('YZ').circle(sq * 0.36).extrude(hub))
    w = w.cut(cq.Workplane('YZ').circle(d / 2).extrude(hub))
    w = w.cut(cq.Workplane('YZ').pushPoints([(sx * bc / 2, sy * bc / 2) for sx in (-1, 1) for sy in (-1, 1)]).circle(6).extrude(th))
    return w


def ucp_shape(d):
    """pillow block; shaft axis along X through (z = centre height h), base on z=0, centred"""
    h, a, e, w_ = {20: (33.3, 127, 95, 38), 25: (36.5, 140, 105, 38), 30: (42.9, 165, 121, 48), 35: (47.6, 167, 127, 48),
                   40: (49.2, 184, 137, 54)}[d]
    b = cq.Workplane('XY').box(w_, a, 14, centered=(True, True, False))
    b = b.union(cq.Workplane('YZ').workplane(offset=-w_ / 2).center(0, h).circle(h * 0.85).extrude(w_))
    b = b.union(cq.Workplane('XY').box(w_, h * 1.5, h, centered=(True, True, False)))
    b = b.cut(cq.Workplane('YZ').workplane(offset=-w_ / 2).center(0, h).circle(d / 2).extrude(w_))
    b = b.cut(cq.Workplane('XY').pushPoints([(0, e / 2), (0, -e / 2)]).circle(7).extrude(14))
    return b, h


_COMMON = {}


def common_buy(key, pn, name, wp, spec, color=DARK, mass=None):
    if key not in _COMMON:
        _COMMON[key] = buy(pn, name, wp, spec, color, mass)
    return _COMMON[key]


def gearmotor(kw, hollow, rpm):
    pn = f'CM-G{int(kw * 100):03d}-{hollow}-{rpm}'
    return common_buy(pn, pn, f'Gearmotor {kw:g} kW, {rpm} rpm, hollow shaft dia {hollow}',
                      gearmotor_shape(kw, hollow),
                      f'Shaft-mounted worm/helical gearmotor {kw:g} kW, 400 V 3-ph 50 Hz, output approx. {rpm} rpm, '
                      f'hollow bore {hollow} H7 with keyway, torque arm, IP55', BLUE,
                      {0.18: 9, 0.37: 12, 0.75: 20, 2.2: 45, 4.0: 70}[kw])


def ucf(d):
    pn = f'CM-UCF2{d // 5:02d}'
    return common_buy(pn, pn, f'Flange bearing unit UCF2{d // 5:02d} (shaft {d})', ucf_shape(d),
                      f'UCF2{d // 5:02d} 4-bolt flanged insert bearing unit, bore {d} mm, grub-screw locking', DARK,
                      {20: 0.6, 25: 0.8, 30: 1.1, 35: 1.5, 40: 1.9, 50: 2.6}[d])


def ucp(d):
    pn = f'CM-UCP2{d // 5:02d}'
    sh, h = ucp_shape(d)
    return common_buy(pn, pn, f'Pillow block bearing UCP2{d // 5:02d} (shaft {d})', sh,
                      f'UCP2{d // 5:02d} pillow block insert bearing unit, bore {d} mm', DARK,
                      {20: 0.65, 25: 0.8, 30: 1.3, 35: 1.6, 40: 2.0}[d]), h


# ---------------------------------------------------------------- builders
def table_frame(base, name, Lx, Ly, H, sec=(50, 50, 3), levels=None, color=GREEN, feet=True, foot_hole=14):
    """welded rectangular table / machine frame. Origin at back-left-floor corner of the footprint.
    levels: list of (z_centre, sides) with sides a string of 'F','B','L','R' (rails present).
    default: top rails all round + low rails at 150."""
    a, b, t = sec
    A = Asm(base + '00', name, kind='weldment',
            weld='Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints '
                 '(fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.')
    fz = 8 if feet else 0
    leg = p_shs(base + '01', name + ' - leg', H - fz, a, a, t, color)
    for x in (a / 2, Lx - a / 2):
        for y in (a / 2, Ly - a / 2):
            A.add(leg, (x, y, fz), (0, -90, 0))
    if feet:
        foot = p_plate(base + '04', name + ' - foot plate', a + 20, a + 90, 8,
                       holes=[(0, -(a / 2 + 22), foot_hole), (0, (a / 2 + 22), foot_hole)], color=color,
                       notes='Anchor to container floor with M12 coach bolts / through-bolts.')
        for x in (a / 2, Lx - a / 2):
            for y in (a / 2, Ly - a / 2):
                A.add(foot, (x, y, 0))
    if levels is None:
        levels = [(H - b / 2, 'FBLR'), (150, 'FBLR')]
    lr = sr = None
    for z, sides in levels:
        for s in sides:
            if s in 'FB':
                if lr is None:
                    lr = p_shs(base + '02', name + ' - long rail', Lx - 2 * a, a, b, t, color)
                A.add(lr, (a, a / 2 if s == 'B' else Ly - a / 2, z))
            else:
                if sr is None:
                    sr = p_shs(base + '03', name + ' - cross rail', Ly - 2 * a, a, b, t, color)
                A.add(sr, (a / 2 if s == 'L' else Lx - a / 2, a, z), (0, 0, 90))
    return A


def hopper(base, name, top, bot, h, t=3, color=ORANGE, mat='S235JR', n0=1):
    """4-panel welded pyramid hopper. Centred on Z axis, small opening (bot) at z=0, large opening (top) at z=h.
    Dimensions are INSIDE dimensions. Returns weldment Asm (panels only)."""
    A_, B_ = top; a_, b_ = bot
    Aw = Asm(base + f'{n0 - 1:02d}' if n0 > 1 else base + '00', name, kind='weldment',
             weld='Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, '
                  'then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth '
                  'so material does not hang up.')
    dy = (B_ - b_) / 2; s1 = math.hypot(h, dy); phi1 = math.degrees(math.atan2(h, dy))
    dx = (A_ - a_) / 2; s2 = math.hypot(h, dx); phi2 = math.degrees(math.atan2(h, dx))

    def trap(wb, wt, s):
        return cq.Workplane('XY').polyline([(-wb / 2, 0), (wb / 2, 0), (wt / 2, s), (-wt / 2, s)]).close().extrude(-t)

    p1 = P(base + f'{n0:02d}', name + ' - front/back panel', trap(a_, A_, s1), mat, f'Sheet {t:g} mm', 'LASER', color,
           dims={'Bottom width': a_, 'Top width': A_, 'Slant height': round(s1, 1), 'Thickness': t,
                 'Wall angle to horizontal': f'{phi1:.1f} deg'})
    p2 = P(base + f'{n0 + 1:02d}', name + ' - side panel', trap(b_, B_, s2), mat, f'Sheet {t:g} mm', 'LASER', color,
           dims={'Bottom width': b_, 'Top width': B_, 'Slant height': round(s2, 1), 'Thickness': t,
                 'Wall angle to horizontal': f'{phi2:.1f} deg'})
    Aw.add(p1, (0, b_ / 2, 0), (phi1, 0, 0))
    Aw.add(p1, (0, -b_ / 2, 0), (phi1, 0, 180))
    Aw.add(p2, (a_ / 2, 0, 0), (phi2, 0, -90))
    Aw.add(p2, (-a_ / 2, 0, 0), (phi2, 0, 90))
    return Aw


_FLIGHTS = {}


def flight_part(od, id_, pitch, t=4):
    key = (od, id_, pitch, t)
    if key not in _FLIGHTS:
        blank, dv = flight_blank(od, id_, pitch, t)
        pn = f'CM-F{od:g}-{pitch:g}'
        _FLIGHTS[key] = P(pn, f'Screw flight segment dia {od:g}/{id_:g}, pitch {pitch:g}', flight(od, id_, pitch, t),
                          'S355J2', f'Plate {t:g} mm', 'FLIGHT', STEEL,
                          dims={'Flight OD': od, 'Flight ID': id_, 'Pitch': pitch, 'Thickness': t,
                                'Blank outer radius R': dv['R'], 'Blank inner radius r': dv['r'],
                                'Blank included angle': f"{dv['angle']} deg"},
                          flat=blank,
                          notes='One blank makes one full pitch. Right-hand helix.')
    return _FLIGHTS[key]


def screw_conveyor(base, name, Lt, color=STEEL, kw=0.37, rpm=90, inlet_x=150, pitch=80, outlet_len=120, inlet=True, stub=True):
    """Tubular screw conveyor module. Axis along +X; tube from x=0 (tail/inlet end) to x=Lt (head/drive end).
    Inlet opening on +Z near x=inlet_x; outlet spout on -Z near the head end."""
    OD, T = 114.3, 3.6
    A = Asm(base + '00', name, kind='machine')
    ox = Lt - 110
    cut = cq.Workplane('XY').box(100, 80, 80, centered=(True, True, False)).translate((ox, 0, -OD / 2 - 10))
    if inlet:
        cut = cut.union(cq.Workplane('XY').box(140, 90, 80, centered=(True, True, False)).translate((inlet_x, 0, OD / 2 - 60)))
    tb = P(base + '01', name + ' - casing tube', tube(OD, T, Lt).cut(cut), 'S235JR', 'Tube OD114.3 x 3.6', 'SAW', color,
           dims={'Cut length': Lt, 'OD': OD, 'Wall': T, 'Inlet cut-out (top)': f'140 x 90 at x={inlet_x:g}',
                 'Outlet cut-out (bottom)': f'100 x 80 at x={ox:g}'},
           notes='Saw to length, mark and plasma/grinder-cut the inlet (top) and outlet (bottom) windows. Deburr inside.')
    A.add(tb)
    fl = p_disc(base + '02', name + ' - end flange', 170, 8, bore=45,
                holes=[(sx * 35, sy * 35, 12) for sx in (-1, 1) for sy in (-1, 1)], color=color,
                notes='Bolt pattern 70 x 70 suits UCF205. Weld square to the tube end (fillet a3 all round).')
    A.add(fl, (0, 0, 0), (0, -90, 0))            # plate normal -> -X at tail  (z 0..8 maps to x -8..0)
    A.add(fl, (Lt, 0, 0), (0, 90, 0))            # head
    brg = ucf(25)
    A.add(brg, (-8, 0, 0), (0, 0, 180))
    A.add(brg, (Lt + 8, 0, 0))
    Ls = Lt - 20
    sp = p_tube(base + '03', name + ' - screw centre pipe', 33.7, 4.0, Ls, STEEL,
                notes='Drill 2 x dia 8 cross holes 25 mm from each end (at 90 deg to each other) for the stub-shaft pins after fitting the stubs.')
    A.add(sp, (10, 0, 0))
    st_t = P(base + '04', name + ' - tail stub shaft', stepped([(25.7, 60), (25, 75)]), 'C45', 'Round bar dia 30', 'TURN', STEEL,
             dims={'Plug dia (into pipe)': '25.7 h9 x 60', 'Journal dia': '25 h7 x 75', 'Overall': 135})
    st_h = P(base + '05', name + ' - drive stub shaft', stepped([(25.7, 60), (25, 190)], keys=[(140, 100, 8, 4, 25)]), 'C45',
             'Round bar dia 30', 'TURN', STEEL,
             dims={'Plug dia (into pipe)': '25.7 h9 x 60', 'Journal dia': '25 h7 x 190', 'Keyway': '8 x 4 deep x 100 long', 'Overall': 250})
    A.add(st_t, (70, 0, 0), (0, 0, 180))
    A.add(st_h, (Lt - 70, 0, 0))
    fp = flight_part(98, 34, pitch)
    n = int((Ls - 20) // pitch)
    for i in range(n):
        A.add(fp, (20 + i * pitch, 0, 0), ((i * 0) % 360, 0, 0))
    gm = gearmotor(kw, 25, rpm)
    A.add(gm, (Lt + 8 + 36 + 60, 0, 0))
    if inlet and stub:
        ib = P(base + '06', name + ' - inlet stub', cq.Workplane('XY').rect(150, 100).rect(144, 94).extrude(90),
               'S235JR', 'Sheet 3 mm', 'BEND', color,
               dims={'Inside': '144 x 94', 'Height': 90, 'Sheet': 3},
               notes='Fold from one strip (developed length 488) and seam-weld; scribe the bottom to the tube and weld all round.',
               flat=plate(488, 90, 3))
        A.add(ib, (inlet_x, 0, OD / 2 - 10))
    ob = P(base + '07', name + ' - outlet spout', cq.Workplane('XY').rect(110, 90).rect(104, 84).extrude(outlet_len),
           'S235JR', 'Sheet 3 mm', 'BEND', color,
           dims={'Inside': '104 x 84', 'Height': outlet_len, 'Sheet': 3},
           notes='Fold from one strip (developed length 388) and seam-weld; scribe to the tube and weld all round.',
           flat=plate(388, outlet_len, 3))
    A.add(ob, (ox, 0, -OD / 2 - outlet_len + 12))
    A.hw('M10x35 hex bolt 8.8 + nyloc nut + 2 washers (bearing units)', 8)
    A.hw('Spring pin dia 8 x 40 (stub shafts)', 4)
    A.hw('Parallel key 8x7x90', 1)
    A.hw('Torque-arm bolt M10x60 + rubber bush', 1)
    A.n_flights = n
    return A


def plate_box(base, name, lx, ly, lz, t, omit='', cuts=None, color=STEEL, mat='S235JR', n0=1, weld=None):
    """Welded box from flat plates. Origin = centre of footprint, z 0..lz (outside dimensions).
    Faces: T top, B bottom, F front(+Y), K back(-Y), L left(-X), R right(+X). `omit` lists faces left open.
    cuts: {face: dict(holes=[(x,y,d)], rects=[(x,y,w,h)])} in the plate's own flat coordinates:
       T/B plates: x->X, y->Y ; F/K plates: x->X, y->Z (from plate centre) ; L/R plates: x->Y, y->Z."""
    cuts = cuts or {}
    A = Asm(base + f'{n0 - 1:02d}', name, kind='weldment',
            weld=weld or 'Tack plates square (check diagonals), stitch-weld outside corners 25 mm every 100 mm, '
                         'then seal all seams that must be dust tight with a continuous a2 fillet. Dress sharp edges.')
    sizes = {'T': (lx, ly), 'B': (lx, ly), 'F': (lx, lz - 2 * t), 'K': (lx, lz - 2 * t),
             'L': (ly - 2 * t, lz - 2 * t), 'R': (ly - 2 * t, lz - 2 * t)}
    labels = {'T': 'top plate', 'B': 'bottom plate', 'F': 'front plate', 'K': 'back plate', 'L': 'left plate', 'R': 'right plate'}
    pos = {'T': ((0, 0, lz - t), (0, 0, 0)), 'B': ((0, 0, 0), (0, 0, 0)),
           'F': ((0, ly / 2, lz / 2), (90, 0, 0)), 'K': ((0, -ly / 2 + t, lz / 2), (90, 0, 0)),
           'R': ((lx / 2 - t, 0, lz / 2), (90, 0, 90)), 'L': ((-lx / 2, 0, lz / 2), (90, 0, 90))}
    made = {}
    n = n0
    for f in 'TBFKLR':
        if f in omit:
            continue
        c = cuts.get(f, {})
        key = (sizes[f], repr(c))
        if key not in made:
            twin = [g for g in 'TBFKLR' if g != f and g not in omit and (sizes[g], repr(cuts.get(g, {}))) == key]
            lab = labels[f] if not twin else {'T': 'top/bottom plate', 'F': 'front/back plate', 'L': 'side plate'}.get(f, labels[f])
            made[key] = p_plate(base + f'{n:02d}', f'{name} - {lab}', sizes[f][0], sizes[f][1], t,
                                holes=c.get('holes', ()), rects=c.get('rects', ()), color=color, mat=mat)
            n += 1
        A.add(made[key], *pos[f])
    A.next_n = n
    return A


def bin_shape(lx, ly, lz, wall=4):
    return cq.Workplane('XY').box(lx, ly, lz, centered=(True, True, False)).faces('>Z').shell(-wall)


def tote():
    return common_buy('tote', 'CM-TOTE60', 'Stacking tote 600x400x320 (60 L)', bin_shape(600, 400, 320),
                      'Euro stacking container 600 x 400 x 320 mm, solid walls, PP, blue', SKY, 2.6)


def control_box(w=200, h=300, d=150):
    key = f'ctrl{w}x{h}'
    sh = cq.Workplane('XY').box(w, d, h, centered=(True, True, False))
    sh = sh.union(cq.Workplane('XZ').workplane(offset=-d / 2 - 8).center(0, h * 0.72).circle(18).extrude(8))
    sh = sh.union(cq.Workplane('XZ').workplane(offset=-d / 2 - 6).center(0, h * 0.35).circle(11).extrude(6))
    return common_buy(key, f'CM-CTRL{w}', f'Local control station {w}x{h}x{d}', sh,
                      f'Steel enclosure IP65 {w}x{h}x{d} with start/stop, mushroom E-stop (EN ISO 13850), motor starter / contactor '
                      'with overload, lockable isolator', WHITE, 4)


def bench_scale():
    sh = cq.Workplane('XY').box(350, 300, 55, centered=(True, True, False))
    return common_buy('scale', 'CM-SCALE15', 'Bench scale 15 kg x 5 g', sh,
                      'Stainless bench scale, 15 kg capacity, 5 g resolution, platform approx. 350 x 300 mm, IP65', LGREY, 4)


def between(p1, p2):
    """pos, rot, length to place an X-axis member from p1 to p2"""
    dx, dy, dz = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    Lg = math.sqrt(dx * dx + dy * dy + dz * dz)
    return tuple(p1), (0, -math.degrees(math.asin(dz / Lg)), math.degrees(math.atan2(dy, dx))), Lg
