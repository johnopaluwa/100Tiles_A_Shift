"""Generates all drawing files: one SVG per part, one PDF per machine (GA sheets + weldment sheets + part sheets), shaded PNGs."""
import os, time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from .core import PARTS, ASMS, Asm
from . import drawing, plant, export, render

VIEW = {'SC': (1, 1.9, 0.8), 'CT': (1, 2.2, 1.3), 'SF': (-1, 1.6, 0.8), 'TL': (1, 1.2, 1.0), 'TT': (1, 1.5, 0.7), 'RC': (1, 2.0, 1.2)}


def sub_asms(asm, out=None):
    out = [] if out is None else out
    for ref, _ in asm.direct():
        if isinstance(ref, Asm) and ref not in out:
            out.append(ref); sub_asms(ref, out)
    return out


def parts_of(asm):
    seen = []
    for pn, _, _ in asm.flat():
        if pn not in seen:
            seen.append(pn)
    return seen


def make_all(root, only=None):
    dp = export.ensure(f'{root}/drawings/parts'); dm = export.ensure(f'{root}/drawings'); di = export.ensure(f'{root}/images')
    qty = export.plant_qty()
    done = set()
    for a, pos in plant.MACHINES:
        if only and a.code not in only:
            continue
        t = time.time()
        with PdfPages(f'{dm}/{a.code}_drawing_set.pdf') as pdf:
            for fig in drawing.asm_sheets(a, VIEW.get(a.code, (1, 1.7, 1.0)), png_path=f'{di}/{a.code}.png', hlr_ok=True):
                pdf.savefig(fig); plt.close(fig)
            for s in sub_asms(a):
                if s.code in done:
                    continue
                done.add(s.code)
                figs = drawing.asm_sheets(s, (1, 1.5, 0.9), png_path=f'{di}/{s.code}.png', hlr_ok=True)
                figs[0].savefig(f'{dp}/{s.code}.svg')
                for fig in figs:
                    pdf.savefig(fig); plt.close(fig)
            for pn in parts_of(a):
                if pn in done and not pn.startswith(a.code + '-'):
                    continue            # shared part already drawn in its own machine set
                fig = drawing.part_sheet(pn, qty.get(pn))
                if pn not in done:
                    fig.savefig(f'{dp}/{pn}.svg'); done.add(pn)
                pdf.savefig(fig); plt.close(fig)
        print(f'  drawings {a.code}: {time.time() - t:.0f}s', flush=True)
    if not only or 'PLANT' in only:
        t = time.time()
        P = ASMS['PLANT']
        skip = [pn for pn, p in PARTS.items() if p.alpha < 1]
        tri, col, ids = render.scene_tris(P, skip)
        render.render(tri, col, ids, (1, 1.8, 1.1), (2400, 1500)).save(f'{di}/PLANT_front_right.png')
        render.render(tri, col, ids, (-1, 1.8, 1.1), (2400, 1500)).save(f'{di}/PLANT_front_left.png')
        sk2 = skip + [pn for pn in PARTS if pn.startswith('SC-')] + ['CT-101', 'CT-102', 'CT-103']
        tri, col, ids = render.scene_tris(P, sk2)
        render.render(tri, col, ids, (0.35, 1.6, 0.75), (2400, 1100)).save(f'{di}/PLANT_line_no_canopy.png')
        sk3 = sk2 + ['CT-001']
        tri, col, ids = render.scene_tris(P, sk3)
        t2 = tri[:, :, [0, 2, 1]].copy(); t2[:, :, 1] *= -1          # (x, -z, y): true view from above, x to the right
        render.render(t2, col, ids, (0, -1, 0.0001), (2600, 1000)).save(f'{di}/PLANT_plan.png')
        with PdfPages(f'{dm}/PLANT_general_arrangement.pdf') as pdf:
            for fig in plant_sheets(root):
                pdf.savefig(fig); plt.close(fig)
        print(f'  plant sheets {time.time() - t:.0f}s', flush=True)


def plant_sheets(root):
    import numpy as np
    from PIL import Image
    from . import layout as LY
    figs = []
    for title, img, note in (
            ('Complete plant - isometric from the front right', 'PLANT_front_right.png', 'Solar canopy 13.8 x 6.9 m over a 40 ft high-cube container; receiving hopper, generator and tile test rig outside.'),
            ('Process line - canopy removed', 'PLANT_line_no_canopy.png', 'Seen from the open front, material flows from right to left: sort, shred, dry + screen sand, weigh, mix, press, cool, trim / stack.'),
            ('Plan view - canopy, roof and container shell removed', 'PLANT_plan.png', 'Seen from above, x to the right: back wall at the bottom, open front and walking aisle at the top. One-way flow from left (sorting) to right (finished tiles).')):
        fig, ax = drawing.new_page()
        im = Image.open(f'{root}/images/{img}')
        w, h = im.size
        bw, bh = 396, 205
        s = min(bw / w, bh / h)
        x0 = 12 + (bw - w * s) / 2; y0 = 64 + (bh - h * s) / 2
        ax.imshow(np.asarray(im), extent=(x0, x0 + w * s, y0, y0 + h * s), zorder=1, interpolation='bilinear')
        ax.set_xlim(0, 420); ax.set_ylim(0, 297)
        drawing.txt(ax, 14, 280, title, 12, drawing.INK, weight='bold')
        drawing.txt(ax, 14, 274, note, 7)
        rows = [(a.code, a.name, '-' if pos is None else f'x={pos[0]:.0f}  y={pos[1]:.0f}') for a, pos in plant.MACHINES]
        drawing.wrap_block(ax, 14, 54, 'MACHINE DATUMS (plant origin = inside back-left floor corner of the container; x along the line, y toward the open front, z up)',
                           '   |   '.join(f'{c}: {p}' for c, n, p in rows if p != '-' and not p.startswith('x=0  y=0')), 150, 5.8, 8)
        drawing.title_block(ax, 'PLANT', 'Plant general arrangement', [('TYPE', 'General arrangement'), ('CONTAINER', '40 ft HC, internal 12032 x 2352 x 2690'),
                                                                        ('OUTPUT', '100 tiles / shift, 2.2 kg each'), ('POWER', '19.8 kWp PV, 40 kWh battery'), ('STEP', 'models/step/assemblies/PLANT_complete.step')], 'NTS')
        figs.append(fig)
    return figs
