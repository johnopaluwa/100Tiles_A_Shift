"""Exports: STEP / STL / DXF per part, STEP per machine and plant, GLB, web-viewer data, BOM data."""
import os, json, base64, csv, math, time
import numpy as np
import cadquery as cq
from cadquery import exporters
from .core import PARTS, ASMS, HARDWARE, Asm
from . import render, plant

DXF_PROCS = ('LASER', 'MESH', 'BOARD')


def ensure(d):
    os.makedirs(d, exist_ok=True)
    return d


def dxf_source(p):
    """-> (workplane-with-solid, z) for the flat profile, or None"""
    if p.flat is not None:
        sh = p.flat
    elif p.proc in DXF_PROCS:
        sh = p.wp
    else:
        return None
    s = sh.val() if hasattr(sh, 'val') else sh
    bb = s.BoundingBox()
    return s, (bb.zmin + bb.zmax) / 2


def export_parts(root):
    ds, dl, dd = ensure(f'{root}/models/step/parts'), ensure(f'{root}/models/stl'), ensure(f'{root}/models/dxf')
    ndxf = 0
    for pn, p in PARTS.items():
        sh = p.shape()
        exporters.export(cq.Workplane('XY').add(sh), f'{ds}/{pn}.step')
        V, T = render.tess(pn)
        write_stl(f'{dl}/{pn}.stl', V, T)
        src = dxf_source(p)
        p.has_dxf = False
        if src:
            s, z = src
            try:
                sec = cq.Workplane('XY').add(s).section(z)
                exporters.exportDXF(sec, f'{dd}/{pn}.dxf')
                p.has_dxf = True; ndxf += 1
            except Exception as e:
                print('  DXF failed', pn, e)
    return ndxf


def write_stl(path, V, T):
    tri = V[T]
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    ln = np.linalg.norm(n, axis=1); ln[ln == 0] = 1
    n = (n / ln[:, None]).astype(np.float32)
    rec = np.zeros(len(T), dtype=[('n', '<f4', 3), ('v', '<f4', (3, 3)), ('a', '<u2')])
    rec['n'] = n; rec['v'] = tri.astype(np.float32)
    with open(path, 'wb') as f:
        f.write(b'Tile microfactory part (mm)'.ljust(80, b' '))
        f.write(np.uint32(len(T)).tobytes())
        f.write(rec.tobytes())


def export_assembly_step(asm, path):
    assy = cq.Assembly(name=asm.code)
    objs = {}
    for i, (pn, loc, pth) in enumerate(asm.flat()):
        p = PARTS[pn]
        if pn not in objs:
            objs[pn] = p.shape()
        assy.add(objs[pn], name=f'{pn}_{i + 1}', loc=loc, color=cq.Color(*p.color, p.alpha))
    assy.save(path)


def export_assemblies(root, with_plant=True):
    d = ensure(f'{root}/models/step/assemblies')
    for a, pos in plant.MACHINES:
        t = time.time()
        export_assembly_step(a, f'{d}/{a.code}.step')
        print(f'  STEP {a.code}  {time.time() - t:.1f}s')
    for code, a in ASMS.items():
        if a.kind == 'weldment':
            export_assembly_step(a, f'{d}/{code}.step')
    if with_plant:
        t = time.time()
        export_assembly_step(ASMS['PLANT'], f'{d}/PLANT_complete.step')
        print(f'  STEP PLANT {time.time() - t:.1f}s')


def b64(a):
    return base64.b64encode(a.tobytes()).decode()


def instances():
    """flat list of plant instances with machine code and path"""
    out = []
    for a, pos in plant.MACHINES:
        if pos is None:
            continue
        base = cq.Location(cq.Vector(*pos))
        for pn, loc, pth in a.flat(base):
            out.append((a.code, pn, render.loc_matrix(loc), pth))
    return out


def export_viewer(root):
    d = ensure(f'{root}/data')
    parts = {}
    for pn, p in PARTS.items():
        V, T = render.tess(pn)
        parts[pn] = dict(v=b64(V.astype(np.float32)), i=b64(T.astype(np.uint32)), c=[round(x, 3) for x in p.color], a=p.alpha)
    inst = [dict(m=code, p=pn, t=[round(float(x), 3) for x in M[:3, :].flatten()], w=(pth[-1] if pth else '')) for code, pn, M, pth in instances()]
    with open(f'{d}/viewer_data.js', 'w') as f:
        f.write('window.MF_GEOM=' + json.dumps(dict(parts=parts, inst=inst), separators=(',', ':')) + ';')
    return len(inst)


def export_glb(root):
    import trimesh
    sc = trimesh.Scene()
    meshes = {}
    R = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]], dtype=float)     # Z-up mm -> Y-up
    S = np.diag([0.001, 0.001, 0.001, 1])
    for k, (code, pn, M, pth) in enumerate(instances()):
        if pn not in meshes:
            V, T = render.tess(pn)
            m = trimesh.Trimesh(V, T, process=False)
            c = PARTS[pn].color
            m.visual = trimesh.visual.TextureVisuals(material=trimesh.visual.material.PBRMaterial(
                baseColorFactor=[c[0], c[1], c[2], PARTS[pn].alpha], metallicFactor=0.2, roughnessFactor=0.7,
                alphaMode='BLEND' if PARTS[pn].alpha < 1 else 'OPAQUE', name=pn))
            meshes[pn] = m
        sc.add_geometry(meshes[pn], node_name=f'{code}/{pn}#{k}', geom_name=pn, transform=R @ S @ M)
    d = ensure(f'{root}/models/glb')
    sc.export(f'{d}/plant.glb')


# ------------------------------------------------------------------ BOM / data
def plant_qty():
    q = {}
    for a, pos in plant.MACHINES:
        if pos is None:
            continue
        for pn, n in a.counts().items():
            q[pn] = q.get(pn, 0) + n
    for k, n in plant.INFO['extra_qty'].items():
        if k in PARTS:
            q[k] = q.get(k, 0) + n
        else:
            for pn, m in ASMS[k].counts().items():
                q[pn] = q.get(pn, 0) + n * m
    return q


def machine_of(pn):
    return pn.split('-')[0]


def tree(asm):
    """nested BOM: list of dict(ref, name, qty, kind, children)"""
    rows = []
    for ref, qty in asm.direct():
        if isinstance(ref, Asm):
            rows.append(dict(ref=ref.code, name=ref.name, qty=qty, kind=ref.kind, children=tree(ref)))
        else:
            rows.append(dict(ref=ref, name=PARTS[ref].name, qty=qty, kind=PARTS[ref].kind))
    return rows


def export_data(root, extra=None):
    d = ensure(f'{root}/data'); ensure(f'{root}/docs')
    q = plant_qty()
    parts = {}
    for pn, p in PARTS.items():
        bb = p.bbox()
        kg = p.kg()
        parts[pn] = dict(name=p.name, mat=p.mat, stock=p.stock, proc=p.proc, kind=p.kind, qty=q.get(pn, 0),
                         kg=None if kg is None else round(kg, 2), bbox=[round(x, 1) for x in bb], dims=p.dims, notes=p.notes, spec=p.spec,
                         dxf=bool(getattr(p, 'has_dxf', False)), route=getattr(p, 'route_final', None), holes=getattr(p, 'holes_txt', None))
    machines = []
    for a, pos in plant.MACHINES:
        c = a.counts()
        mass = sum((PARTS[pn].kg() or 0) * n for pn, n in c.items())
        machines.append(dict(code=a.code, name=a.name, desc=a.desc, pos=pos, tree=tree(a), hw=HARDWARE.get(a.code, []),
                             nparts=len(c), ninst=sum(c.values()), kg=round(mass)))
    weld = {code: dict(name=a.name, weld=a.weld, tree=tree(a), hw=HARDWARE.get(code, [])) for code, a in ASMS.items() if a.kind == 'weldment'}
    sub = {code: dict(name=a.name, tree=tree(a), hw=HARDWARE.get(code, [])) for code, a in ASMS.items() if a.kind == 'machine' and code not in [m['code'] for m in machines] and code != 'PLANT'}
    data = dict(parts=parts, machines=machines, weldments=weld, subs=sub, info=plant.INFO)
    if extra:
        data.update(extra)
    with open(f'{d}/data.js', 'w', encoding='utf-8') as f:
        f.write('window.MF_DATA=' + json.dumps(data, separators=(',', ':'), default=str) + ';')
    with open(f'{root}/docs/BOM_all_parts.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['Part number', 'Name', 'Machine', 'Make/Buy', 'Qty (plant)', 'Material', 'Stock / specification', 'Process', 'Mass each kg', 'Mass total kg',
                    'Size X mm', 'Size Y mm', 'Size Z mm', 'STEP file', 'DXF file', 'Drawing'])
        for pn, p in sorted(parts.items()):
            w.writerow([pn, p['name'], machine_of(pn), 'BUY' if p['kind'] == 'buy' else 'MAKE', p['qty'], p['mat'], p['stock'], p['proc'], p['kg'],
                        None if p['kg'] is None else round(p['kg'] * p['qty'], 1), *p['bbox'], f'models/step/parts/{pn}.step',
                        f'models/dxf/{pn}.dxf' if p['dxf'] else '', f'drawings/parts/{pn}.svg'])
    with open(f'{root}/docs/BOM_hardware.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['Assembly', 'Assembly name', 'Item', 'Qty'])
        for code, rows in HARDWARE.items():
            for desc, n in rows:
                w.writerow([code, ASMS[code].name, desc, n])
    # cut list of linear stock
    with open(f'{root}/docs/Cut_list_sections.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['Stock section', 'Material', 'Part number', 'Name', 'Cut length mm', 'Qty', 'Total length m'])
        rows = []
        for pn, p in PARTS.items():
            if p.proc == 'SAW' and 'Cut length' in p.dims and q.get(pn, 0):
                rows.append([p.stock, p.mat, pn, p.name, p.dims['Cut length'], q[pn], round(p.dims['Cut length'] * q[pn] / 1000, 2)])
        for r in sorted(rows, key=lambda r: (r[0], -r[4])):
            w.writerow(r)
    return data
