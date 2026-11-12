"""Interference check: reports pairs of placed parts whose solids overlap by more than a threshold volume.

    python clash_check.py [min_volume_cm3]
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cadquery as cq
from mf import core, plant

MINV = float(sys.argv[1]) * 1000 if len(sys.argv) > 1 else 5000.0     # mm3
SKIP = {'CT-001', 'CT-002', 'TL-001'}
t0 = time.time()
plant.build()
items = []
for a, pos in plant.MACHINES:
    if pos is None:
        continue
    for pn, loc, pth in a.flat(cq.Location(cq.Vector(*pos))):
        if pn in SKIP or core.PARTS[pn].alpha < 1:
            continue
        sh = core.PARTS[pn].shape().moved(loc)
        b = sh.BoundingBox()
        items.append((a.code, pn, pth, sh, (b.xmin, b.ymin, b.zmin, b.xmax, b.ymax, b.zmax)))
print(len(items), 'solids', flush=True)
items.sort(key=lambda it: it[4][0])
cand = []
M = 3.0
for i in range(len(items)):
    bi = items[i][4]
    for j in range(i + 1, len(items)):
        bj = items[j][4]
        if bj[0] > bi[3] - M:
            break
        if bj[1] < bi[4] - M and bj[4] > bi[1] + M and bj[2] < bi[5] - M and bj[5] > bi[2] + M:
            cand.append((i, j))
print(len(cand), 'candidate pairs', flush=True)
out = []
for k, (i, j) in enumerate(cand):
    a, b = items[i], items[j]
    try:
        v = a[3].intersect(b[3]).Volume()
    except Exception:
        continue
    if v > MINV:
        out.append((v, a, b))
out.sort(key=lambda r: -r[0])
print(f'{len(out)} overlaps above {MINV / 1000:g} cm3   ({time.time() - t0:.0f}s)')
for v, a, b in out:
    print(f'{v / 1000:9.1f} cm3   {a[0]}:{a[1]:14s} {"/".join(a[2]):12s} x  {b[0]}:{b[1]:14s} {"/".join(b[2])}')
