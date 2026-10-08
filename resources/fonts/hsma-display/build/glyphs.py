"""HSMA display lettering, rebuilt from centre lines.

The logo's letters are monoline strokes (~150px at a 745px cap height) with a narrow groove
running along each stroke's centre line, stopping half a stroke short of free ends. Each glyph
here is a list of centre-line paths in logo pixel units (y up, baseline 0, cap height CAP);
`letter()` thickens them into the solid letter and `groove()` cuts the centre line back out.

build_font.py replaces S and M with versions traced from the logo; the rebuilt M here is kept for
calibrate.py and as a reference for other diagonal letters.
"""
import math
from shapely.geometry import LineString, MultiLineString, box, Point
from shapely.ops import unary_union

CAP = 745          # cap height in logo pixels
W = 148            # stroke width (straight strokes)
WD = 126           # stroke width for diagonals, lighter than stems as in the logo's M (121) and A (130)
G = 15             # groove width
H2 = W / 2
ROUND = 9          # outer corner rounding
TOP = CAP - H2     # centre line of top strokes
BOT = H2           # centre line of bottom strokes
MID = 381          # centre line of crossbars (H)


def arc(cx, cy, rx, ry, a0, a1, n=48):
    """Points along an elliptical arc, angles in degrees (0 = right, counter-clockwise)."""
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


class Glyph:
    def __init__(self, width, strokes, diagonal=(), extra=None, groove_strokes=None, clip=True, wd=None, bars=()):
        self.width = width            # advance width of the letter body, excluding side bearings
        self.wd = wd or WD            # stroke width for this glyph's diagonals
        self.bars = bars              # centre lines drawn at W with flat ends, for bars that stop inside other strokes
        self.strokes = strokes        # straight / curved centre lines, drawn at W
        self.diagonal = diagonal      # centre lines drawn at WD
        self.extra = extra            # extra solid geometry (e.g. a dot)
        self.groove_strokes = groove_strokes  # override which centre lines get a groove
        self.clip = clip              # clip to the cap-height box (flat tops on M, A, N...)


def _thicken(paths, width, cap='square'):
    if not paths:
        return None
    return unary_union([LineString(p).buffer(width / 2, cap_style=cap, join_style='mitre', mitre_limit=10)
                        for p in paths])


def letter(g):
    parts = [s for s in (_thicken(g.strokes, W), _thicken(g.diagonal, g.wd), _thicken(g.bars, W, 'flat'), g.extra)
             if s is not None]
    shape = unary_union(parts)
    if g.clip:
        shape = shape.intersection(box(-400, 0, g.width + 400, CAP))
    # Slightly rounded outer corners, as in the logo
    return shape.buffer(-ROUND, join_style='round').buffer(ROUND, join_style='round')


def groove(g):
    paths = g.groove_strokes if g.groove_strokes is not None else list(g.strokes) + list(g.diagonal) + list(g.bars)
    if not paths:
        return None
    return unary_union([LineString(p).buffer(G / 2, cap_style='round', join_style='round') for p in paths])


def outline(g):
    shape = letter(g)
    gr = groove(g)
    return shape.difference(gr) if gr is not None else shape


# ---------------------------------------------------------------- glyph definitions
def build():
    gl = {}
    R = lambda w: w - H2  # centre line of a right-hand stem

    gl['H'] = Glyph(488, [[(H2, BOT), (H2, TOP)], [(R(488), BOT), (R(488), TOP)], [(H2, MID), (R(488), MID)]])
    gl['I'] = Glyph(150, [[(H2, BOT), (H2, TOP)]])
    gl['L'] = Glyph(400, [[(H2, TOP), (H2, BOT), (R(400), BOT)]])
    gl['E'] = Glyph(420, [[(R(420), TOP), (H2, TOP), (H2, BOT), (R(420), BOT)], [(H2, MID), (R(420) - 20, MID)]])
    gl['F'] = Glyph(410, [[(R(410), TOP), (H2, TOP), (H2, BOT)], [(H2, MID), (R(410) - 20, MID)]])
    gl['T'] = Glyph(470, [[(H2, TOP), (R(470), TOP)], [(235, TOP), (235, BOT)]])

    # M: vertical sides, V reaching the baseline; flat tops/bottom come from clipping to the cap-height box.
    # Diagonal centre lines follow the logo's grooves: (128, 654) -> (322, 82), mirrored.
    mw = 644
    dl = lambda y: 128 + (322 - 128) * (y - 654) / (82 - 654)
    gl['M'] = Glyph(mw, [[(H2, BOT), (H2, TOP)], [(R(mw), TOP), (R(mw), BOT)]],
                    diagonal=[[(dl(CAP + 60), CAP + 60), (322, 82), (mw - dl(CAP + 60), CAP + 60)],
                              [(322, 82), (322, -80)]],
                    groove_strokes=[[(H2, BOT), (H2, TOP)], [(R(mw), BOT), (R(mw), TOP)],
                                    [(dl(TOP), TOP), (322, 82), (mw - dl(TOP), TOP)]], wd=128)
    nw = 520
    gl['N'] = Glyph(nw, [[(H2, BOT), (H2, TOP)], [(R(nw), TOP), (R(nw), BOT)]],
                    diagonal=[[(H2, CAP + 40), (R(nw), -40)]],
                    groove_strokes=[[(H2, BOT), (H2, TOP), (R(nw), BOT), (R(nw), TOP)]])

    # A: diagonals along the logo's grooves (89, 69) -> (264, 654), mirrored, meeting in a flat apex;
    # full-weight crossbar centred at y=240
    aw = 557
    al = lambda y: 89 + (264 - 89) * (y - 69) / (654 - 69)
    apex = 680
    gl['A'] = Glyph(aw, [], bars=[[(al(240), 240), (aw - al(240), 240)]],
                    diagonal=[[(al(-80), -80), (aw / 2, al_y_apex := (aw / 2 - 89) * (654 - 69) / (264 - 89) + 69), (aw - al(-80), -80)]],
                    groove_strokes=[[(al(BOT), BOT), (aw / 2, apex - 8), (aw - al(BOT), BOT)], [(al(240), 240), (aw - al(240), 240)]],
                    wd=138)
    # V: built like the centre of the logo's M. The strokes' centre lines meet just above the baseline,
    # which (once clipped) leaves a flat base about 110px wide; the groove follows the centre lines and
    # meets at y=82, as in the M.
    vw = 557
    vx = lambda y: 68 + (vw / 2 - 68) * (y - TOP) / (37 - TOP)   # left centre line
    gl['V'] = Glyph(vw, [], diagonal=[[(vx(CAP + 60), CAP + 60), (vw / 2, 37), (vw - vx(CAP + 60), CAP + 60)],
                                      [(vw / 2, 37), (vw / 2, -80)]],
                    groove_strokes=[[(vx(TOP), TOP), (vw / 2, 82), (vw - vx(TOP), TOP)]], wd=128)

    kw = 480
    gl['K'] = Glyph(kw, [[(H2, BOT), (H2, TOP)]],
                    diagonal=[[(R(kw) + 30, CAP + 40), (H2 + 40, 330)], [(H2 + 120, 400), (R(kw) + 30, -40)]],
                    groove_strokes=[[(H2, BOT), (H2, TOP)], [(R(kw) - 10, TOP), (H2, 330)], [(H2 + 135, 395), (R(kw) - 10, BOT)]])

    # Round letters: stadium-like bowls with the same stroke
    # Round letters overshoot the cap height and baseline slightly, as the logo's S does (by ~10px)
    OVER = 10
    ow = 560
    oh = CAP - W + 2 * OVER
    gl['O'] = Glyph(ow, [arc(ow / 2, CAP / 2, ow / 2 - H2, oh / 2, 0, 360, 96)], clip=False)
    dw = 520
    r = (TOP - BOT) / 2
    gl['D'] = Glyph(dw, [[(H2, BOT), (H2, TOP)],
                         [(H2, TOP), (dw - H2 - r * 0.9, TOP)] + arc(dw - H2 - r * 0.9, CAP / 2, r * 0.9, r, 90, -90) + [(H2, BOT)]])
    bw = 480
    ru = (TOP - MID) / 2
    rl = (MID - BOT) / 2
    gl['B'] = Glyph(bw, [[(H2, BOT), (H2, TOP)],
                         [(H2, TOP), (bw - H2 - ru - 30, TOP)] + arc(bw - H2 - ru - 30, MID + ru, ru, ru, 90, -90) + [(H2, MID)],
                         [(H2, MID), (bw - H2 - rl, MID)] + arc(bw - H2 - rl, BOT + rl, rl, rl, 90, -90) + [(H2, BOT)]])
    pw = 470
    gl['P'] = Glyph(pw, [[(H2, BOT), (H2, TOP)],
                         [(H2, TOP), (pw - H2 - ru, TOP)] + arc(pw - H2 - ru, MID + ru - 15, ru, ru + 15, 90, -90) + [(H2, MID - 30)]])
    gl['R'] = Glyph(500, [[(H2, BOT), (H2, TOP)],
                          [(H2, TOP), (500 - H2 - ru - 20, TOP)] + arc(500 - H2 - ru - 20, MID + ru - 15, ru, ru + 15, 90, -90) + [(H2, MID - 30)]],
                    diagonal=[[(250, MID - 30), (500 - 40, -60)]],
                    groove_strokes=[[(H2, BOT), (H2, TOP)],
                                    [(H2, TOP), (500 - H2 - ru - 20, TOP)] + arc(500 - H2 - ru - 20, MID + ru - 15, ru, ru + 15, 90, -90) + [(H2, MID - 30)],
                                    [(270, MID - 30), (500 - H2 - 10, BOT)]])
    cw = 520
    gl['C'] = Glyph(cw, [arc(cw / 2 + 10, CAP / 2, cw / 2 - H2, oh / 2, 40, 320, 80)],
                    groove_strokes=[arc(cw / 2 + 10, CAP / 2, cw / 2 - H2, oh / 2, 52, 308, 80)], clip=False)
    uw = 500
    # (the arc's end points repeat the stems' end points, so drop them: a doubled point makes a spike at the join)
    gl['U'] = Glyph(uw, [[(H2, TOP), (H2, uw / 2)] + arc(uw / 2, uw / 2, uw / 2 - H2, uw / 2 - H2 + OVER, 180, 360)[1:-1]
                         + [(R(uw), uw / 2), (R(uw), TOP)]],
                    clip=False)

    # 7: top bar running into a long diagonal; the diagonal's outer edge forms the top-right corner,
    # so nothing overhangs it
    sw = 470
    sx = lambda y: 395 + (130 - 395) * (y - CAP) / (-60 - CAP)    # diagonal centre line
    gl['seven'] = Glyph(sw, [], diagonal=[[(sx(CAP + 60), CAP + 60), (sx(-60), -60)]],
                        extra=box(0, CAP - W, sx(CAP - W / 2), CAP),
                        groove_strokes=[[(H2, TOP), (sx(TOP), TOP), (sx(BOT), BOT)]])

    # λ: long stroke from top-left down to bottom-right, short leg to bottom-left
    lw = 500
    gl['lambda'] = Glyph(lw, [], diagonal=[[(60, CAP + 30), (lw - 30, -60)], [(250, 360), (25, -60)]],
                         groove_strokes=[[(85, TOP), (lw - 80, BOT)], [(235, 345), (85, BOT)]])

    # Brackets: flat arcs a little taller than the caps, at the lighter diagonal weight
    pr, pa = 700, 38            # arc radius and half-angle
    bw = 300
    cx = 75 + pr
    gl['parenleft'] = Glyph(bw, [], diagonal=[arc(cx, CAP / 2, pr, pr, 180 - pa, 180 + pa, 40)], clip=False, wd=120)
    gl['parenright'] = Glyph(bw, [], diagonal=[arc(bw - cx, CAP / 2, pr, pr, pa, -pa, 40)], clip=False, wd=120)

    gl['hyphen'] = Glyph(320, [[(H2, MID), (320 - H2, MID)]])
    gl['period'] = Glyph(150, [], extra=box(0, 0, 150, 150), groove_strokes=[])
    gl['periodcentered'] = Glyph(150, [], extra=box(0, MID - 75, 150, MID + 75), groove_strokes=[])
    return gl
