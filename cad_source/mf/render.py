"""Tessellation cache + a small numpy z-buffer renderer (shaded CAD-style images, no GPU needed)."""
import math
import numpy as np
from PIL import Image
from .core import PARTS

_TESS = {}


def tess(pn):
    """-> (verts Nx3 float32, tris Mx3 int32) in part-local coordinates"""
    if pn not in _TESS:
        sh = PARTS[pn].shape()
        bb = sh.BoundingBox()
        diag = bb.DiagonalLength
        tol = min(max(diag / 600.0, 0.15), 4.0)
        v, t = sh.tessellate(tol, 0.35)
        V = np.array([(p.x, p.y, p.z) for p in v], dtype=np.float32)
        T = np.array(t, dtype=np.int32).reshape(-1, 3)
        _TESS[pn] = (V, T)
    return _TESS[pn]


def loc_matrix(loc):
    T = loc.wrapped.Transformation()
    M = np.eye(4)
    for i in range(3):
        for j in range(4):
            M[i, j] = T.Value(i + 1, j + 1)
    return M


def scene_tris(asm, skip=()):
    """-> tri (N,3,3) world coords, colour (N,3), instance id (N,)"""
    tri, col, ids = [], [], []
    k = 0
    for pn, loc, _ in asm.flat():
        if pn in skip:
            continue
        V, T = tess(pn)
        if len(T) == 0:
            continue
        M = loc_matrix(loc)
        W = V @ M[:3, :3].T + M[:3, 3]
        tri.append(W[T])
        c = np.array(PARTS[pn].color, dtype=np.float32)
        col.append(np.repeat(c[None, :], len(T), 0))
        k += 1
        ids.append(np.full(len(T), k, dtype=np.int32))
    return np.concatenate(tri), np.concatenate(col), np.concatenate(ids)


def render(tri, col, ids, view=(1, -1.4, 0.9), size=(1500, 1000), bg=(247, 245, 238), ss=2, margin=0.05, return_proj=False):
    w, h = size[0] * ss, size[1] * ss
    f = -np.array(view, dtype=float); f /= np.linalg.norm(f)          # viewing direction (into the screen)
    up = np.array([0, 0, 1.0])
    r = np.cross(f, up); r /= np.linalg.norm(r)
    u = np.cross(r, f)
    P = tri.reshape(-1, 3)
    x = P @ r; y = P @ u; z = P @ f
    xmin, xmax, ymin, ymax = x.min(), x.max(), y.min(), y.max()
    sc = min(w * (1 - 2 * margin) / (xmax - xmin + 1e-9), h * (1 - 2 * margin) / (ymax - ymin + 1e-9))
    sx = (x - (xmin + xmax) / 2) * sc + w / 2
    sy = h / 2 - (y - (ymin + ymax) / 2) * sc
    S = np.stack([sx, sy, z], 1).reshape(-1, 3, 3)
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    ln = np.linalg.norm(n, axis=1); ok = ln > 1e-9
    n[ok] /= ln[ok][:, None]
    light = np.array([0.35, -0.5, 0.8]); light /= np.linalg.norm(light)
    sh = 0.45 + 0.55 * np.abs(n @ light)
    rgb = np.clip(col * sh[:, None] * 255, 0, 255).astype(np.uint8)
    zb = np.full((h, w), np.inf, dtype=np.float32)
    img = np.empty((h, w, 3), dtype=np.uint8); img[:] = bg
    idb = np.zeros((h, w), dtype=np.int32)
    nb = np.zeros((h, w, 3), dtype=np.float32)
    x0 = np.floor(S[:, :, 0].min(1)).astype(int); x1 = np.ceil(S[:, :, 0].max(1)).astype(int)
    y0 = np.floor(S[:, :, 1].min(1)).astype(int); y1 = np.ceil(S[:, :, 1].max(1)).astype(int)
    for i in np.nonzero(ok)[0]:
        ax, ay, az = S[i, 0]; bx, by, bz = S[i, 1]; cx, cy, cz = S[i, 2]
        X0 = max(x0[i], 0); X1 = min(x1[i], w - 1); Y0 = max(y0[i], 0); Y1 = min(y1[i], h - 1)
        if X1 < X0 or Y1 < Y0:
            continue
        den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
        if abs(den) < 1e-12:
            continue
        xs = np.arange(X0, X1 + 1) + 0.5; ys = np.arange(Y0, Y1 + 1) + 0.5
        gx, gy = np.meshgrid(xs, ys)
        l1 = ((by - cy) * (gx - cx) + (cx - bx) * (gy - cy)) / den
        l2 = ((cy - ay) * (gx - cx) + (ax - cx) * (gy - cy)) / den
        l3 = 1 - l1 - l2
        m = (l1 >= -1e-4) & (l2 >= -1e-4) & (l3 >= -1e-4)
        if not m.any():
            continue
        zz = l1 * az + l2 * bz + l3 * cz
        sub = zb[Y0:Y1 + 1, X0:X1 + 1]
        m &= zz < sub
        if not m.any():
            continue
        sub[m] = zz[m]
        img[Y0:Y1 + 1, X0:X1 + 1][m] = rgb[i]
        idb[Y0:Y1 + 1, X0:X1 + 1][m] = ids[i]
        nb[Y0:Y1 + 1, X0:X1 + 1][m] = n[i]
    # edges: instance change, crease or depth jump
    e = np.zeros((h, w), dtype=bool)
    for dy, dx in ((0, 1), (1, 0)):
        a_id = idb[:h - dy, :w - dx]; b_id = idb[dy:, dx:]
        a_n = nb[:h - dy, :w - dx]; b_n = nb[dy:, dx:]
        a_z = zb[:h - dy, :w - dx]; b_z = zb[dy:, dx:]
        dz = np.abs(np.where(np.isfinite(a_z), a_z, 1e9) - np.where(np.isfinite(b_z), b_z, 1e9))
        ee = (a_id != b_id) | ((np.abs((a_n * b_n).sum(2)) < 0.72) & (a_id > 0)) | ((dz > 40 / 1.0) & (dz < 1e8))
        e[:h - dy, :w - dx] |= ee
    img[e] = (img[e] * 0.25).astype(np.uint8)
    im = Image.fromarray(img)
    if ss > 1:
        im = im.resize(size, Image.LANCZOS)
    if return_proj:
        cx, cy = (xmin + xmax) / 2, (ymin + ymax) / 2

        def proj(pts):
            pts = np.asarray(pts, dtype=float)
            return np.stack([((pts @ r - cx) * sc + w / 2) / ss, (h / 2 - (pts @ u - cy) * sc) / ss], 1)
        return im, proj
    return im


def render_asm(asm, path, view=(1, -1.4, 0.9), size=(1500, 1000), skip=()):
    tri, col, ids = scene_tris(asm, skip)
    im = render(tri, col, ids, view, size)
    im.save(path)
    return len(tri)
