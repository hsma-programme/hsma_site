"""Overlay rebuilt letters on the logo originals: white = both, red = original only, blue = rebuilt only.

Usage: python calibrate.py [logo png]  -> writes calib.png next to this script (not committed).
"""
import sys, os
import numpy as np
import cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glyphs import build, outline, CAP

d = os.path.dirname(os.path.abspath(__file__))
LOGO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(d, '..', '..', '..', 'Chalky HSMA-07-wide white logo.png')
TOPY, BOTY = 467, 1211          # cap top / baseline rows of the wordmark in the logo
SEGS = {'H': (2101, 2588), 'S': (2760, 3262), 'M': (3436, 4079), 'A': (4241, 4797)}

im = np.array(Image.open(LOGO))
mask = (im[:, :, 3] > 128).astype(np.uint8)
gl = build()
rows = []
for name in ['H', 'M', 'A']:
    x0, x1 = SEGS[name]
    orig = mask[TOPY:BOTY + 1, x0:x1 + 1]
    h, w = orig.shape
    rend = np.zeros_like(orig)
    geom = outline(gl[name])
    polys = getattr(geom, 'geoms', [geom])
    for p in polys:
        ext = np.array([[x, CAP - y] for x, y in p.exterior.coords], dtype=np.int32)
        cv2.fillPoly(rend, [ext], 1)
        for hole in p.interiors:
            cv2.fillPoly(rend, [np.array([[x, CAP - y] for x, y in hole.coords], dtype=np.int32)], 0)
    inter = (orig & rend).sum(); union = (orig | rend).sum()
    print(name, 'IoU %.3f' % (inter / union), 'orig width', w)
    rgb = np.zeros((h, w, 3), np.uint8)
    rgb[(orig == 1) & (rend == 1)] = (235, 235, 235)
    rgb[(orig == 1) & (rend == 0)] = (255, 40, 40)
    rgb[(orig == 0) & (rend == 1)] = (40, 120, 255)
    rows.append(rgb)
gap = np.zeros((rows[0].shape[0], 30, 3), np.uint8)
out = np.concatenate(sum([[r, gap] for r in rows], [])[:-1], axis=1)
Image.fromarray(out).resize((out.shape[1] // 2, out.shape[0] // 2)).save(os.path.join(d, 'calib.png'))
