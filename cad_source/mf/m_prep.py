"""Material preparation: ST sorting table, SH shredder, SF sand feed, DR rotary dryer, VS vibrating screen, DC dust collector."""
import math
import cadquery as cq
from .core import *
from . import layout as LY


# =============================================================== ST  sorting table
def build_ST():
    A = Asm('ST', 'Station 1a - Sorting table', desc='Hand sorting of incoming plastic. Only HDPE (resin code 2) goes on to the shredder.')
    fr = table_frame('ST-1', 'Sorting table frame', 900, 600, 830, sec=(40, 40, 2.5), levels=[(810, 'FBLR'), (200, 'BLR')])
    A.add(fr)
    top = P('ST-201', 'Sorting table top', plate(940, 640, 20), 'HDPE', 'HDPE board 20 mm', 'BOARD', WHITE,
            dims={'Length': 940, 'Width': 640, 'Thickness': 20},
            notes='Fix to the top rails with 8 x M6x50 countersunk screws into rivet nuts. Break all edges R3.')
    A.add(top, (450, 300, 830))
    A.add(buy('ST-301', 'Reject bin 80 L, red', bin_shape(400, 400, 600), '80 L rigid PP bin, RED, labelled "PVC / PET / unknown - REJECT"', RED, 3.5), (-220, 220, 0))
    A.add(buy('ST-302', 'HDPE bin 80 L, green', bin_shape(400, 400, 600), '80 L rigid PP bin, GREEN, labelled "HDPE only"', GREEN, 3.5), (-220, 680, 0))
    A.hw('M6x50 countersunk screw + rivet nut', 8)
    A.hw('M12x100 floor anchor / through bolt', 8)
    return A


# =============================================================== SH  shredder
def _knife(off):
    pts = []
    for k in range(3):
        for i in range(11):
            th = math.radians(k * 120 - 8 + 128 * i / 10)
            r = 62 + 28 * i / 10
            pts.append((r * math.cos(th), r * math.sin(th)))
    w = cq.Workplane('XY').polyline(pts).close().extrude(10)
    hx = cq.Workplane('XY').transformed(rotate=(0, 0, off)).polygon(6, 36.2 / math.cos(math.radians(30))).extrude(10)
    return w.cut(hx)


def build_SH():
    A = Asm('SH', 'Station 1b - Low-speed shredder', desc='Single-shaft, 15-knife low-speed shredder. 4 kW, ~70 rpm, 8 mm screen. 30-50 kg/h HDPE flakes.')
    ZS = 950.0            # shaft centre height
    CX, CY = 400.0, 576.0  # chamber centre
    fr = table_frame('SH-1', 'Shredder frame', 800, 950, 800, sec=(60, 60, 4), levels=[(770, 'FBLR'), (200, 'BLR')])
    A.add(fr)
    deck = p_plate('SH-201', 'Shredder deck plate', 800, 950, 10, holes=[(0, 255 - 475, 260)] + [(sx * 150, CY - 475 + sy * 196, 13) for sx in (-1, 1) for sy in (-1, 0, 1)],
                   rects=[(0, CY - 475, 222, 304)], color=GREEN, mat='S235JR',
                   notes='Stitch-weld to the frame top (50 every 150). The dia 260 hole clears the gearmotor; the 222 x 304 window is the flake discharge.')
    A.add(deck, (400, 475, 800))
    # --- cutting chamber weldment
    C = Asm('SH-210', 'Cutting chamber', kind='weldment',
            weld='Clamp both end plates on a dummy shaft through the dia 50 bores so the bearing seats stay co-axial, tack the side plates '
                 'and flanges, check the 220 inside width with a gauge block, then weld (a4 fillets outside, stitch inside).')
    endp = p_plate('SH-211', 'Chamber end plate (bearing plate)', 244, 250, 15,
                   holes=[(0, -5, 50)] + [(sx * 46, -5 + sy * 46, 14) for sx in (-1, 1) for sy in (-1, 1)], color=BLUE, mat='S355J2',
                   notes='Bore dia 50 and the 4 x dia 14 (92 x 92, UCF207) must be positioned within 0.2 mm - drill both plates clamped together.')
    C.add(endp, (CX, 425, ZS - 5 + 0), (90, 0, 0))
    C.add(endp, (CX, 742, ZS - 5 + 0), (90, 0, 0))
    sidep = p_plate('SH-212', 'Chamber side plate', 302, 250, 12, color=BLUE, mat='S355J2')
    C.add(sidep, (CX - 122, CY, ZS - 5), (90, 0, 90))
    C.add(sidep, (CX + 110, CY, ZS - 5), (90, 0, 90))
    fl = p_plate('SH-213', 'Chamber flange (top / bottom)', 344, 432, 10, rects=[(0, 0, 222, 304)],
                 holes=[(sx * 150, sy * 196, 13) for sx in (-1, 1) for sy in (-1, 0, 1)], color=BLUE, mat='S235JR')
    C.add(fl, (CX, CY, 810)); C.add(fl, (CX, CY, ZS - 5 + 125))
    sup = p_angle('SH-242', 'Comb support angle', 302, 40, 40, 5, color=BLUE,
                  notes='Weld inside the chamber, top face 10 mm below shaft centre. Drill and tap 3 x M10 at 100 pitch through the horizontal leg, 20 from the heel.')
    C.add(sup, (CX - 110, 425, ZS - 10), (180, 0, 90))
    C.add(sup, (CX + 110, 727, ZS - 10), (180, 0, -90))
    A.add(C)
    # --- rotor
    shaft = stepped([(35, 276)]).union(cq.Workplane('YZ').workplane(offset=276).polygon(6, 36 / math.cos(math.radians(30))).extrude(300))
    shaft = shaft.union(cq.Workplane('YZ').workplane(offset=576).circle(17.5).extrude(66))
    shaft = shaft.cut(cq.Workplane('XY').box(170, 10, 10, centered=(False, True, False)).translate((12, 0, 12.5)))
    P('SH-221', 'Rotor shaft (hex 36 A/F)', shaft, 'C45', 'Hexagon bar 36 A/F', 'TURN', STEEL,
      dims={'Overall length': 642, 'Hex section': '36 A/F x 300 (left as drawn bar)', 'Drive journal': 'dia 35 k6 x 276',
            'Front journal': 'dia 35 k6 x 66', 'Keyway': '10 P9 x 5 deep x 170 (for 10x8 key)'},
      route=['Saw hexagon bar 36 A/F (C45, bright drawn) to 646 mm.',
             'Lathe, 3-jaw on the hex with soft jaws: face and centre-drill both ends to 642 mm overall.',
             'Between centres: turn the drive end to dia 35 k6 for 276 mm and the front end to dia 35 k6 for 66 mm. '
             'Leave R1 fillets at the hex shoulders; do not touch the hex section.',
             'Mill the 10 P9 x 5 deep keyway, 170 long, starting 12 mm from the drive end.',
             'Deburr, check both journals run true to each other within 0.05 mm TIR.'])
    A.add('SH-221', (CX, 150, ZS), (0, 0, 90))
    knives = [P(f'SH-23{i + 1}', f'Rotary knife, type {"ABC"[i]} (hex at {i * 20} deg)', _knife(i * 20), 'Hardox 450', 'Plate 10 mm', 'LASER', DARK,
                dims={'Tip circle': 180, 'Root circle': 124, 'Thickness': 10, 'Hex bore': '36.2 A/F', 'Hex rotation': f'{i * 20} deg', 'Teeth': 3},
                notes='Laser or waterjet cut from Hardox 450 (do NOT plasma cut - the heat softens the edge). Surface-grind both faces only if the plate is not flat within 0.2 mm. '
                      'Grind a 5 deg relief behind each hook tip. The three types differ only in the angle of the hex bore, which staggers the teeth into a helix.')
              for i in range(3)]
    spacer = P('SH-234', 'Rotor spacer', cq.Workplane('XY').circle(32).extrude(10).cut(cq.Workplane('XY').polygon(6, 36.2 / math.cos(math.radians(30))).extrude(10)),
               'S355J2', 'Plate 10 mm', 'LASER', STEEL, dims={'OD': 64, 'Thickness': 10, 'Hex bore': '36.2 A/F'},
               notes='Must be the same thickness as the knives within 0.05 mm; cut both from the same plate.')
    for k in range(15):
        A.add(knives[k % 3], (CX, 426 + 20 * k, ZS), (-90, 0, 0))
        A.add(spacer, (CX, 436 + 20 * k, ZS), (-90, 0, 0))
    comb = p_plate('SH-241', 'Fixed comb (counter knife)', 76, 300, 10, rects=[(8, -145 + 20 * k, 62, 12) for k in range(15)],
                   color=DARK, mat='Hardox 450',
                   notes='Fingers are 8 mm wide and sit in the gaps between the rotary knives with 1 mm side clearance. '
                         '3 x dia 11 holes on the back strip are match-drilled from the support angle on assembly; shim so the finger tips clear the spacers by 2 mm.')
    A.add(comb, (CX - 72, CY, ZS - 10))
    A.add(comb, (CX + 72, CY, ZS), (0, 180, 0))
    scr = tube(204, 4, 300).cut(cq.Workplane('XY').box(320, 240, 140, centered=(False, True, False)).translate((-10, 0, -15)))
    holes = [(-135 + 12 * i + (6 if j % 2 else 0), -140 + 10.4 * j, 8) for i in range(23) for j in range(28)]
    P('SH-251', 'Screen, dia 8 perforation', scr, 'S355J2', 'Sheet 4 mm', 'ROLL', STEEL,
      dims={'Inside radius': 98, 'Length': 300, 'Flat blank': '284 x 300', 'Perforation': 'dia 8 holes, 12 mm staggered pitch'},
      notes='Laser the perforated blank flat (DXF), then roll to R98 inside with the burr side outward. Sits in the comb support angles; held by 2 x M8 each side.',
      flat=plate(284, 300, 4, holes=[(x, y, d) for x, y, d in holes if abs(x) < 132 and abs(y) < 140]))
    A.add('SH-251', (CX, 426, ZS), (0, 0, 90))
    A.add(ucf(35), (CX, 410, ZS), (0, 0, -90)); A.add(ucf(35), (CX, 742, ZS), (0, 0, 90))
    A.add(gearmotor(4.0, 35, 70), (CX, 255, ZS), (180, 0, 90))
    ta = p_plate('SH-281', 'Gearmotor torque arm', 80, 180, 10, holes=[(0, -70, 13), (0, 70, 17)], color=BLUE,
                 notes='Bolts to the gearbox torque-arm lug; the dia 17 end takes an M16 bolt with rubber bushes anchored to the deck.')
    A.add(ta, (CX + 122, 255, ZS - 45), (90, 0, 90))
    # --- feed hopper
    H = hopper('SH-26', 'Shredder feed hopper', (700, 600), (220, 302), 400, t=3, color=ORANGE)
    A.add(H, (CX, CY, ZS + 136))
    hf = p_plate('SH-263', 'Hopper flange', 344, 432, 6, rects=[(0, 0, 220, 302)],
                 holes=[(sx * 150, sy * 196, 13) for sx in (-1, 1) for sy in (-1, 0, 1)], color=ORANGE)
    A.add(hf, (CX, CY, ZS + 130))
    sk = P('SH-271', 'Discharge skirt', cq.Workplane('XY').rect(226, 308).rect(222, 304).extrude(300), 'DC01 galv.', 'Sheet 2 mm', 'BEND', STEEL,
           dims={'Inside': '222 x 304', 'Height': 300, 'Sheet': 2},
           notes='Fold from one strip 1060 x 300 with a 20 mm top flange on each side; spot/stitch-weld the seam. Screw to the underside of the deck.',
           flat=plate(1060, 320, 2))
    A.add(sk, (CX, CY, 500))
    A.add(tote(), (CX, CY, 0), (0, 0, 90))
    post = p_shs('SH-291', 'Control post', 500, 40, 40, 3, GREEN)
    A.add(post, (30, 920, 810), (0, -90, 0))
    A.add(control_box(), (120, 1016, 1000))
    A.hw('M12x40 hex bolt 8.8 + nut + washers (chamber flange to deck, hopper flange)', 12)
    A.hw('M12x45 hex bolt 8.8 + nyloc nut (UCF207 bearing units)', 8)
    A.hw('M10x25 socket cap screw 12.9 (comb to support angle)', 6)
    A.hw('Parallel key 10x8x160', 1)
    A.hw('M12x100 floor anchor', 8)
    return A


# =============================================================== SF  sand feed
def build_SF():
    """built directly in plant coordinates"""
    A = Asm('SF', 'Station 2a - Sand receiving hopper and feed screws',
            desc='0.36 m3 receiving hopper outside the container (loaded by skid-steer), 45 deg elevating screw, '
                 'overhead transfer screw crossing the aisle at 2.09 m clear height into the dryer inlet.')
    G = LY.G
    cy = LY.HOPPER_CY
    rise = (LY.SCREW2_Z + 57.15 - 10 + 90 + 60 + LY.SPOUT) - (G + 425)
    cx = LY.SCREW2_X - LY.SPOUT - rise
    x0, y0 = cx - 640, cy - 640
    st = table_frame('SF-1', 'Sand hopper stand', 1280, 1280, 1340, sec=(80, 80, 4),
                     levels=[(1300, 'FBLR'), (700, 'FBLR'), (300, 'FBL')], foot_hole=18)
    A.add(st, (x0, y0, G))
    # hopper weldment (origin = centre of the 250 outlet)
    H = hopper('SF-2', 'Sand receiving hopper', (1100, 1100), (250, 250), 700, t=4, color=ORANGE)
    band = p_plate('SF-203', 'Hopper top band', 1104, 150, 4, color=ORANGE)
    H.add(band, (2, 554, 775), (90, 0, 0)); H.add(band, (-2, -550, 775), (90, 0, 0))
    H.add(band, (550, -2, 775), (90, 0, 90)); H.add(band, (-554, 2, 775), (90, 0, 90))
    rim = p_angle('SF-204', 'Hopper support rim angle', 1158, 50, 50, 5, color=ORANGE,
                  notes='Welded round the hopper at the band joint; the horizontal leg sits on the stand top rails (2 x M12 per side).')
    H.add(rim, (-604, 554, 695)); H.add(rim, (604, -554, 695), (0, 0, 180))
    H.add(rim, (554, 604, 695), (0, 0, -90)); H.add(rim, (-554, -604, 695), (0, 0, 90))
    gb = p_rod('SF-205', 'Grizzly bar', 12, 1100, STEEL)
    for i in range(11):
        H.add(gb, (-550, -450 + 90 * i, 800))
    ge = p_flat('SF-206', 'Grizzly end flat', 1100, 30, 5, ORANGE)
    H.add(ge, (-547, -550, 800), (90, 0, 90)); H.add(ge, (547, -550, 800), (90, 0, 90))
    H.weld += ' Then weld the top band, the rim angles and the grizzly (bars at 90 mm pitch keep stones, roots and hands out of the screw).'
    A.add(H, (cx, cy, G + 645))
    # feed boot around the screw inlet
    boot = cq.Workplane('XY').box(258, 258, 360, centered=(True, True, False)).faces('>Z').shell(-4)
    boot = boot.cut(cq.Workplane('YZ').circle(58.5).extrude(900).translate((-450, 0, 0)).rotate((0, 0, 0), (0, 1, 0), -45).translate((0, 0, 140)))
    P('SF-251', 'Flood-feed boot', boot, 'S235JR', 'Plate 4 mm', 'WELD', ORANGE,
      dims={'Inside': '250 x 250 x 356', 'Plate': 4, 'Tube penetrations': 'dia 117 at 45 deg, both side walls, on the boot centre line'},
      notes='Fabricate from 5 flat plates (4 walls 250/258 x 360, base 258 x 258). Offer the casing tube through at 45 deg, scribe and cut the two '
            'elliptical penetrations, then seal-weld round the tube. Bolt the open top to the hopper outlet with a 30 x 5 flat flange.')
    A.add('SF-251', (cx, cy, G + 285))
    # screw 1 : 45 deg elevating screw along +X
    axial = rise / LY.S45
    Lt1 = round(250 + axial + 110)
    S1 = screw_conveyor('SF-3', 'Elevating screw (45 deg)', Lt1, color=STEEL, kw=0.75, rpm=120, inlet_x=250, pitch=80, stub=False)
    tail = (cx - 250 * LY.S45, cy, G + 425 - 250 * LY.S45)
    A.add(S1, tail, (0, -45, 0))
    # support post for screw 1
    d = 2800
    px, pz = tail[0] + d * LY.S45, tail[2] + d * LY.S45 - 57.15 / LY.S45 - 75
    post1 = p_shs('SF-501', 'Elevating screw support post', round(pz - G - 20), 80, 80, 4, GREEN)
    A.add(post1, (px, cy, G + 10), (0, -90, 0))
    bp = p_plate('SF-502', 'Post base plate', 250, 250, 10, holes=[(sx * 95, sy * 95, 18) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN)
    A.add(bp, (px, cy, G))
    cap = p_plate('SF-503', 'Post saddle plate', 160, 160, 10, holes=[(-62, 0, 13), (62, 0, 13)], color=GREEN,
                  notes='Welded on the post top; the casing tube is held down with an M12 U-bolt (DN100) over a 45 deg steel wedge packer about 65 mm high, made to suit on site.')
    A.add(cap, (px, cy, pz - 10))
    # screw 2 : horizontal overhead transfer screw along -Y
    ytail = cy + 250
    Lt2 = round(ytail - LY.DR_AXIS_Y + 110)
    S2 = screw_conveyor('SF-4', 'Overhead transfer screw', Lt2, color=STEEL, kw=0.37, rpm=90, inlet_x=250, pitch=80, outlet_len=400)
    A.add(S2, (LY.SCREW2_X, ytail, LY.SCREW2_Z), (0, 0, -90))
    post2 = p_shs('SF-511', 'Transfer screw support post', round(LY.SCREW2_Z - 57.15 - 10 - G - 10), 80, 80, 4, GREEN)
    A.add(post2, (LY.SCREW2_X, cy + 380, G + 10), (0, -90, 0))
    A.add(bp, (LY.SCREW2_X, cy + 380, G)); A.add(cap, (LY.SCREW2_X, cy + 380, LY.SCREW2_Z - 57.15 - 10))
    clamp = common_buy('clamp114', 'CM-CLAMP114', 'Pipe clamp DN100 with M12 hanger rod', tube(126, 5, 30).union(rod(12, 480).rotate((0, 0, 0), (0, 1, 0), -90).translate((15, 0, 62))),
                       'Two-piece steel pipe clamp for OD 114.3, M12 boss, with M12 threaded rod 500 mm and roof/beam fixing', DARK, 1.2)
    A.add(clamp, (LY.SCREW2_X, 2200, LY.SCREW2_Z), (0, 0, -90))
    A.add(clamp, (LY.SCREW2_X, 950, LY.SCREW2_Z), (0, 0, -90))
    A.hw('M12x40 hex bolt + nut + washers (hopper rim to stand, boot flange)', 16)
    A.hw('U-bolt M12 for OD 114 tube', 2)
    A.hw('M16x150 chemical / wedge anchor into concrete pad (stand and posts)', 16)
    A.info = dict(cx=cx, cy=cy, Lt1=Lt1, Lt2=Lt2)
    return A


# =============================================================== DR  rotary dryer
def build_DR():
    A = Asm('DR', 'Station 2b - Rotary sand dryer',
            desc='Dia 400 x 1400 rotary drum on four trunnion rollers, friction driven at ~5 rpm, slope adjustable 0-4 deg, '
                 '4.5 kW electric hot-air heater. Dries ~60 kg/h of sand from 5 % to below 0.5 % moisture.')
    TILT = 2.0
    FT = 860.0
    fr = table_frame('DR-1', 'Dryer frame', 1540, 700, FT, sec=(60, 60, 3), levels=[(FT - 30, 'FBLR'), (450, 'FBLR'), (150, 'FBLR')])
    xr = p_shs('DR-105', 'Dryer frame - jack cross rail', 580, 60, 60, 3, GREEN)
    fr.add(xr, (160, 60, FT - 30), (0, 0, 90))
    A.add(fr)
    th = math.radians(TILT)
    zc = FT + 30 + 1360 * math.sin(th)
    org = (120.0, 350.0, zc)

    def w(x, y, z):          # cradle-local -> machine-local
        return (org[0] + x * math.cos(th) + z * math.sin(th), org[1] + y, org[2] - x * math.sin(th) + z * math.cos(th))

    # ---------------- cradle weldment
    C = Asm('DR-200', 'Tilting cradle', kind='weldment',
            weld='Weld the two rails on the two end beams (square within 1 mm over the diagonals), add the four riser blocks. '
                 'The riser tops must be co-planar within 0.5 mm - skim them after welding or shim under the bearings.')
    rail = P('DR-201', 'Cradle rail', shs(1400, 80, 40, 3), 'S235JR', 'RHS 80x40x3', 'SAW', GREEN, dims={'Cut length': 1400, 'Section': '80 x 40 x 3 (laid flat)'})
    C.add(rail, (0, -140, 60)); C.add(rail, (0, 140, 60))
    endb = P('DR-202', 'Cradle end beam', shs(600, 80, 40, 3), 'S235JR', 'RHS 80x40x3', 'SAW', GREEN, dims={'Cut length': 600, 'Section': '80 x 40 x 3 (laid flat)'})
    C.add(endb, (40, -300, 20), (0, 0, 90)); C.add(endb, (1360, -300, 20), (0, 0, 90))
    ris = P('DR-203', 'Bearing riser block', shs(70, 80, 40, 3), 'S235JR', 'RHS 80x40x3', 'SAW', GREEN,
            dims={'Cut length': 70, 'Section': '80 x 40 x 3 (laid flat, tube axis along the drum)', 'Holes': '2 x dia 11 at 95 mm centres across the 80 mm width'},
            notes='One block under each UCP204 unit; the roller runs in the 80 mm gap between the two blocks. Drill 2 x dia 11 through the top wall. '
                  'Because the 95 mm bolt centres are wider than the 80 mm block, weld a 130 x 60 x 8 flat on top (or use M10 studs welded to the block sides).')
    RX = (430.0, 1230.0)
    for rx_ in RX:
        for sy in (-140, 140):
            C.add(ris, (rx_ - 110, sy, 100)); C.add(ris, (rx_ + 40, sy, 100))
    piv = P('DR-211', 'Cradle pivot block', box(80, 30, 30).cut(cq.Workplane('YZ').workplane(offset=-40).center(0, 15).circle(8.2).extrude(80)),
            'S235JR', 'Flat bar 30x30', 'MILL', GREEN, dims={'Size': '80 x 30 x 30', 'Cross hole': 'dia 16.4'},
            notes='Welded under the discharge-end beam. A dia 16 pin through the block and two lugs on the frame forms the tilt hinge.')
    C.add(piv, (1360, -250, -30)); C.add(piv, (1360, 250, -30))
    A.add(C, org, (0, TILT, 0))
    # moving parts placed in the cradle frame via a mechanism sub-assembly
    M = Asm('DR-250', 'Trunnion drive group')
    pb, hb = ucp(20)
    ZR = 120 + hb
    for rx_ in RX:
        for sy in (-140, 140):
            M.add(pb, (rx_ - 75, sy, 120)); M.add(pb, (rx_ + 75, sy, 120))
    rol = P('DR-204', 'Trunnion roller (plain)', tube(120, 50, 50), 'C45', 'Round bar dia 125', 'TURN', STEEL,
            dims={'OD': 120, 'Width': 50, 'Bore': '20 H7', 'Grub screws': '2 x M8 at 90 deg'},
            route=['Saw dia 125 C45 bar to 54 mm.', 'Lathe: face, drill and ream the bore to dia 20 H7, turn the OD to 120, chamfer 2 x 45 deg.',
                   'Reverse on a mandrel, face to 50 mm wide.', 'Drill and tap 2 x M8 radially at 90 deg for grub screws.',
                   'Optional: flame-harden the running surface or sleeve with 10 mm polyurethane for a quieter drive.'])
    frol = tube(120, 50, 42).union(tube(140, 60, 8).translate((-8, 0, 0))).union(tube(140, 60, 8).translate((42, 0, 0)))
    P('DR-207', 'Trunnion roller (flanged, thrust)', frol, 'C45', 'Round bar dia 145', 'TURN', STEEL,
      dims={'Tread OD': 120, 'Tread width': '42 (ring is 40)', 'Flange OD': 140, 'Flange width': 8, 'Bore': '20 H7'},
      notes='The two flanges straddle riding ring No. 2 and take the downhill thrust of the tilted drum.',
      route=['Saw dia 145 C45 bar to 62 mm.', 'Lathe: face, drill and ream dia 20 H7.', 'On a mandrel turn the two flanges to OD 140 x 8 wide and the 42 mm tread to OD 120 with R2 root radii.',
             'Drill and tap 2 x M8 grub screws through one flange hub.'])
    for sy in (-140, 140):
        M.add(rol, (RX[0] - 25, sy, ZR)); M.add('DR-207', (RX[1] - 21, sy, ZR))
    P('DR-205', 'Drive shaft dia 20', stepped([(20, 1120)], keys=[(10, 110, 6, 3.5, 20)]), 'C45', 'Round bar dia 20 h9 bright', 'TURN', STEEL,
      dims={'Length': 1120, 'Diameter': '20 h9 (bright bar as drawn)', 'Keyway': '6 x 3.5 deep x 110 at the motor end'})
    M.add('DR-205', (200, -140, ZR))
    M.add(p_rod('DR-206', 'Idler shaft dia 20', 20, 1000, STEEL, 'C45', notes='Bright drawn bar dia 20 h9, saw and chamfer only.'), (330, 140, ZR))
    M.add(gearmotor(0.37, 20, 22), (265, -140, ZR), (90, 0, 0))
    # ---------------- drum
    Dm = Asm('DR-300', 'Dryer drum', kind='weldment',
             weld='Roll and seam-weld the shell, check roundness within 2 mm. Shrink or tack-weld the two riding rings on (ring faces square to the axis within 1 mm) '
                  'and stitch-weld both sides. Stitch the 8 lifters inside at 45 deg spacing, weld the dam rings in each end.')
    Dm.add(p_shell('DR-301', 'Drum shell', 400, 3, 1400, STEEL, 'S235JR'))
    P('DR-302', 'Riding ring', tube(440, 20, 40), 'S355J2', 'Flat bar 40x20', 'ROLL', DARK,
      dims={'OD': 440, 'ID': 400, 'Width': 40, 'Developed length': f'{math.pi * 420:.0f}'},
      notes='Roll the flat bar the easy way to ID 400, butt-weld, grind flush. Ideally skim the OD and both faces in a lathe after welding to the shell.',
      flat=plate(round(math.pi * 420), 40, 20))
    Dm.add('DR-302', (230, 0, 0)); Dm.add('DR-302', (1030, 0, 0))
    lif = p_angle('DR-303', 'Lifter flight', 1200, 30, 30, 3, STEEL)
    for k in range(8):
        a = math.radians(k * 45)
        Dm.add(lif, (120, 194.5 * math.sin(a), -194.5 * math.cos(a)), (k * 45, 0, 0))
    Dm.add(p_disc('DR-304', 'Feed-end dam ring', 394, 3, bore=200, color=STEEL), (0, 0, 0), (0, 90, 0))
    Dm.add(p_disc('DR-305', 'Discharge-end dam ring', 394, 3, bore=320, color=STEEL), (1397, 0, 0), (0, 90, 0))
    ZD = ZR + 0.5 * math.sqrt((220 + 60) ** 2 * 4 - 280 ** 2)       # roller centres 280 apart, centre distance 280
    M.add(Dm, (180, 0, ZD))
    cowl = tube(540, 1.5, 700).cut(cq.Workplane('XY').box(720, 560, 300, centered=(False, True, False)).translate((-10, 0, -300)))
    P('DR-401', 'Insulated drum cowl', cowl, 'DC01 galv.', 'Sheet 1.5 mm', 'ROLL', ORANGE,
      dims={'Inside radius': 268.5, 'Length': 700, 'Flat blank': '846 x 700'},
      notes='Roll to a half cylinder. Line the inside with 25 mm foil-faced mineral wool held by weld pins. Keeps the heat in and hands off the hot drum.',
      flat=plate(846, 700, 1.5))
    M.add('DR-401', (480, 0, ZD))
    stay = P('DR-402', 'Cowl stay', cq.Workplane('XZ').polyline([(0, 0), (95, 0), (95, 5), (5, 5), (5, ZD - 80), (0, ZD - 80)]).close().extrude(30),
             'S235JR', 'Flat bar 30x5', 'BEND', ORANGE, dims={'Developed length': round(ZD - 80 + 90), 'Section': '30 x 5', 'Bend': '90 deg, 95 mm foot'},
             flat=plate(round(ZD - 80 + 90), 30, 5))
    for sx in (500, 1130):
        M.add(stay, (sx, 268, 80), (0, 0, 180)); M.add(stay, (sx - 30, -268, 80))
    A.add(M, org, (0, TILT, 0))
    A.zd_feed = w(180, 0, ZD)[2]; A.zd_dis = w(1580, 0, ZD)[2]
    # ---------------- feed hood (fixed to the frame)
    zf = A.zd_feed
    FH = plate_box('DR-5', 'Feed hood', 300, 460, 460, 2, color=LGREY,
                   cuts={'R': dict(holes=[(0, 0, 412)]), 'T': dict(rects=[(0, 0, 164, 164)]), 'F': dict(rects=[(0, 0, 180, 180)])})
    A.add(FH, (170, 350, zf - 230))
    col = P('DR-510', 'Feed inlet collar', cq.Workplane('XY').rect(164, 164).rect(160, 160).extrude(150), 'DC01 galv.', 'Sheet 2 mm', 'BEND', LGREY,
            dims={'Inside': '160 x 160', 'Height': 150}, flat=plate(648, 150, 2),
            notes='Fold from one strip; the transfer-screw spout hangs 40 mm inside it. Fit a canvas dust sock between the two.')
    A.add(col, (170, 350, zf + 228))
    defl = p_plate('DR-511', 'Feed deflector plate', 300, 200, 2, color=LGREY,
                   notes='Welded inside the hood at 50 deg so the sand slides into the drum mouth.')
    A.add(defl, (200, 350, zf - 40), (0, 50, 0))
    fpost = p_shs('DR-512', 'Feed hood post', round(zf - 230 - FT), 40, 40, 3, GREEN)
    A.add(fpost, (60, 200, FT), (0, -90, 0)); A.add(fpost, (60, 500, FT), (0, -90, 0))
    A.add(buy('DR-601', 'Duct air heater 4.5 kW', box(200, 250, 200), 'Finned electric duct heater 4.5 kW, 400 V 3-ph, 200 x 200 mm duct, '
              'with over-temperature cut-out and air-flow interlock; outlet air 150-200 C', RED, 9), (170, 350 + 230 + 125, zf - 100))
    blower = cq.Workplane('XZ').circle(120).extrude(110).translate((0, 55, 0)).union(cq.Workplane('XZ').circle(60).extrude(150).translate((0, 205, 0)))
    A.add(buy('DR-602', 'Centrifugal blower 0.18 kW', blower, 'Centrifugal blower 0.18 kW, approx. 400 m3/h at 300 Pa, 200 x 200 outlet flange', BLUE, 8), (170, 350 + 480 + 55, zf))
    # ---------------- discharge hood
    zd = A.zd_dis
    DH = plate_box('DR-7', 'Discharge hood', 230, 520, 560, 2, omit='B', color=LGREY,
                   cuts={'L': dict(holes=[(0, zd - 1290, 424)]), 'T': dict(holes=[(0, 0, 125)])})
    A.add(DH, (1785, 350, 1010))
    arm = p_angle('DR-711', 'Discharge hood support arm', 400, 40, 40, 4, GREEN)
    A.add(arm, (1510, 350 - 262, 1006), (90, 0, 0)); A.add(arm, (1510, 350 + 262, 1006), (180, 0, 0))
    dpost = p_shs('DR-712', 'Discharge hood post', round(1002 - FT), 40, 40, 3, GREEN)
    A.add(dpost, (1520, 350 - 290, FT), (0, -90, 0)); A.add(dpost, (1520, 350 + 290, FT), (0, -90, 0))
    A.add(buy('DR-801', 'Cradle jack screw M20', rod(20, 120).rotate((0, 0, 0), (0, 1, 0), -90), 'M20 x 120 hex set screw 8.8 with 2 nuts (slope adjustment and lock)', DARK, 0.4),
          (160, 100, FT - 20))
    A.add('DR-801', (160, 600, FT - 20))
    A.add(control_box(), (1300, 776, 950))
    A.add(p_shs('DR-901', 'Control post', 400, 40, 40, 3, GREEN), (1300, 680, FT), (0, -90, 0))
    A.hw('M10x60 hex bolt + nut (UCP204 to risers)', 16)
    A.hw('Pin dia 16 x 110 with split pins (cradle pivot)', 2)
    A.hw('Parallel key 6x6x100', 1)
    A.hw('M8x12 grub screw (rollers)', 8)
    A.hw('Mineral wool 25 mm foil faced, 0.6 m2 (cowl lining)', 1)
    A.hw('PT100 air temperature sensor + PID controller (heater)', 1)
    A.hw('M12x100 floor anchor', 8)
    return A


# =============================================================== VS  vibrating screen
def build_VS():
    A = Asm('VS', 'Station 2c - Vibrating screen',
            desc='430 x 840 single-deck screen, 2 mm aperture, 8 deg slope, 0.12 kW vibrator. Passes dry sand to a tote, rejects stones and oversize.')
    fr = table_frame('VS-1', 'Screen frame', 600, 1000, 700, sec=(50, 50, 3), levels=[(675, 'FBLR'), (150, 'BLR')])
    A.add(fr)
    TL = 8.0
    t8 = math.radians(TL)
    zc = 796 - 380 * math.sin(t8) - 10 * math.cos(t8)
    zl_front = (796 - zc + 380 * math.sin(t8)) / math.cos(t8)
    seat = p_plate('VS-201', 'Spring seat', 80, 80, 6, holes=[(0, 0, 9)], color=GREEN, notes='Weld on the frame top rail; the M8 stud centres the spring.')
    spring = buy('VS-202', 'Compression spring dia 50 x 90', tube(50, 6, 90).rotate((0, 0, 0), (0, 1, 0), -90),
                 'Compression spring OD 50, wire 6, free length 90, rate approx. 15 N/mm, ground ends', YELLOW, 0.3)
    for sx in (25, 575):
        for yy in (500 - 380 * math.cos(t8), 500 + 380 * math.cos(t8)):
            A.add(seat, (sx, yy, 700)); A.add(spring, (sx, yy, 706))
    B = Asm('VS-300', 'Screen box', kind='weldment',
            weld='Tack side plates to the back plate and the two cross tubes on a flat table, check square, weld fully. '
                 'Add the four spring lugs LEVEL with the box tilted 8 deg on packers. All welds continuous - vibration finds every weak joint.')
    side = p_plate('VS-301', 'Screen box side plate', 840, 150, 4, color=BLUE)
    B.add(side, (-220, 0, 75), (90, 0, 90)); B.add(side, (216, 0, 75), (90, 0, 90))
    B.add(p_plate('VS-302', 'Screen box back plate', 432, 150, 4, color=BLUE), (0, -416, 75), (90, 0, 0))
    ct = p_tube('VS-303', 'Screen box cross tube', 33.7, 3, 432, BLUE)
    B.add(ct, (-216, -300, 20)); B.add(ct, (-216, 300, 20))
    df = p_flat('VS-304', 'Deck support flat', 836, 25, 5, BLUE)
    B.add(df, (-203, -416, 95.5), (0, 0, 90)); B.add(df, (203, -416, 95.5), (0, 0, 90))
    B.add(p_plate('VS-307', 'Vibrator bridge plate', 440, 200, 8, holes=[(sx * 60, sy * 45, 11) for sx in (-1, 1) for sy in (-1, 1)], color=BLUE,
                  notes='Welded across the top of the side plates at the discharge end; hole pattern to suit the vibrator feet (check the purchased unit).'), (0, 310, 150))
    lug = p_angle('VS-309', 'Spring lug', 80, 60, 60, 6, BLUE)
    B.add(lug, (220, -340, 10), (0, 0, -90)); B.add(lug, (-220, -420, 10), (0, 0, 90))
    B.add(lug, (220, 420, zl_front), (0, 0, -90)); B.add(lug, (-220, 340, zl_front), (0, 0, 90))
    A.add(B, (300, 500, zc), (-TL, 0, 0))
    U = Asm('VS-350', 'Screen deck and attachments')
    U.add(P('VS-305', 'Screen mesh panel 2 mm aperture', plate(430, 836, 2), 'Woven wire 304', 'Woven wire cloth, 2.0 mm aperture, 0.9 mm wire', 'MESH', LGREY,
            dims={'Length': 836, 'Width': 430, 'Aperture': 2.0, 'Wire': 0.9}, notes='Cut with a 4 mm allowance, fold the long edges 10 mm over for clamping. Keep a spare; this is a wear part.'),
          (0, 2, 98))
    cs = p_flat('VS-306', 'Mesh clamp strip', 836, 25, 4, BLUE, notes='6 x dia 7 holes at 150 pitch; M6 screws into the deck support flats.')
    U.add(cs, (-203, -416, 102), (0, 0, 90)); U.add(cs, (203, -416, 102), (0, 0, 90))
    U.add(buy('VS-308', 'Vibrator motor 0.12 kW', box(200, 150, 130), 'External electric vibrator motor 0.12 kW, 2-pole (3000 rpm), centrifugal force adjustable to approx. 1.5 kN', DARK, 6),
          (0, 310, 158))
    pan = hopper('VS-31', 'Undersize pan', (430, 700), (150, 150), 260, t=2, color=BLUE, mat='DC01 galv.')
    U.add(pan, (0, -40, -265))
    ch = P('VS-321', 'Oversize chute', cq.Workplane('XZ').polyline([(-217, 60), (-217, 0), (217, 0), (217, 60), (215, 60), (215, 2), (-215, 2), (-215, 60)]).close().extrude(-135),
           'DC01 galv.', 'Sheet 2 mm', 'BEND', BLUE, dims={'Width': 434, 'Length': 135, 'Side height': 60}, flat=plate(550, 135, 2))
    U.add(ch, (0, 420, 62), (-4, 0, 0))
    A.add(U, (300, 500, zc), (-TL, 0, 0))
    A.add(buy('VS-501', 'Stones bucket 20 L', bin_shape(300, 300, 300, 3), 'Steel bucket 20 L for stones and oversize', DARK, 1.5), (300, 1090, 0))
    A.add(tote(), (300, 440, 0), (0, 0, 90))
    # dust hood
    Hd = hopper('VS-4', 'Screen dust hood', (440, 400), (150, 150), 220, t=1.5, color=WHITE, mat='DC01 galv.')
    A.add(Hd, (300, 600, 1240), (180, 0, 0))
    hp = p_shs('VS-411', 'Dust hood post', 320, 30, 30, 2, GREEN)
    for sx in (25, 575):
        for yy in (410, 790):
            A.add(hp, (sx, yy, 700), (0, -90, 0))
    hb = p_angle('VS-412', 'Dust hood bearer', 600, 30, 30, 3, GREEN)
    A.add(hb, (0, 395, 1020), (0, 0, 0)); A.add(hb, (600, 805, 1020), (0, 0, 180))
    A.hw('M6x16 pan-head screw (mesh clamp strips)', 12)
    A.hw('M10x35 bolt + nyloc + spring washer (vibrator)', 4)
    A.hw('M8x40 stud (spring location)', 8)
    A.hw('M12x100 floor anchor', 8)
    A.deck = dict(zc=zc)
    return A


# =============================================================== DC  dust collector
def build_DC():
    A = Asm('DC', 'Station 2d - Cartridge dust collector',
            desc='0.75 kW fan, ~1000 m3/h, one dia 325 x 600 cartridge (approx. 10 m2). Extracts the screen hood and the dryer discharge hood.')
    A.add(table_frame('DC-1', 'Dust collector stand', 450, 450, 497, sec=(30, 30, 2.5), levels=[(482, 'FBLR'), (120, 'BLR')]))
    body = plate_box('DC-2', 'Dust collector body', 450, 450, 1000, 2, omit='B', color=WHITE, mat='DC01 galv.',
                     cuts={'T': dict(holes=[(0, 0, 200)]), 'L': dict(holes=[(0, -250, 125)]), 'F': dict(rects=[(0, 40, 340, 620)])})
    A.add(body, (225, 225, 500))
    door = p_plate('DC-210', 'Service door', 400, 680, 2, holes=[(sx * 185, sy * 108.3 * k, 7) for sx in (-1, 1) for sy in (-1, 1) for k in (1, 3)],
                   color=WHITE, mat='DC01 galv.', notes='Bolted with 8 x M6 wing nuts over a 20 x 5 EPDM gasket.')
    A.add(door, (225, 452, 1040), (90, 0, 0))
    hp = hopper('DC-3', 'Dust hopper', (380, 380), (150, 150), 218, t=2, color=WHITE, mat='DC01 galv.')
    A.add(hp, (225, 225, 279))
    A.add(p_plate('DC-304', 'Hopper flange ring', 450, 450, 3, rects=[(0, 0, 380, 380)], color=WHITE, mat='DC01 galv.',
                  notes='Sits on the stand top rails; the body stands on it and the hopper is welded underneath.'), (225, 225, 497))
    A.add(buy('DC-401', 'Filter cartridge dia 325 x 600', tube(325, 30, 600).rotate((0, 0, 0), (0, 1, 0), -90), 'Pleated polyester cartridge, OD 325 x 600, approx. 10 m2, '
              'flange top, M class (EN 60335-2-69) or better', CREAM, 4), (225, 225, 880))
    fan = cq.Workplane('XY').circle(210).extrude(160).union(cq.Workplane('XY').workplane(offset=160).circle(90).extrude(240))
    fan = fan.union(cq.Workplane('XY').box(200, 250, 150, centered=(False, True, False)).translate((120, 0, 5)))
    A.add(buy('DC-402', 'Centrifugal fan 0.75 kW', fan, 'Radial fan 0.75 kW 2-pole, approx. 1000 m3/h at 1500 Pa, vertical shaft, inlet dia 200', BLUE, 22), (225, 225, 1500))
    A.add(buy('DC-403', 'Dust bucket 30 L', bin_shape(300, 300, 250, 3), 'Steel dust bucket 30 L with quick-release band clamp', DARK, 2), (225, 225, 0))
    A.hw('M6 wing nut + stud (door)', 8)
    A.hw('EPDM gasket 20x5, 2.3 m', 1)
    A.hw('Flexible PU ducting dia 125, 4 m, with 4 hose clamps and one Y-branch 125/125/125', 1)
    return A
