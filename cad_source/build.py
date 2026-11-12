"""Master build script.

    python build.py                 -> everything
    python build.py parts asm       -> only the named stages
    python build.py draw HP TL      -> drawings for the named machines only

stages: parts (STEP/STL/DXF per part)  asm (assembly STEP)  viewer (3D viewer data)  glb  draw (drawings)  data (BOM + hub data + guide)
Requires: pip install cadquery matplotlib pillow trimesh numpy
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from mf import core, plant, export, routes

args = sys.argv[1:]
stages = [a for a in args if a.islower()] or ['parts', 'asm', 'viewer', 'glb', 'draw', 'data']
only = [a for a in args if a.isupper()] or None
t0 = time.time()
P = plant.build()
routes.assign()
print(f'model built: {len(core.PARTS)} unique parts, {sum(P.counts().values())} placed, {time.time() - t0:.0f}s', flush=True)
if 'parts' in stages:
    t = time.time(); n = export.export_parts(ROOT); print(f'parts exported (STEP + STL), {n} DXF, {time.time() - t:.0f}s', flush=True)
else:
    for pn, p in core.PARTS.items():
        p.has_dxf = os.path.exists(f'{ROOT}/models/dxf/{pn}.dxf')
if 'asm' in stages:
    t = time.time(); export.export_assemblies(ROOT); print(f'assembly STEP {time.time() - t:.0f}s', flush=True)
if 'viewer' in stages:
    t = time.time(); n = export.export_viewer(ROOT); print(f'viewer data: {n} instances, {time.time() - t:.0f}s', flush=True)
if 'glb' in stages:
    t = time.time(); export.export_glb(ROOT); print(f'glb {time.time() - t:.0f}s', flush=True)
if 'draw' in stages:
    from mf import sheets
    t = time.time(); sheets.make_all(ROOT, only); print(f'drawings {time.time() - t:.0f}s', flush=True)
    try:                       # optional: merge every set into drawings/ALL_drawings.pdf (needs: pip install pymupdf)
        import fitz
        order = ['PLANT_general_arrangement'] + [a.code + '_drawing_set' for a, _ in plant.MACHINES]
        allp = fitz.open(); toc = []
        for k in order:
            f = f'{ROOT}/drawings/{k}.pdf'
            if os.path.exists(f):
                toc.append([1, k.replace('_', ' '), len(allp) + 1]); allp.insert_pdf(fitz.open(f))
        allp.set_toc(toc); allp.save(f'{ROOT}/drawings/ALL_drawings.pdf', deflate=True, garbage=3)
        print(f'merged {len(allp)} sheets into drawings/ALL_drawings.pdf', flush=True)
    except ImportError:
        print('pymupdf not installed - skipped merging drawings/ALL_drawings.pdf', flush=True)
if 'data' in stages:
    from mf import docs
    t = time.time(); docs.make(ROOT); print(f'data + docs {time.time() - t:.0f}s', flush=True)
print(f'done in {time.time() - t0:.0f}s')
