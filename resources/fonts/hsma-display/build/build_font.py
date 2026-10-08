"""Build HSMA Display (grooved, like the logo) and HSMA Display Solid as TTF + WOFF2.

Usage: python build_font.py [logo png] [out dir]
Defaults to the white HSMA logo in resources/ and writes the fonts to resources/fonts/hsma-display/.
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from shapely.geometry import Polygon, MultiPolygon
from shapely.geometry.polygon import orient
from shapely.ops import unary_union

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glyphs import build, outline, letter, CAP  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
LOGO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, 'resources', 'Chalky HSMA-07-wide white logo.png')
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.abspath(os.path.join(HERE, '..'))
os.makedirs(OUT, exist_ok=True)

UPM = 1000
CAP_UNITS = 700
SCALE = CAP_UNITS / CAP
SB = 45                      # side bearing each side, in font units
TOPY, BOTY = 467, 1211       # cap top / baseline rows of the wordmark in the logo
MARGIN = 30                  # extra rows above/below so round letters keep their overshoot
TRACED = {'S': (2760, 3262), 'M': (3436, 4079)}   # letters taken directly from the logo


def traced(seg):
    """A logo letter traced from the high-resolution image: (with groove, solid, width).

    y is measured up from the logo's baseline, so the S keeps its overshoot above and below.
    """
    im = np.array(Image.open(LOGO))
    r0 = TOPY - MARGIN
    m = (im[r0:BOTY + MARGIN + 1, seg[0]:seg[1] + 1, 3] > 128).astype(np.uint8)
    contours, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    to_xy = lambda cc: [(p[0][0], BOTY - (r0 + p[0][1])) for p in cc]
    polys = []
    for i, c in enumerate(contours):
        if hier[0][i][3] != -1:
            continue  # holes are attached to their parent below
        holes = []
        child = hier[0][i][2]
        while child != -1:
            if len(contours[child]) >= 3:
                holes.append(to_xy(contours[child]))
            child = hier[0][child][0]
        polys.append(Polygon(to_xy(c), holes).buffer(0))
    # Every hole in S and M is groove (neither has a counter), so the solid letter is just the outer shapes
    outer = unary_union([Polygon(p.exterior) for p in polys])
    return unary_union(polys), outer, seg[1] - seg[0] + 1


def to_units(geom):
    from shapely import affinity
    g = affinity.scale(geom, xfact=SCALE, yfact=SCALE, origin=(0, 0))
    g = affinity.translate(g, xoff=SB)
    return g.simplify(0.6, preserve_topology=True)


def draw(geom, pen):
    polys = geom.geoms if isinstance(geom, MultiPolygon) else [geom]
    for p in polys:
        if p.is_empty:
            continue
        p = orient(p, sign=-1.0)  # TrueType: outer contours clockwise, holes anticlockwise
        for ring in [p.exterior] + list(p.interiors):
            pts = [(round(x), round(y)) for x, y in ring.coords[:-1]]
            dedup = [pt for i, pt in enumerate(pts) if pt != pts[i - 1]]
            if len(dedup) < 3:
                continue
            pen.moveTo(dedup[0])
            for pt in dedup[1:]:
                pen.lineTo(pt)
            pen.closePath()


def glyph_from(geom):
    pen = TTGlyphPen(None)
    if geom is not None:
        draw(geom, pen)
    return pen.glyph()


def make_font(style, solid):
    defs = build()
    shapes = {}
    for name, g in defs.items():
        shapes[name] = (to_units(letter(g) if solid else outline(g)), g.width)
    for name, seg in TRACED.items():
        grooved, solid_shape, w = traced(seg)
        shapes[name] = (to_units(solid_shape if solid else grooved), w)

    order = ['.notdef', 'space'] + sorted(shapes)
    glyphs, metrics = {}, {}
    pen = TTGlyphPen(None)
    for rect in [((50, 0), (450, 0), (450, 700), (50, 700)), ((110, 60), (110, 640), (390, 640), (390, 60))]:
        pen.moveTo(rect[0]); [pen.lineTo(p) for p in rect[1:]]; pen.closePath()
    glyphs['.notdef'] = pen.glyph(); metrics['.notdef'] = (500, 50)
    glyphs['space'] = TTGlyphPen(None).glyph(); metrics['space'] = (260, 0)
    for name, (geom, w) in shapes.items():
        glyphs[name] = glyph_from(geom)
        adv = round(w * SCALE) + 2 * SB
        metrics[name] = (adv, SB)

    cmap = {0x20: 'space', 0x28: 'parenleft', 0x29: 'parenright', 0x2D: 'hyphen', 0x2E: 'period',
            0xB7: 'periodcentered', 0x3BB: 'lambda', 0x39B: 'lambda',
            0x2C: 'comma', 0x3A: 'colon', 0x27: 'quotesingle', 0x2019: 'quotesingle', 0x21: 'exclam',
            0x3F: 'question', 0x2F: 'slash'}
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, name in enumerate(digits):
        cmap[0x30 + i] = name
    for name in shapes:
        if len(name) == 1 and name.isalpha():
            cmap[ord(name)] = name
            cmap[ord(name.lower())] = name   # lowercase types the same capitals, so no text-transform is needed

    family = 'HSMA Display' + (' Solid' if solid else '')
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=820, descent=-180)
    fb.setupNameTable({'familyName': family, 'styleName': 'Regular',
                       'uniqueFontIdentifier': family.replace(' ', '') + '-Prototype',
                       'fullName': family, 'psName': family.replace(' ', '') + '-Regular',
                       'version': 'Version 0.1 (prototype)'})
    fb.setupOS2(sTypoAscender=820, sTypoDescender=-180, sTypoLineGap=0, usWinAscent=900, usWinDescent=200,
                sCapHeight=CAP_UNITS, sxHeight=CAP_UNITS, achVendID='HSMA')
    fb.setupPost()
    # J's top-left is empty, so pull it in after round letters
    fb.addOpenTypeFeatures("languagesystem DFLT dflt; languagesystem latn dflt; languagesystem grek dflt; "
                           "feature kern { pos [O Q D zero] J -60; } kern;")
    base = os.path.join(OUT, family.replace(' ', '') + '-Regular')
    fb.save(base + '.ttf')
    f = TTFont(base + '.ttf')
    f.flavor = 'woff2'
    f.save(base + '.woff2')
    print(family, len(order), 'glyphs ->', base + '.ttf/.woff2')


make_font('Regular', solid=False)
make_font('Regular', solid=True)
