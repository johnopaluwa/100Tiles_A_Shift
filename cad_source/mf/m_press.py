"""TL tooling + product, HP hydraulic press, RC roller tables, CR cooling rack, TR trim station, TT tile test rig."""
import math
import cadquery as cq
from .core import *
from . import layout as LY

# ------------------------------------------------------------------ tile profile
TW, TLEN, TT_ = 330.0, 420.0, 8.0     # tile width, length, wall thickness
HR = 32.0                             # roll height (centre line)
HI = 75.0                             # insert height
ZREF = 15.0 + HR + TT_ / 2            # mould z of the tile reference plane (15 mm of metal under the roll crowns)
PB = HI + 3.0                         # underside of the punch base when closed
PT = PB + 35.0                        # top of the punch base when closed
BT = LY.TRANSFER_Z - 30.0             # bed top
STROKE = 300.0


def _c(u):
    if u < 30:
        return 7 * (1 + math.cos(math.pi * u / 30))
    if 80 <= u <= 180:
        return HR / 2 * (1 - math.cos(2 * math.pi * (u - 80) / 100))
    if 235 <= u <= 335:
        return HR / 2 * (1 - math.cos(2 * math.pi * (u - 235) / 100))
    return 0.0


def _curves():
    top, bot = [], []
    u = -12.0
    while u <= 342.01:
        dz = (_c(u + 0.05) - _c(u - 0.05)) / 0.1
        n = math.hypot(1, dz)
        nx, nz = -dz / n, 1 / n
        top.append((u + nx * TT_ / 2, _c(u) + nz * TT_ / 2))
        bot.append((u - nx * TT_ / 2, _c(u) - nz * TT_ / 2))
        u += 3.0
    return top, bot


def tile_solid():
    top, bot = _curves()
    w = (cq.Workplane('XZ').moveTo(*top[0]).spline(top[1:], includeCurrent=True).lineTo(*bot[-1])
         .spline(bot[::-1][1:], includeCurrent=True).close().extrude(-TLEN))
    w = w.intersect(cq.Workplane('XY').box(TW, TLEN, 200, centered=(False, False, True)))
    for uc in (55.0, 207.0):
        w = w.union(cq.Workplane('XY').box(30, 20, 13, centered=(True, False, False)).translate((uc, TLEN - 35, -TT_ / 2 - 12)))
    return w


def _section(pts, zcap, length):
    """solid between a profile curve (list of (u,z) in tile coords, flipped into mould coords) and the plane z=zcap, extruded along mould X"""
    m = [(u - TW / 2, ZREF - z) for u, z in pts]
    w = cq.Workplane('YZ').moveTo(*m[0]).spline(m[1:], includeCurrent=True).lineTo(m[-1][0], zcap).lineTo(m[0][0], zcap).close()
    return w.extrude(length).translate((-length / 2, 0, 0))


def insert_solid():
    top, _ = _curves()
    pocket = _section(top, HI + 5, TLEN + 1.0).intersect(cq.Workplane('XY').box(TLEN + 1.0, TW + 1.0, 300))
    w = cq.Workplane('XY').box(470, 380, HI, centered=(True, True, False)).cut(pocket)
    for yc in (-110.0, 42.0):
        w = w.cut(cq.Workplane('XY').box(380, 40, 33, centered=(True, True, False)).translate((0, yc, 0)))
    for sx in (-1, 1):
        w = w.cut(cq.Workplane('XY').box(12, 120, 14, centered=(True, True, False)).translate((sx * 229, 0, 42)))
    return w


def punch_solid():
    _, bot = _curves()
    boss = _section(bot, PB, TLEN + 0.2).intersect(cq.Workplane('XY').box(TLEN + 0.2, TW + 0.2, 300))
    w = cq.Workplane('XY').box(470, 380, PT - PB, centered=(True, True, False)).translate((0, 0, PB)).union(boss)
    for sy in (-1, 1):
        w = w.union(cq.Workplane('XY').box(470, 20, 3, centered=(True, True, False)).translate((0, sy * 180, HI)))
    for uc in (55.0, 207.0):
        w = w.cut(cq.Workplane('XY').box(20.6, 30.6, 13, centered=(False, True, False)).translate((TLEN / 2 - 35.3, uc - TW / 2, ZREF + TT_ / 2 - 0.5)))
    return w


def register_tooling():
    t = tile_solid()
    kg = t.val().Volume() * 1.72e-6
    P('TL-001', 'Roof tile, double-roman, plastic-sand', t, 'Plastic-sand composite', '70 % dry sand + 30 % HDPE by weight', 'MOULD', TILE,
      dims={'Length': TLEN, 'Cover width': TW, 'Wall thickness': TT_, 'Roll height': HR + TT_, 'Hanging nibs': '2 x 30 x 20 x 12',
            'Calculated mass': f'{kg:.2f} kg at 1.72 g/cm3',
            'Profile, centre line (x across the width)': 'x 0-30: side rim falling 14 to 0 (half cosine); 30-80 flat pan; 80-180 roll, 32 high (full cosine); '
                                                         '180-235 flat pan; 235-330 second roll, 32 high, cut off at x=330 (the overlap edge)',
            'Wall': '8 mm measured normal to the centre line, constant',
            'Nib positions': 'under the pans at x = 55 and 207, 15-35 mm from the head end'},
      notes='The product. Compression-moulded upside down: weather face in the aluminium cavity insert, underside and nibs formed by the punch.')
    P('TL-101', 'Cavity insert (lower mould half)', insert_solid(), 'Al A356-T6', 'Sand casting, or 5083 tooling plate 80 mm', 'CAST', ALU,
      dims={'Block': '470 x 380 x 75', 'Pocket plan': f'{TLEN + 1:g} x {TW + 1:g} (tile + 0.5 mm per side)', 'Min. floor under roll crowns': 15,
            'Shut-off depth above tile': f'{HI - (ZREF + TT_ / 2):.0f}', 'Lightening pockets (underside)': '2 x 380 x 40 x 33', 'Finger grooves': '2 x 120 x 14 x 12'},
      notes='10 off: two are in the press while eight cool in the rack. Machine the cavity directly from the STEP surface. '
            'Hard-anodise 50 micron (or electroless nickel) for abrasion resistance; polish the cavity to Ra 0.8.')
    P('TL-102', 'Punch (upper mould half)', punch_solid(), 'S355J2', 'Plate 100 mm', 'CNC3D', STEEL,
      dims={'Base': '470 x 380 x 35', 'Boss plan': f'{TLEN + 0.2:g} x {TW + 0.2:g} (0.4 mm shear gap per side to the pocket)',
            'Kiss-off lands': '2 x 470 x 20 x 3 high', 'Nib pockets': '2 x 30.6 x 20.6 x 12.5 deep, 5 deg draft'},
      notes='2 off, bolted under the upper bolster. The two 3 mm lands close on the insert top face and fix the tile thickness; flash escapes at the ends. '
            'Drill and tap 6 x M12 x 25 deep in the back face (pattern 400 x 150) for the bolster screws.')
    return kg


def build_carrier():
    C = Asm('TL-110', 'Mould carrier', kind='weldment',
            weld='Stitch-weld the rim bars to the base plate (30 every 100) with the two inserts in place as a jig and 0.75 mm shims all round, '
                 'so each insert drops in freely but cannot shift. Skim the underside flat after welding if it has pulled more than 0.5 mm.')
    C.add(p_plate('TL-111', 'Carrier base plate', 540, 840, 10, holes=[(-258, 0, 22), (258, 0, 22)], color=DARK, mat='S355J2',
                  notes='2 x dia 22 pull holes for the hook tool.'))
    lb = p_flat('TL-112', 'Carrier long rim bar', 822, 20, 15, DARK)
    C.add(lb, (-245.75, -411, 17.5), (0, 0, 90)); C.add(lb, (245.75, -411, 17.5), (0, 0, 90))
    cb = p_flat('TL-113', 'Carrier cross rim bar', 471, 20, 15, DARK)
    for y in (-401, 0, 401):
        C.add(cb, (-235.5, y, 17.5))
    return C


# =============================================================== HP
def build_HP():
    A = Asm('HP', 'Station 5 - Two-cavity hydraulic press, 1000 kN',
            desc='Four-column down-stroking press. Bore 250 cylinder at 210 bar = 1030 kN (3.7 MPa on two tiles). 300 mm stroke, 4 kW power pack on the crown. '
                 'Two tiles per cycle; the mould carrier rolls in from the charge table and out to the cooling side.')
    CX, CY = 500.0, 580.0
    COLS = [(sx * 335, sy * 480) for sx in (-1, 1) for sy in (-1, 1)]
    ch = [(x, y, 74) for x, y in COLS]
    FT = BT - 290
    fr = table_frame('HP-1', 'Press base frame', 1000, 1160, FT, sec=(100, 100, 5), levels=[(FT - 50, 'LR'), (120, 'FB')], foot_hole=18)
    br = p_shs('HP-105', 'Press base - return conveyor bearer', 960, 60, 60, 4, GREEN)
    fr.add(br, (50, 100, 270), (0, 0, 90)); fr.add(br, (950, 100, 270), (0, 0, 90))
    A.add(fr)
    WELD = ('Tack the webs and stiffeners to the 30 mm load plate first, then the sleeves, then close with the second plate. Weld in a balanced '
            'back-step sequence (a6 fillets, both sides of every web). Stress-relieve at 580-620 C for 2 h, then machine: both outer faces parallel within 0.1 mm '
            'and the four column bores dia 72 H8 line-bored in ONE setting together with the other crosshead so the column centres match within 0.1 mm.')
    web = p_plate('HP-203', 'Crosshead main web', 1160, 240, 16, color=STEEL, mat='S355J2')
    stf = p_plate('HP-204', 'Crosshead stiffener, outer bay', 208, 240, 12, color=STEEL, mat='S355J2')
    stf2 = p_plate('HP-205', 'Crosshead stiffener, inner bay', 184, 240, 12, color=STEEL, mat='S355J2')
    slv = P('HP-206', 'Column sleeve', tube(121, 23.5, 240), 'S355J2', 'Hollow bar OD 121 x ID 71', 'TURN', STEEL,
            dims={'OD': 121, 'ID': '74 (finish-bored to 72 H8 after welding)', 'Length': 240})
    # ---- bed
    Bd = Asm('HP-200', 'Press bed (lower crosshead)', kind='weldment', weld=WELD)
    Bd.add(p_plate('HP-202', 'Bed bottom plate', 880, 1160, 20, holes=ch, color=STEEL, mat='S355J2'))
    for xc in (-424, -200, 0, 200, 424):
        Bd.add(web, (xc - 8, 0, 140), (90, 0, 90))
    for y in (-300, 0, 300):
        for xc in (-312, 312):
            Bd.add(stf, (xc, y + 6, 140), (90, 0, 0))
        for xc in (-100, 100):
            Bd.add(stf2, (xc, y + 6, 140), (90, 0, 0))
    for x, y in COLS:
        Bd.add(slv, (x, y, 20), (0, -90, 0))
    Bd.add(p_plate('HP-201', 'Bed top plate', 880, 1160, 30, holes=ch + [(sx * 250, sy * 400, 14) for sx in (-1, 1) for sy in (-1, 0, 1)], color=STEEL, mat='S355J2',
                   notes='6 x dia 14 are tapping-drill positions for M16 (lower bolster screws) - drill and tap after machining the face.'), (0, 0, 260))
    A.add(Bd, (CX, CY, FT))
    # ---- crown
    ZP = BT + 30 + 10 + PT + 30 + STROKE        # platen underside, open
    ZC = ZP + 200 + 40 + 12 + 45                # crown underside
    Cr = Asm('HP-300', 'Press crown (upper crosshead)', kind='weldment', weld=WELD)
    Cr.add(p_plate('HP-301', 'Crown bottom plate', 880, 1160, 30, holes=ch + [(0, 0, 310)] + pcd(8, 380, 22, 22.5), color=GREEN, mat='S355J2',
                   notes='Load face: the cylinder head flange bears on the underside. 8 x dia 22 on PCD 380 for M20 flange bolts.'))
    for xc in (-424, -200, 200, 424):
        Cr.add(web, (xc - 8, 0, 150), (90, 0, 90))
    for y in (-300, 0, 300):
        for xc in (-312, 312):
            Cr.add(stf, (xc, y + 6, 150), (90, 0, 0))
    cst = p_plate('HP-303', 'Crown centre stiffener', 384, 240, 12, color=GREEN, mat='S355J2')
    Cr.add(cst, (0, 236, 150), (90, 0, 0)); Cr.add(cst, (0, -224, 150), (90, 0, 0))
    Cr.add(P('HP-304', 'Cylinder sleeve ring', tube(355, 16, 240), 'S355J2', 'Plate 16 mm', 'ROLL', GREEN,
             dims={'OD': 355, 'Wall': 16, 'Height': 240, 'Developed blank': f'{math.pi * 339:.0f} x 240'}, flat=plate(round(math.pi * 339), 240, 16)), (0, 0, 30), (0, -90, 0))
    for x, y in COLS:
        Cr.add(slv, (x, y, 30), (0, -90, 0))
    Cr.add(p_plate('HP-302', 'Crown top plate', 880, 1160, 20, holes=ch + [(0, 0, 310)], color=GREEN, mat='S355J2'), (0, 0, 270))
    A.add(Cr, (CX, CY, ZC))
    # ---- columns and nuts
    P('HP-401', 'Press column dia 80', stepped([(72, 365), (80, ZC - BT), (72, 365)]), '42CrMo4', 'Round bar dia 80, hard-chromed', 'TURN', LGREY,
      dims={'Overall length': ZC - BT + 730, 'Body': f'dia 80 f7 x {ZC - BT:g} (chromed, ground)', 'Ends': 'dia 72 x 365, threaded M72x4 for 80 mm',
            'Shoulder length tolerance': '+/-0.05 mm, all four columns matched'},
      route=['Saw 42CrMo4 (QT, hard-chromed and ground dia 80 f7 bar) to length + 6 mm.',
             'Lathe with steady rest: face and centre both ends.',
             'Between centres: turn both ends to dia 72 g6 for 365 mm, leaving a sharp square shoulder with a 1 x 45 deg relief. '
             'The distance between the two shoulders is the press daylight datum: hold it within +/-0.05 mm and make all four columns in one batch.',
             'Screw-cut M72x4 for 80 mm at each end; fit a nut as gauge.',
             'Protect the chromed body with sleeve during all handling.'])
    nut = P('HP-402', 'Column nut M72x4', cq.Workplane('XY').polygon(6, 105 / math.cos(math.radians(30))).circle(36.05).extrude(58), 'C45', 'Hexagon bar 105 A/F', 'TURN', DARK,
            dims={'Across flats': 105, 'Height': 58, 'Thread': 'M72x4'}, notes='Can be bought as DIN 934 M72x4 class 8. Tighten each to 2000 N.m in a cross pattern, or hydraulically pre-tension.')
    for x, y in COLS:
        A.add('HP-401', (CX + x, CY + y, BT - 365), (0, -90, 0))
        A.add(nut, (CX + x, CY + y, FT - 58)); A.add(nut, (CX + x, CY + y, ZC + 290))
    # ---- moving platen
    Pl = Asm('HP-500', 'Moving platen', kind='weldment',
             weld='Same sequence and stress relief as the crossheads. After machining both faces parallel, bore the four bush housings dia 100 H7 '
                  'in the same setting as the bed and crown column bores. Press in the bronze bushes and ream to dia 80 H8.')
    bh = [(x, y, 131) for x, y in COLS]
    Pl.add(p_plate('HP-501', 'Platen bottom plate', 860, 1140, 30, holes=bh + [(sx * 200, sy * 330, 14) for sx in (-1, 1) for sy in (-1, 0, 1)], color=STEEL, mat='S355J2',
                   notes='6 x dia 14 tapping positions for M16 upper-bolster screws.'))
    pw = p_plate('HP-503', 'Platen web', 1108, 150, 16, color=STEEL, mat='S355J2')
    for xc in (-230, -70, 70, 230):
        Pl.add(pw, (xc - 8, 0, 105), (90, 0, 90))
    pe = p_plate('HP-504', 'Platen end web', 860, 150, 16, color=STEEL, mat='S355J2')
    Pl.add(pe, (0, 570, 105), (90, 0, 0)); Pl.add(pe, (0, -554, 105), (90, 0, 0))
    hsg = P('HP-505', 'Bush housing', tube(130, 15, 200), 'S355J2', 'Hollow bar OD 130 x ID 95', 'TURN', STEEL, dims={'OD': 130, 'ID': '100 H7 (finish-bored after welding)', 'Length': 200})
    bush = P('HP-506', 'Column guide bush', tube(100, 9.9, 200), 'Bronze CuSn12', 'Cast bronze tube 105/75', 'TURN', BRONZE,
             dims={'OD': '100 r6', 'ID': '80 H8 (ream after pressing in)', 'Length': 200, 'Grease grooves': 'figure-8, 3 wide x 1.5 deep'})
    for x, y in COLS:
        Pl.add(hsg, (x, y, 0), (0, -90, 0)); Pl.add(bush, (x, y, 0), (0, -90, 0))
    Pl.add(p_plate('HP-502', 'Platen top plate', 860, 1140, 20, holes=bh + pcd(6, 240, 22), color=STEEL, mat='S355J2'), (0, 0, 180))
    A.add(Pl, (CX, CY, ZP))
    A.add(p_disc('HP-602', 'Rod flange', 280, 40, bore=100, holes=pcd(6, 240, 22), color=DARK, mat='C45', proc='TURN',
                 notes='Bore threaded to suit the purchased cylinder rod end (typically M100x3). 6 x M20 into the platen top plate.'), (CX, CY, ZP + 200))
    cyl = cq.Workplane('XY').box(420, 420, 45, centered=(True, True, False)).translate((0, 0, -45))
    cyl = cyl.union(cq.Workplane('XY').circle(149).extrude(650)).union(cq.Workplane('XY').workplane(offset=-57).circle(90).extrude(12))
    cyl = cyl.union(cq.Workplane('XY').workplane(offset=650).circle(120).extrude(30))
    A.add(buy('HP-601', 'Hydraulic cylinder 250/180 x 300', cyl, 'Double-acting cylinder, bore 250, rod 180, stroke 300, 250 bar rated, head-flange mount (ISO 6022 MF1 style, '
              '420 x 420 flange, 8 x M20 on PCD 380), rod-end male thread, cushioned', BLUE, 430), (CX, CY, ZC))
    hpu = cq.Workplane('XY').box(500, 330, 300, centered=(True, True, False)).union(cq.Workplane('XY').workplane(offset=300).center(-100, 0).circle(100).extrude(280))
    hpu = hpu.union(cq.Workplane('XY').box(160, 160, 140, centered=(True, True, False)).translate((150, 0, 300)))
    A.add(buy('HP-610', 'Hydraulic power unit 4 kW', hpu, 'Power pack: 4 kW 400 V motor, hi-lo double pump (approx. 30 l/min at 40 bar, 5 l/min at 210 bar), 60 l tank, '
              'relief valve set 210 bar, 4/3 solenoid valve with pilot check (load holding), pressure switch, gauge 0-400 bar, return filter, oil cooler optional', BLUE, 95),
          (CX, CY - 380, ZC + 290))
    # ---- bolsters and die lifters
    lb = plate(600, 900, 30, holes=[(sx * 250, sy * 400, 18) for sx in (-1, 1) for sy in (-1, 0, 1)])
    for sy in (-1, 1):
        lb = lb.cut(cq.Workplane('XY').box(600, 42, 24, centered=(True, True, False)).translate((0, sy * 300, 6)))
    P('HP-701', 'Lower bolster with lifter grooves', lb, 'S355J2', 'Plate 30 mm', 'MILL', STEEL,
      dims={'Size': '600 x 900 x 30', 'Lifter grooves': '2 x 42 wide x 24 deep, full length, at y = +/-300', 'Fixing': '6 x dia 18 c/bored for M16 cap screws'},
      notes='Top face ground or fly-cut flat within 0.05 mm - the mould carrier seats on it under full press load.')
    A.add('HP-701', (CX, CY, BT))
    lf = buy('HP-702', 'Spring die-lifter bar 40x24x600 with balls', box(600, 40, 27), 'Spring-loaded ball die lifter for 42 mm groove, 600 long, lift 3 mm, '
             'approx. 100 kg per bar; retracts flush under press load', LGREY, 5)
    A.add(lf, (CX, CY - 300, BT + 6)); A.add(lf, (CX, CY + 300, BT + 6))
    A.add(P('HP-703', 'Carrier end stop (flip-down)', box(30, 200, 45), 'S355J2', 'Flat bar 45x30', 'MILL', YELLOW, dims={'Size': '30 x 200 x 45', 'Pivot hole': 'dia 12.5, 12 from the bottom edge'},
            notes='Pivots on an M12 shoulder bolt on the outfeed edge of the lower bolster. Up = positions the carrier under the punches; flipped down = carrier rolls out.'),
          (CX + 285, CY, BT + 30))
    A.add(p_plate('HP-711', 'Upper bolster', 540, 840, 30, holes=[(sx * 200, sy * 330, 18) for sx in (-1, 1) for sy in (-1, 0, 1)]
                  + [(sx * 200, yc + sy * 75, 14) for sx in (-1, 0, 1) for yc in (-200, 200) for sy in (-1, 1)], color=STEEL, mat='S355J2', proc='MILL',
                  notes='6 x dia 18 (c/bored) to the platen, 12 x dia 14 (c/bored from above) for the M12 punch screws. Both faces parallel within 0.05 mm.'), (CX, CY, ZP - 30))
    A.add('TL-102', (CX, CY - 200, ZP - 30 - PT)); A.add('TL-102', (CX, CY + 200, ZP - 30 - PT))
    # ---- mould set in the press (carrier + 2 inserts)
    A.add(ASMS['TL-110'], (CX, CY, BT + 30))
    A.add('TL-101', (CX, CY - 200, BT + 40)); A.add('TL-101', (CX, CY + 200, BT + 40))
    # ---- safety
    lc = buy('HP-640', 'Safety light curtain, 500 mm, type 4', box(40, 40, 520), 'Type 4 safety light curtain pair (IEC 61496), 500 mm protective height, 30 mm resolution, '
             'with safety relay to stop the down-stroke (ISO 13855 safety distance to be calculated)', YELLOW, 1.5)
    A.add(lc, (60, 1190, BT + 60)); A.add(lc, (940, 1190, BT + 60))
    A.add(P('HP-650', 'Rear fixed guard', plate(880, 700, 2), 'S235JR', 'Weld mesh 25x25x2.5 in 25x25 angle frame', 'MESH', YELLOW, dims={'Width': 880, 'Height': 700}, alpha=0.35),
          (CX, 25, BT + 400), (90, 0, 0))
    con = cq.Workplane('XY').box(60, 60, 950, centered=(True, True, False)).union(cq.Workplane('XY').box(420, 160, 120, centered=(True, True, False)).translate((0, 0, 950)))
    A.add(buy('HP-630', 'Two-hand control console', con, 'Two-hand control station type IIIC (ISO 13851) on pedestal, with E-stop, mode key switch and pressure/dwell timer display', YELLOW, 14),
          (-130, 1330, 0))
    A.add(buy('HP-620', 'Pressure gauge 0-400 bar', cq.Workplane('XZ').circle(50).extrude(40), 'Glycerine-filled gauge dia 100, 0-400 bar, with gauge isolator', WHITE, 0.6), (CX - 335, CY + 582, 1250))
    A.hw('M20x110 hex bolt 10.9 + hardened washers (cylinder flange to crown)', 8)
    A.hw('M20x70 socket cap screw 12.9 (rod flange to platen)', 6)
    A.hw('M16x50 socket cap screw 12.9 (bolsters)', 12)
    A.hw('M12x50 socket cap screw 12.9 (punches to upper bolster)', 12)
    A.hw('M12 shoulder bolt (end stop pivot)', 1)
    A.hw('Hydraulic hoses 2 x 1/2 in, 280 bar, with fittings', 2)
    A.hw('Hydraulic oil ISO VG 46, 60 l', 1)
    A.hw('M16x150 anchor (base frame to floor, through to container cross-members)', 8)
    A.geom = dict(ZC=ZC, ZP=ZP, FT=FT)
    return A


# =============================================================== RC
_ROLL = {}


def roller():
    return common_buy('roll900', 'CM-ROLL900', 'Gravity roller dia 50 x 900', rod(50, 900).union(rod(12, 930).translate((-15, 0, 0))),
                      'Steel gravity conveyor roller dia 50 x 1.5, face length 900, spring-loaded axle dia 12 (hex 11), precision bearings, 60 kg rating', LGREY, 3.4)


def build_RC():
    """built in plant coordinates"""
    A = Asm('RC', 'Mould handling - roller tables, return line, charge station',
            desc='Charge table and outfeed table at the 885 mm transfer height, a lower gravity return line for the empty carrier, '
                 'and the dough-weighing shelf at the mixer discharge.')
    T = Asm('RC-150', 'Roller table 550')
    fr = table_frame('RC-1', 'Roller table frame', 550, 1000, 810, sec=(40, 40, 3), levels=[(790, 'FBLR'), (280, 'LR'), (120, 'FB')])
    T.add(fr)
    rail = p_angle('RC-111', 'Roller rail 550', 550, 40, 80, 5, GREEN,
                   notes='Drill dia 12.5 axle holes 50 mm above the heel: 5 at 110 pitch (first at 55) for the top level; the return level uses 3 of them. '
                         'The 80 leg stands 5 mm proud of the roller tops and guides the carrier.')
    T.add(rail, (550, 50, 810), (0, 0, 180)); T.add(rail, (0, 950, 810))
    T.add(rail, (550, 50, 300), (0, 0, 180)); T.add(rail, (0, 950, 300))
    r = roller()
    for k in range(5):
        T.add(r, (55 + 110 * k, 50, 860), (0, 0, 90))
    for k in range(3):
        T.add(r, (55 + 220 * k, 50, 350), (0, 0, 90))
    A.add(T, (LY.RCI[0] + 250, LY.RCI[1], 0))
    A.add(T, (LY.RCO[0], LY.RCO[1], 0))
    prail = p_flat('RC-121', 'Return rail, press section', 1090, 80, 5, GREEN, notes='Flat on edge, welded to the two bearers in the press base. 5 x dia 12.5 axle holes at 220 pitch, first at 105, 50 above the bottom edge.')
    hx, hy = LY.HP
    A.add(prail, (hx - 45, LY.RCI[1] + 47.5, 340), (90, 0, 0)); A.add(prail, (hx - 45, LY.RCI[1] + 952.5, 340), (90, 0, 0))
    for k in range(5):
        A.add(r, (hx - 45 + 105 + 220 * k, LY.RCI[1] + 50, 350), (0, 0, 90))
    # dough weighing shelf
    sx, sy = LY.RCI[0], LY.MX_C[1] - 210
    A.add(table_frame('RC-2', 'Dough scale shelf', 240, 420, 690, sec=(30, 30, 2.5), levels=[(675, 'FBLR'), (150, 'FBLR')]), (sx, sy, 0))
    A.add(p_plate('RC-255', 'Scale shelf top', 240, 420, 3, color=GREEN), (sx + 120, sy + 210, 690))
    A.add(bench_scale(), (sx + 120, sy + 210, 693), (0, 0, 90))
    tray = cq.Workplane('XY').box(240, 380, 60, centered=(True, True, False)).faces('>Z').shell(-2)
    A.add(P('RC-251', 'Dough tray', tray, 'AISI 304', 'Sheet 2 mm', 'BEND', STEEL, dims={'Inside': '236 x 376 x 58', 'Sheet': 2},
            flat=plate(356, 496, 2), notes='Cut the 356 x 496 blank with 58 mm corner notches, fold four sides up, TIG the corners. Tare the scale with the tray on it.'),
          (sx + 120, sy + 210, 748))
    A.add(buy('RC-301', 'Carrier hook tool', rod(12, 700).union(cq.Workplane('XY').box(20, 12, 60, centered=(True, True, False)).translate((690, 0, -60))),
              'Steel pull hook dia 12 x 700 with T-handle, for moving hot mould carriers and inserts', DARK, 0.8), (LY.RCI[0] + 300, LY.RCI[1] + 1020, 700), (0, 80, 0))
    A.hw('M12x100 floor anchor', 24)
    A.hw('M8x25 bolt + nut (roller rails to frames)', 24)
    A.hw('Heat-resistant gloves, 250 C contact (pairs)', 4)
    return A


# =============================================================== CR
def build_CR():
    A = Asm('CR', 'Station 6 - Cooling rack',
            desc='Four shelves, two cavity inserts per shelf (eight cooling positions). Tiles cool in the insert for about 20 min under the wall fan, '
                 'then release by shrinkage. With two more inserts in the press, ten inserts keep the press from ever waiting.')
    levels = [(1780, 'FBLR'), (150, 'BLR')] + [(z + 20, 'B') for z in (450, 800, 1150, 1500)]
    A.add(table_frame('CR-1', 'Cooling rack frame', 560, 900, 1800, sec=(40, 40, 3), levels=levels))
    run = p_angle('CR-201', 'Shelf runner', 820, 40, 40, 4, STEEL, notes='Welded to the uprights; the horizontal leg carries the insert edge (35 mm bearing each side).')
    for z in (450, 800, 1150, 1500):
        A.add(run, (40, 860, z), (0, 0, -90)); A.add(run, (520, 40, z), (0, 0, 90))
    for z in (450, 800, 1150):
        for yc in (250, 650):
            A.add('TL-101', (280, yc, z + 4), (0, 0, 0))
            A.add('TL-001', (280 - TLEN / 2, yc - TW / 2, z + 4 + ZREF), (180, 0, 90))
    A.hw('M12x100 floor anchor', 8)
    A.hw('Wall fixing bracket + M10 bolts (anti-tip, top rail to container wall)', 2)
    return A


# =============================================================== TR
def build_TR():
    A = Asm('TR', 'Station 7 - Guarded trim, check and stack station',
            desc='Flash is trimmed against a carbide burr inside a polycarbonate guard; offcuts and rejects fall into the regrind tote and go back to the next batch.')
    A.add(table_frame('TR-1', 'Trim table frame', 850, 700, 846, sec=(40, 40, 2.5), levels=[(826, 'FBLR'), (200, 'BLR')]))
    A.add(p_plate('TR-201', 'Trim table top', 890, 740, 4, holes=[(-65, 70, 40)], rects=[(-65, -60, 220, 120)], color=WHITE,
                  notes='Dia 40 hole for the trim spindle, 220 x 120 slot for offcuts. Powder-coat white so cracks and voids show up against it.'), (425, 350, 846))
    A.add(hopper('TR-21', 'Offcut funnel', (260, 160), (120, 120), 180, t=1.5, color=ORANGE, mat='DC01 galv.'), (360, 290, 666))
    A.add(tote(), (360, 300, 0), (0, 0, 0))
    sp = cq.Workplane('XY').circle(40).extrude(250).translate((0, 0, -250)).union(cq.Workplane('XY').circle(6).extrude(45))
    A.add(buy('TR-301', 'Trim spindle 0.75 kW with carbide burr', sp, 'Router / die-grinder spindle 0.75 kW, 10 000-20 000 rpm variable, under-table mount, '
              'with dia 12 x 30 cylindrical carbide burr and guide bearing; foot switch', DARK, 4), (360, 420, 846))
    G = Asm('TR-310', 'Trim guard frame', kind='weldment', weld='Weld square, grind, powder-coat yellow RAL 1023. Polycarbonate panels are screwed on with M5 button heads and washers at 120 pitch.')
    gp = p_shs('TR-311', 'Guard post', 380, 25, 25, 2, YELLOW)
    for x in (12.5, 587.5):
        for y in (12.5, 437.5):
            G.add(gp, (x, y, 0), (0, -90, 0))
    gl = p_shs('TR-312', 'Guard top rail, long', 550, 25, 25, 2, YELLOW)
    G.add(gl, (25, 12.5, 367.5)); G.add(gl, (25, 437.5, 367.5))
    gs = p_shs('TR-313', 'Guard top rail, short', 400, 25, 25, 2, YELLOW)
    G.add(gs, (12.5, 25, 367.5), (0, 0, 90)); G.add(gs, (587.5, 25, 367.5), (0, 0, 90))
    A.add(G, (60, 150, 850))

    def pc(pn, name, lx, ly):
        return P(pn, name, plate(lx, ly, 4), 'Polycarbonate', 'Polycarbonate sheet 4 mm', 'BOARD', GLASS, dims={'Length': lx, 'Width': ly, 'Thickness': 4}, alpha=0.3)
    A.add(pc('TR-321', 'Guard panel, top', 600, 450), (360, 375, 1230))
    A.add(pc('TR-322', 'Guard panel, back', 600, 380), (360, 150, 1040), (90, 0, 0))
    sd = pc('TR-323', 'Guard panel, side', 450, 380)
    A.add(sd, (56, 375, 1040), (90, 0, 90)); A.add(sd, (660, 375, 1040), (90, 0, 90))
    A.add(pc('TR-324', 'Guard panel, front upper', 600, 200), (360, 604, 1130), (90, 0, 0))
    A.add(P('TR-401', 'Trim fence', box(300, 40, 20), 'HDPE', 'HDPE board 20 mm', 'BOARD', WHITE, dims={'Size': '300 x 40 x 20'},
            notes='Screwed to the table 6 mm behind the burr; the tile edge slides along it.'), (360, 466, 850))
    A.add(control_box(), (800, 781, 950))
    A.add(p_shs('TR-901', 'Control post', 300, 30, 30, 2, GREEN), (800, 690, 846), (0, -90, 0))
    A.hw('M5x16 button-head screw + washer (guard panels)', 40)
    A.hw('Go / no-go gauge: tile must sit flat on the table top without rocking more than 3 mm', 1)
    A.hw('M12x100 floor anchor', 8)
    return A


# =============================================================== TT
def build_TT():
    A = Asm('TT', 'Tile test rig (transverse breaking load)',
            desc='Three-point bending frame with a 5 t hand-pump ram and gauge. Supports at 280 mm span (2/3 of tile length). '
                 'Test at least 5 tiles from every new recipe before production; record the breaking load.')
    B = Asm('TT-100', 'Test rig frame', kind='weldment', weld='Fully weld (a5). The top beam takes the ram reaction - weld both upright joints all round.')
    run = P('TT-101', 'Base runner', shs(800, 50, 100, 4), 'S235JR', 'RHS 100x50x4', 'SAW', DARK, dims={'Cut length': 800, 'Section': '100 x 50 x 4 (upright)'})
    B.add(run, (-400, -200, 50)); B.add(run, (-400, 200, 50))
    B.add(p_plate('TT-102', 'Base plate', 800, 500, 10, color=DARK), (0, 0, 100))
    up = p_shs('TT-103', 'Upright', 1250, 80, 80, 4, GREEN)
    B.add(up, (-300, 0, 110), (0, -90, 0)); B.add(up, (300, 0, 110), (0, -90, 0))
    B.add(p_shs('TT-104', 'Top beam', 680, 80, 80, 4, GREEN, holes=[(340, 22, 'z')]), (-340, 0, 1400))
    B.add(P('TT-105', 'Support beam', shs(400, 100, 150, 5), 'S235JR', 'RHS 150x100x5', 'SAW', LGREY, dims={'Cut length': 400, 'Section': '150 x 100 x 5'}), (-200, 0, 185))
    sd = P('TT-106', 'Support saddle', box(40, 60, 20).cut(cq.Workplane('XZ').center(0, 30).circle(15.2).extrude(60).translate((0, 30, 0))), 'S235JR', 'Flat bar 40x20', 'MILL', LGREY,
           dims={'Size': '40 x 60 x 20', 'Seat': 'R15.2 groove across the 40 mm width'})
    for sx in (-140, 140):
        B.add(sd, (sx, -150, 260)); B.add(sd, (sx, 150, 260))
    A.add(B)
    bar = p_rod('TT-201', 'Support / loading bar dia 30', 30, 360, STEEL, 'C45', notes='Bright bar; 2 supports + 1 loading nose. Free to rotate in the saddles.')
    A.add(bar, (-140, -180, 290), (0, 0, 90)); A.add(bar, (140, -180, 290), (0, 0, 90))
    ztile = 305 + 4
    A.add('TL-001', (-TLEN / 2, TW / 2, ztile), (0, 0, -90))
    znose = ztile + HR + TT_ / 2 + 15
    A.add(bar, (0, -180, znose), (0, 0, 90))
    A.add(P('TT-202', 'Loading nose holder', box(60, 60, 40).cut(cq.Workplane('XZ').center(0, 0).circle(15.2).extrude(60).translate((0, 30, 0))), 'S235JR', 'Flat bar 60x40', 'MILL', DARK,
            dims={'Size': '60 x 60 x 40', 'Seat': 'R15.2 groove', 'Top': 'M16 tapped for the ram rod'}), (0, 0, znose))
    ram = cq.Workplane('XY').circle(35).extrude(260).union(cq.Workplane('XY').circle(17).extrude(1360 - 260 - znose - 40).translate((0, 0, -(1360 - 260 - znose - 40))))
    A.add(buy('TT-301', 'Hydraulic ram 5 t with hand pump and gauge', ram, 'Single-acting 5 t ram, stroke >= 100 mm, with hand pump, hose and calibrated gauge '
              '(or a 20 kN load cell + indicator for direct reading)', BLUE, 9), (0, 0, 1360 - 260))
    A.hw('M16 rod coupler (ram to nose holder)', 1)
    A.hw('Steel rule and dial gauge (deflection reading, optional)', 1)
    return A
