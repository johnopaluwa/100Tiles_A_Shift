"""WB weigh batcher (with incline screw) and MX heated batch mixer."""
import math
import cadquery as cq
from .core import *
from . import layout as LY

WB_PIN_Z = 230.0     # screw axis height under the collecting hopper
WB_INLET = 150.0     # inlet window distance from the tail end of the screw


def wb_geometry():
    mouth = LY.MX_PORT_TOP + 15
    rise = mouth + LY.SPOUT - WB_PIN_Z
    pin_x = LY.MX_PORT[0] - LY.SPOUT - rise
    return dict(rise=rise, origin=(pin_x - 500, LY.MX_PORT[1] - 300), Lt=round(WB_INLET + rise / LY.S45 + 110))


# =============================================================== WB
def build_WB():
    A = Asm('WB', 'Station 3 - Weigh batcher',
            desc='Two 29 L weigh hoppers (sand, HDPE flakes) on single-point load cells with indicators, slide gates, a common collecting hopper '
                 'and a 45 deg screw that lifts each weighed batch into the mixer. Batch = 6.65 kg sand + 2.85 kg HDPE (70 : 30 by weight).')
    g = wb_geometry()
    fr = table_frame('WB-1', 'Weigh batcher frame', 1000, 600, 1500, sec=(50, 50, 3),
                     levels=[(1475, 'BLR'), (1230, 'B'), (800, 'FBL'), (150, 'BLR')])
    A.add(fr)
    ch = hopper('WB-2', 'Collecting hopper', (900, 500), (150, 100), 350, t=2, color=LGREY, mat='DC01 galv.')
    A.add(ch, (500, 300, 430))
    chute = cq.Workplane('XY').rect(156, 106).rect(150, 100).extrude(210).translate((0, 0, -210))
    chute = chute.cut(cq.Workplane('YZ').circle(57.2).extrude(600).translate((-300, 0, 0)).rotate((0, 0, 0), (0, 1, 0), -45).translate((0, 0, WB_PIN_Z - 430)))
    P('WB-251', 'Screw inlet chute', chute, 'S235JR', 'Sheet 3 mm', 'WELD', LGREY,
      dims={'Inside': '150 x 100', 'Height': '210 max, scribed to the 45 deg tube'},
      notes='Make as a 4-sided sleeve 210 high, offer up to the casing tube at 45 deg, scribe, cut and seal-weld to the tube round the inlet window.')
    A.add('WB-251', (500, 300, 430))
    # ---- weigh hopper weldment (origin = centre of the 100 x 100 outlet)
    W = hopper('WB-3', 'Weigh hopper', (380, 380), (100, 100), 280, t=2, color=LGREY, mat='AISI 304')
    band = p_plate('WB-303', 'Weigh hopper band', 382, 120, 2, color=LGREY, mat='AISI 304')
    W.add(band, (1, 192, 340), (90, 0, 0)); W.add(band, (-1, -190, 340), (90, 0, 0))
    W.add(band, (190, -1, 340), (90, 0, 90)); W.add(band, (-192, 1, 340), (90, 0, 90))
    sp = p_plate('WB-304', 'Weigh hopper support plate', 430, 494, 6, rects=[(0, 13, 388, 388)], holes=[(0, -222, 9), (0, -202, 9)], color=GREEN,
                 notes='Welded round the hopper at the band joint. The rear tongue bolts to the free end of the load cell; nothing else may touch the hopper.')
    W.add(sp, (0, -13, 280))
    gb = p_plate('WB-321', 'Slide gate body', 160, 160, 8, rects=[(0, 0, 100, 100)], color=STEEL, mat='AISI 304')
    W.add(gb, (0, 0, -8))
    gg = p_angle('WB-322', 'Slide gate guide', 200, 20, 20, 3, STEEL, 'AISI 304')
    W.add(gg, (-58, 100, -28), (0, 0, -90)); W.add(gg, (58, -100, -28), (0, 0, 90))
    A.add(W, (280, 350, 1035)); A.add(W, (720, 350, 1035))
    blade = p_plate('WB-323', 'Slide gate blade', 104, 250, 3, holes=[(0, 95, 28)], color=STEEL, mat='AISI 304',
                    notes='Slides in the two guide angles. Pull toward the operator to open; the dia 28 hole is the finger grip.')
    lc = buy('WB-401', 'Single-point load cell 100 kg', box(40, 150, 40), 'Aluminium single-point (platform) load cell, 100 kg, C3, '
             'rated for platforms up to 600 x 600 mm, IP65, with 3 m cable', ALU, 0.9)
    sps = p_plate('WB-402', 'Load cell spacer', 40, 50, 10, holes=[(0, -10, 9), (0, 10, 9)], color=STEEL)
    ind = buy('WB-501', 'Weighing indicator', box(200, 80, 130), 'Weighing indicator with large LED display, set-point output (2 relays), '
              '230 V; 1 per hopper. Display in kg and % of batch target', NAVY, 1.2)
    for hx in (280, 720):
        A.add(blade, (hx, 400, 1010))
        A.add(sps, (hx, 25, 1255)); A.add(lc, (hx, 75, 1265)); A.add(sps, (hx, 125, 1305))
        A.add(ind, (hx, 60, 1640))
    dp = p_shs('WB-502', 'Display post', 320, 30, 30, 2, GREEN)
    A.add(dp, (120, 25, 1500), (0, -90, 0)); A.add(dp, (880, 25, 1500), (0, -90, 0))
    A.add(p_shs('WB-503', 'Display cross bar', 790, 30, 30, 2, GREEN), (105, 25, 1835))
    # ---- incline screw
    S = screw_conveyor('WB-6', 'Batch incline screw (45 deg)', g['Lt'], color=BLUE, kw=0.37, rpm=90, inlet_x=WB_INLET, pitch=80, stub=False)
    A.add(S, (500 - WB_INLET * LY.S45, 300, WB_PIN_Z - WB_INLET * LY.S45), (0, -45, 0))
    d = g['Lt'] - 720
    px, pz = 500 - WB_INLET * LY.S45 + d * LY.S45, WB_PIN_Z - WB_INLET * LY.S45 + d * LY.S45 - 65
    post = p_shs('WB-701', 'Incline screw support post', round(pz - 57.15 / LY.S45 - 20), 50, 50, 3, GREEN)
    A.add(post, (px, 300, 10), (0, -90, 0))
    A.add(p_plate('WB-702', 'Support post base plate', 160, 160, 8, holes=[(sx * 55, sy * 55, 14) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN), (px, 300, 0))
    A.add(p_plate('WB-703', 'Support post saddle plate', 140, 140, 8, holes=[(0, -55, 11), (0, 55, 11)], color=GREEN), (px, 300, pz - 57.15 / LY.S45 - 10))
    A.add(control_box(), (1101, 640, 1000))
    A.hw('M8x40 socket cap screw (load cells)', 8)
    A.hw('M10 U-bolt for OD 114 tube', 1)
    A.hw('Stainless hand scoop 2 L', 2)
    A.hw('M12x100 floor anchor', 12)
    A.hw('Shielded load-cell cable gland + junction box', 2)
    return A


# =============================================================== MX
def build_MX():
    A = Asm('MX', 'Station 4 - Heated batch mixer',
            desc='Dia 450 x 320 jacketed drum, 8 kW electric heating (3 band heaters + base heater), anchor paddle at 30 rpm driven by a 2.2 kW gearmotor. '
                 'One batch = 9.5 kg (4 tiles) melted and mixed at 180-200 C in about 12 minutes.')
    CX, CY = 450.0, 450.0
    FT = 850.0
    fr = table_frame('MX-1', 'Mixer frame', 900, 900, FT, sec=(60, 60, 4), levels=[(FT - 30, 'FBLR'), (150, 'FBLR')])
    A.add(fr)
    deck = p_plate('MX-201', 'Mixer deck plate', 900, 900, 8, holes=[(0, 0, 360)] + [(200 * math.cos(math.radians(a)), 200 * math.sin(math.radians(a)), 13) for a in (45, 135, 225, 315)]
                   , color=GREEN,
                   notes='Dia 360 centre opening gives access to the base heater and its wiring. 4 x dia 13 take the drum standoffs; match-drill 8 x dia 14 from the two column base plates on assembly.')
    A.add(deck, (CX, CY, FT))
    Z0 = FT + 8 + 90 + 12       # inside floor of the drum
    D = Asm('MX-210', 'Mixing drum', kind='weldment',
            weld='Weld the shell to the base plate inside and out (full-penetration, the joint sees 200 C and abrasive melt). Dress the inside corner to a smooth R6. '
                 'Weld the rim flange, discharge nozzle, gate flange and the four standoffs. Pressure is atmospheric - no pressure-vessel code applies, '
                 'but use low-hydrogen filler and let the drum cool slowly to avoid distortion.')
    D.add(p_disc('MX-211', 'Drum base plate', 462, 12, color=STEEL, mat='S355J2', notes='Top face is the mixing floor: flat within 1 mm so the paddle can run 3 mm clear.'), (0, 0, -12))
    cut = cq.Workplane('XY').box(70, 140, 60, centered=(False, True, False)).translate((0, 0, -250))
    D.add(p_shell('MX-212', 'Drum shell', 462, 6, 320, STEEL, 'S355J2', cut=cut,
                  notes='Cut the 140 x 70 discharge window at the bottom edge before rolling (flat blank DXF shows the plain blank; window centred on the seam-opposite side).'),
          (0, 0, 0), (0, -90, 0))
    D.add(p_disc('MX-213', 'Drum rim flange', 600, 8, bore=463, color=STEEL, mat='S355J2'), (0, 0, 312))
    so = p_shs('MX-214', 'Drum standoff', 82, 40, 40, 3, STEEL, notes='Thin-wall standoffs limit heat flow into the frame.')
    pad = p_plate('MX-215', 'Standoff pad', 80, 80, 8, holes=[(0, 0, 13)], color=STEEL)
    for a in (45, 135, 225, 315):
        x, y = 200 * math.cos(math.radians(a)), 200 * math.sin(math.radians(a))
        D.add(so, (x, y, -94), (0, -90, 0)); D.add(pad, (x, y, -102))
    D.add(P('MX-221', 'Discharge nozzle', cq.Workplane('YZ').rect(152, 82).rect(140, 70).extrude(80), 'S355J2', 'Plate 6 mm', 'WELD', STEEL,
            dims={'Inside': '140 x 70', 'Length': 80, 'Plate': 6},
            notes='Four 6 mm plates welded into a sleeve; scribe the inner end to the dia 462 shell.'), (228, 0, 35))
    D.add(p_plate('MX-222', 'Gate flange', 240, 150, 8, rects=[(0, 0, 140, 70)], color=STEEL, mat='S355J2'), (308, 0, 35), (90, 0, 90))
    gd = p_flat('MX-224', 'Gate guide spacer', 150, 20, 7, STEEL)
    gk = p_flat('MX-225', 'Gate keeper strip', 150, 35, 5, STEEL, notes='Welded over the spacer; forms the 7 mm slot the 6 mm gate blade slides in.')
    for s in (-1, 1):
        D.add(gd, (319.5, s * 95, -40), (0, -90, 0)); D.add(gk, (325.5, s * 87.5, -40), (0, -90, 0))
    A.add(D, (CX, CY, Z0))
    A.add(p_plate('MX-223', 'Discharge gate blade', 160, 240, 6, holes=[(0, 90, 30)], color=DARK, mat='S355J2',
                  notes='Guillotine gate: lift to discharge. Fit a hardwood or PTFE grip through the dia 30 hole - the blade is hot.'),
          (CX + 316, CY, Z0 + 115), (90, 0, 90))
    P('MX-231', 'Discharge chute', cq.Workplane('YZ').polyline([(-93, 50), (-93, 0), (93, 0), (93, 50), (90, 50), (90, 3), (-90, 3), (-90, 50)]).close().extrude(330),
      'AISI 304', 'Sheet 3 mm', 'BEND', STEEL, dims={'Inside width': 180, 'Side height': 50, 'Length': 330, 'Slope': '25 deg'}, flat=plate(280, 330, 3))
    A.add('MX-231', (CX + 322, CY, Z0 - 8), (0, 25, 0))
    for i in range(3):
        A.add(buy('MX-601', 'Band heater dia 462 x 70, 1.7 kW', tube(486, 11.5, 70).rotate((0, 0, 0), (0, 1, 0), -90),
                  'Mica or ceramic band heater, ID 462, width 70, 1.7 kW 230 V, two-piece clamp, max 350 C sheath', (0.95, 0.45, 0.30), 2.5) if i == 0 else 'MX-601',
              (CX, CY, Z0 + 85 + 78 * i))
    A.add(buy('MX-602', 'Base plate heater dia 340, 3 kW', disc(340, 20), 'Cast-in aluminium or mica disc heater OD 340, 3 kW 400 V, clamped under the drum base', (0.95, 0.45, 0.30), 6),
          (CX, CY, Z0 - 32))
    jc = cq.Workplane('XY').box(100, 170, 80, centered=(False, True, False)).translate((70, 0, -330))
    A.add(p_shell('MX-241', 'Insulation cladding', 590, 1, 392, CREAM, 'AISI 304', cut=jc,
                  notes='Wraps 50 mm of ceramic-fibre blanket (128 kg/m3) round the heater bands. Overlap seam with 6 self-tapping screws so it can be removed to change a heater.'),
          (CX, CY, Z0 - 80), (0, -90, 0))
    # ---- paddle weldment (origin on the axis at the drum floor)
    Pd = Asm('MX-310', 'Anchor paddle', kind='weldment',
             weld='Weld hub to bottom blade square to the bore (check with the shaft fitted), then the two side scrapers. Hard-face the leading edges '
                  'of the bottom blade and scrapers with 2 layers of chromium-carbide electrode - sand is very abrasive.')
    Pd.add(p_plate('MX-312', 'Paddle bottom blade', 436, 60, 12, color=DARK, mat='Hardox 450'), (0, 0, 3))
    sc = p_flat('MX-313', 'Paddle side scraper', 250, 40, 10, DARK, 'Hardox 450')
    Pd.add(sc, (213, 0, 15), (0, -90, 0)); Pd.add(sc, (-203, 0, 15), (0, -90, 0))
    Pd.add(P('MX-314', 'Paddle hub', tube(70, 15, 60).cut(cq.Workplane('XZ').center(30, 0).circle(6.5).extrude(80).translate((0, 40, 0))), 'C45', 'Round bar dia 70', 'TURN', STEEL,
             dims={'OD': 70, 'Bore': '40 H8', 'Length': 60, 'Cross hole': 'dia 13 for M12 bolt'}), (0, 0, 15), (0, -90, 0))
    A.add(Pd, (CX, CY, Z0))
    ZB = 1650.0
    sh_len = round(ZB + 112 + 160 + 10 - (Z0 + 15))
    P('MX-311', 'Agitator shaft dia 40', stepped([(40, sh_len)], keys=[(sh_len - 175, 170, 12, 5, 40)]).cut(
        cq.Workplane('XZ').center(30, 0).circle(6.5).extrude(60).translate((0, 30, 0))), 'C45', 'Round bar dia 40 h9 bright', 'TURN', STEEL,
      dims={'Length': sh_len, 'Diameter': '40 h9', 'Keyway': '12 P9 x 5 deep x 170 at the top end', 'Cross hole': 'dia 13, 30 from the bottom end'})
    A.add('MX-311', (CX, CY, Z0 + 15), (0, -90, 0))
    col = p_shs('MX-301', 'Bridge column', round(ZB - FT - 18), 80, 80, 4, GREEN)
    cb = p_plate('MX-302', 'Column base plate', 160, 160, 10, holes=[(sx * 60, sy * 55, 14) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN)
    BA = -30.0                                    # bridge angle in plan
    ca, sa = math.cos(math.radians(BA)), math.sin(math.radians(BA))
    for s in (-1, 1):
        A.add(cb, (CX + s * 390 * ca, CY + s * 390 * sa, FT + 8), (0, 0, BA)); A.add(col, (CX + s * 390 * ca, CY + s * 390 * sa, FT + 18), (0, -90, BA))
    A.add(p_shs('MX-303', 'Mixer bridge beam', 860, 100, 100, 5, GREEN, holes=[(430, 62, 'z')],
                notes='Dia 62 through both walls on the centre for the shaft. Match-drill 4 x dia 14 (102 x 102) in the bottom wall for the UCF208 and '
                      '4 x dia 11 in the top wall for the gearbox foot. Weld to both column tops with a5 fillets all round. The bridge runs at 30 deg to the line so the discharge chute and the batch screw both stay clear.'), (CX - 430 * ca, CY - 430 * sa, ZB + 50), (0, 0, BA))
    A.add(ucf(40), (CX, CY, ZB), (0, 90, 0))
    A.add(p_disc('MX-304', 'Gearbox mounting plate', 180, 12, bore=62, holes=pcd(4, 140, 11, 45), color=GREEN,
                  notes='Welded on top of the bridge; lifts the gearmotor so the motor body clears the beam.'), (CX, CY, ZB + 100))
    A.add(gearmotor(2.2, 40, 30), (CX, CY, ZB + 112 + 80), (0, -90, 180))
    # ---- lids
    rear = cq.Workplane('XY').moveTo(-300, 0).threePointArc((0, -300), (300, 0)).close().extrude(3)
    rear = rear.cut(cq.Workplane('XY').circle(35).extrude(3)).cut(cq.Workplane('XY').center(-60, -140).rect(130, 110).extrude(3))
    P('MX-321', 'Rear lid with charge port', rear, 'AISI 304', 'Sheet 3 mm', 'LASER', STEEL, dims={'Diameter': 600, 'Charge port': '130 x 110', 'Shaft notch': 'R35'})
    front = cq.Workplane('XY').moveTo(-300, 0).threePointArc((0, 300), (300, 0)).close().extrude(3).cut(cq.Workplane('XY').circle(35).extrude(3))
    P('MX-322', 'Front lid (hinged, inspection)', front, 'AISI 304', 'Sheet 3 mm', 'LASER', STEEL, dims={'Diameter': 600, 'Shaft notch': 'R35'},
      notes='Hinged on the rim flange; fit a limit switch so the agitator stops when the lid is lifted.')
    A.add('MX-321', (CX, CY, Z0 + 320)); A.add('MX-322', (CX, CY, Z0 + 320))
    P('MX-323', 'Charge collar', cq.Workplane('XY').rect(134, 114).rect(130, 110).extrude(LY.MX_PORT_TOP - (Z0 + 323)), 'AISI 304', 'Sheet 2 mm', 'BEND', STEEL,
      dims={'Inside': '130 x 110', 'Height': round(LY.MX_PORT_TOP - (Z0 + 323))}, flat=plate(488, round(LY.MX_PORT_TOP - (Z0 + 323)), 2))
    A.add('MX-323', (CX - 60, CY - 140, Z0 + 323))
    # ---- extraction hood
    Hd = hopper('MX-4', 'Fume extraction hood', (1000, 1000), (250, 250), 300, t=1.5, color=WHITE, mat='DC01 galv.')
    A.add(Hd, (CX, 480, 2350), (180, 0, 0))
    br = p_angle('MX-411', 'Hood wall bracket', 990, 50, 50, 5, GREEN)
    A.add(br, (-58, 920, 2045), (0, 0, -90)); A.add(br, (958, -70, 2045), (0, 0, 90))
    wp_ = p_plate('MX-412', 'Hood bracket wall plate', 150, 150, 8, holes=[(sx * 50, sy * 50, 11) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN)
    A.add(wp_, (-33, -72, 2070), (90, 0, 0)); A.add(wp_, (933, -72, 2070), (90, 0, 0))
    A.add(buy('MX-420', 'Spiral duct dia 200, vertical', tube(200, 0.8, 150).rotate((0, 0, 0), (0, 1, 0), -90), 'Galvanised spiral duct dia 200 with 250x250-to-dia-200 square/round adapter and one 90 deg bend', LGREY, 3),
          (CX, 480, 2350))
    A.add(buy('MX-421', 'Inline extraction fan dia 200', tube(200, 0.8, 300).union(tube(260, 30, 160).translate((70, 0, 0))), 'Inline duct fan dia 200, approx. 800 m3/h, metal casing, '
              'motor out of the air stream or rated 60 C, with weather cowl through the back wall', LGREY, 6), (CX, 380, 2500), (0, 0, -90))
    # ---- guard
    Gd = Asm('MX-510', 'Front guard panel', kind='weldment', weld='Mitre or butt the 25 SHS frame, weld, then stitch the mesh to the inside every 100 mm. Powder-coat RAL 1023.')
    gv = p_shs('MX-511', 'Guard frame upright', 700, 25, 25, 2, YELLOW)
    gh = p_shs('MX-512', 'Guard frame rail', 850, 25, 25, 2, YELLOW)
    Gd.add(gv, (12.5, 0, 0), (0, -90, 0)); Gd.add(gv, (887.5, 0, 0), (0, -90, 0))
    Gd.add(gh, (25, 0, 12.5)); Gd.add(gh, (25, 0, 687.5))
    Gd.add(P('MX-513', 'Guard mesh infill', plate(850, 650, 2), 'S235JR', 'Weld mesh 25x25x2.5', 'MESH', YELLOW, dims={'Width': 850, 'Height': 650, 'Mesh': '25 x 25 x 2.5'}, alpha=0.35),
           (450, 13, 350), (90, 0, 0))
    A.add(Gd, (0, 935, FT + 30))
    A.add(p_shs('MX-702', 'Panel post', 1500, 40, 40, 3, GREEN), (-30, 985, 8), (0, -90, 0))
    A.add(p_plate('MX-703', 'Panel post foot', 130, 60, 8, holes=[(-45, 0, 14), (45, 0, 14)], color=GREEN), (-30, 985, 0))
    A.add(buy('MX-701', 'Mixer heater control panel', box(400, 200, 500).union(cq.Workplane('XZ').workplane(offset=-108).center(0, 380).rect(120, 60).extrude(8)),
              'Wall/post-mounted panel 400x500x200 IP54: 2 x PID temperature controller (drum wall, melt), 4 x SSR 25 A with heat sinks, main contactor, '
              'agitator VFD 2.2 kW, lid interlock relay, E-stop, batch timer', WHITE, 18), (130, 1105, 1000))
    A.hw('Ceramic-fibre blanket 50 mm, 128 kg/m3, 1.2 m2', 1)
    A.hw('Thermocouple type K, bayonet, with 3 m lead (1 wall, 1 melt probe through the rear lid)', 2)
    A.hw('M12x40 bolt + nut + ceramic washer (drum standoffs)', 4)
    A.hw('M12x40 bolt + nut (bridge columns)', 8)
    A.hw('M12x90 bolt 10.9 + nyloc nut (paddle hub cross bolt)', 1)
    A.hw('Parallel key 12x8x160', 1)
    A.hw('Lid safety limit switch', 1)
    A.hw('M12x100 floor anchor', 8)
    A.z0 = Z0
    return A
