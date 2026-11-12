"""CT container conversion, SC solar canopy, EL electrical, FG finished goods - all in plant coordinates."""
import math
import cadquery as cq
from .core import *
from . import layout as LY
from .m_press import TLEN, TW, TT_, HR

G = LY.G
T10 = math.tan(math.radians(10)); C10 = math.cos(math.radians(10)); S10 = math.sin(math.radians(10))
FANS = [(1900, 2250), (5600, 2250), (10180, 2250)]
LOUVRES = [(800, 2300), (3300, 2300), (7900, 2300), (11300, 2300)]


def build_CT():
    A = Asm('CT', 'Container shell conversion (40 ft high-cube)',
            desc='One long side wall is cut out and replaced by a welded header beam on three posts. The back wall gets three dia 500 exhaust fans, '
                 'four intake louvres and the mixer fume duct. LED lighting under the roof.')
    Lx, W, H = LY.CT_L, LY.CT_W, LY.CT_H
    sh = cq.Workplane('XY').box(Lx + 160, W + 86, 170, centered=False).translate((-80, -43, G))            # base + floor
    back = cq.Workplane('XY').box(Lx + 160, 43, H, centered=False).translate((-80, -43, 0))
    for x, z in FANS:
        back = back.cut(cq.Workplane('XZ').center(x, z).circle(260).extrude(60).translate((0, 10, 0)))
    for x, z in LOUVRES:
        back = back.cut(cq.Workplane('XZ').center(x, z).rect(500, 400).extrude(60).translate((0, 10, 0)))
    back = back.cut(cq.Workplane('XZ').center(LY.MX_C[0], 2500).circle(105).extrude(60).translate((0, 10, 0)))
    sh = sh.union(back)
    for x0 in (-80, Lx):
        sh = sh.union(cq.Workplane('XY').box(80, W + 86, H, centered=False).translate((x0, -43, 0)))
    sh = sh.union(cq.Workplane('XY').box(Lx + 160, 60, 60, centered=False).translate((-80, W - 17, H - 60)))   # front top side rail
    P('CT-001', '40 ft high-cube container, modified', sh, 'Purchased', 'ISO 1AAA container 12.19 x 2.44 x 2.90 m, cargo-worthy', 'MOD', CTGREEN, kind='buy', mass=3900,
      spec='Used ISO 40 ft high-cube dry container, wind- and water-tight, floor sound, CSC plate not required. Internal 12.03 x 2.35 x 2.69 m.',
      dims={'External': '12192 x 2438 x 2896', 'Internal': '12032 x 2352 x 2690', 'Side opening': '12032 x 2490 clear (front long side)',
            'Fan openings': '3 x dia 520 at 2250 above floor', 'Louvre openings': '4 x 500 x 400 at 2300 above floor', 'Duct opening': 'dia 210 at 2500'},
      route=['Set the container level on six concrete pads or sleepers (four corner castings + two mid-span under the bottom side rails), 170 mm floor height. Check diagonals.',
             'BEFORE cutting anything: tack the header beam CT-101 under the front top side rail and fit the three posts CT-102 with their plates (CT-103) '
             'plumb at x = 3008, 6016 and 9024 mm. Fully weld header to top rail (stitch 50/150 both sides) and posts to header and to the bottom side rail.',
             'Only then cut out the corrugated front side panel between the corner posts, flush with the top and bottom rails (plasma or 1 mm slitting discs). '
             'Grind the cut edges smooth and cap with 30 x 3 flat if ragged.',
             'Mark the back-wall openings from inside (heights from the floor): 3 fan holes dia 520, 4 louvre openings 500 x 400, 1 duct hole dia 210. '
             'Frame each rectangular opening with 30 x 30 x 3 angle welded to the corrugation so the louvre has a flat seat.',
             'Wire-brush, prime (zinc phosphate) and repaint all cut edges. Seal the plywood floor with two coats of epoxy floor paint; '
             'mark the 1.0 m walking aisle and one-way arrows in yellow.',
             'Bond the container to the earth electrode (see electrical notes) before any machine is powered.'])
    A.add('CT-001')
    roof = cq.Workplane('XY').box(Lx + 160, W + 86, 36, centered=False).translate((-80, -43, H))
    P('CT-002', 'Container roof (part of CT-001, kept)', roof, 'Purchased', 'part of container', 'BUY', CTGREEN, kind='buy', mass=0, spec='Original roof panel is retained - shown transparent.', alpha=0.18)
    A.add('CT-002')
    A.add(P('CT-101', 'Front header beam', shs(Lx, 100, 200, 6), 'S355J2', 'RHS 200x100x6', 'SAW', GREEN,
            dims={'Cut length': Lx, 'Section': '200 x 100 x 6', 'Note': 'supplied as 2 x 6016, full-penetration butt weld over the centre post'}),
          (0, W - 67, H - 160))
    post = p_shs('CT-102', 'Front opening post', H - 280, 100, 100, 5, GREEN, 'S355J2')
    pl = p_plate('CT-103', 'Post end plate', 200, 200, 10, holes=[(sx * 70, sy * 70, 14) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN)
    for x in (3008, 6016, 9024):
        A.add(pl, (x, W - 67, 0)); A.add(post, (x, W - 67, 10), (0, -90, 0)); A.add(pl, (x, W - 67, H - 270))
    lou = buy('CT-201', 'Weather louvre 500 x 400', box(540, 45, 440, c=(True, False, True)), 'Aluminium weather louvre 500 x 400 with insect mesh, flanged frame', LGREY, 3)
    for x, z in LOUVRES:
        A.add(lou, (x, -45, z))
    fan = cq.Workplane('XZ').circle(270).circle(245).extrude(120).union(cq.Workplane('XZ').circle(60).extrude(80))
    for k in range(5):
        fan = fan.union(cq.Workplane('XZ').transformed(rotate=(0, 0, 72 * k)).center(140, 0).rect(190, 60).extrude(10).translate((0, -40, 0)))
    fw = buy('CT-202', 'Wall axial fan dia 500', fan, 'Plate-mounted axial exhaust fan dia 500, approx. 6000 m3/h, 0.25 kW, IP55, with finger guard and gravity shutter', BLACK, 9)
    for x, z in FANS:
        A.add(fw, (x, 80, z))
    led = buy('CT-203', 'LED batten 1500 mm, 50 W', box(1500, 80, 60), 'IP65 LED batten 1.5 m, 50 W, 4000 K, approx. 6500 lm (target 300 lux on the work surfaces)', WHITE, 2)
    for k in range(6):
        A.add(led, (1000 + 2000 * k, 1300, H - 60))
    ext = buy('CT-204', 'Fire extinguisher 6 kg ABC + CO2 2 kg set', cq.Workplane('XY').circle(75).extrude(500), '6 kg ABC powder + 2 kg CO2 extinguisher, wall brackets, sign', RED, 12)
    A.add(ext, (150, 2150, 0)); A.add(ext, (11900, 1100, 0))
    A.hw('Concrete pad 600 x 600 x 300 (container supports)', 6)
    A.hw('Epoxy floor paint, 30 m2 two coats + yellow line paint', 1)
    A.hw('First-aid kit, burns kit and eyewash station', 1)
    A.hw('Angle 30x30x3 for louvre frames, 8 m', 1)
    return A


def zt(y):
    return 3300.0 + (y + 600.0) * T10


def build_SC():
    A = Asm('SC', 'Solar canopy 19.8 kWp',
            desc='36 x 550 W modules (6 columns x 6 rows, landscape) at 10 deg on a 13.8 x 6.9 m steel canopy. Four portal frames at 4.6 m centres, '
                 'seven purlin lines. The canopy shades the container and the work apron.')
    XF = [-884.0 + 4600 * k for k in range(4)]
    Y0 = -920.0
    YR, YFp = -600.0, 4900.0
    raft = P('SC-101', 'Rafter', shs(7000, 100, 200, 5), 'S355J2', 'RHS 200x100x5', 'SAW', GREEN,
             dims={'Cut length': 7000, 'Section': '200 x 100 x 5', 'Slope': '10 deg'},
             notes='Shop-weld the 7 purlin cleats on top at 1154 mm pitch (first at 40 mm from the low end) and the two post-cap seating plates underneath.')
    base = p_plate('SC-102', 'Post base plate', 350, 350, 16, holes=[(sx * 130, sy * 130, 22) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN, mat='S355J2')
    cap = p_plate('SC-103', 'Post cap plate', 180, 300, 12, holes=[(sx * 60, sy * 115, 18) for sx in (-1, 1) for sy in (-1, 1)], color=GREEN, mat='S355J2',
                  notes='Welded on the post top at 10 deg; 4 x M16 into the rafter.')
    zr_top = zt(YR) - 200 / C10 - 12.2 - 13.5
    zf_top = zt(YFp) - 200 / C10 - 12.2 - 13.5
    pr = p_shs('SC-111', 'Rear post', round(zr_top - G - 16), 150, 150, 5, GREEN, 'S355J2', notes='Top end mitred 10 deg.')
    pf = p_shs('SC-112', 'Front post', round(zf_top - G - 16), 150, 150, 5, GREEN, 'S355J2', notes='Top end mitred 10 deg.')
    kb = {}
    for i, x in enumerate(XF):
        A.add(raft, (x, Y0, zt(Y0) - 100 / C10), (0, -10, 90))
        for yp, post, ztop, sgn, kpn in ((YR, pr, zr_top, 1, 'SC-104'), (YFp, pf, zf_top, -1, 'SC-105')):
            A.add(base, (x, yp, G)); A.add(post, (x, yp, G + 16), (0, -90, 0))
            A.add(cap, (x, yp, zt(yp) - 200 / C10 - 12.6), (10, 0, 0))
            p1 = (x, yp + sgn * 75, ztop - 650)
            y2 = yp + sgn * 700
            p2 = (x, y2, zt(y2) - 200 / C10 - 25)
            pos, rot, Lg = between(p1, p2)
            if kpn not in kb:
                kb[kpn] = p_shs(kpn, 'Knee brace, ' + ('rear' if sgn > 0 else 'front'), round(Lg), 60, 60, 3, GREEN, notes='Both ends mitred to suit post and rafter; weld all round.')
            A.add(kb[kpn], pos, rot)
    pur = P('SC-201', 'Purlin', shs(4590, 60, 120, 3), 'S355J2', 'RHS 120x60x3, hot-dip galvanised', 'SAW', LGREY,
            dims={'Cut length': 4590, 'Section': '120 x 60 x 3', 'End holes': '2 x dia 14 each end, 60 from the end'})
    cl = p_angle('SC-203', 'Purlin cleat', 120, 100, 75, 8, GREEN, 'S355J2', notes='Welded on the rafter top; each purlin end is fixed with 2 x M12.')
    for j in range(7):
        s = 40 + 1154 * j
        y = Y0 + s * C10; zc = zt(y)
        for k in range(3):
            A.add(pur, (XF[k] + 5, y + 60 * -S10, zc + 60 * C10), (10, 0, 0))
        for x in XF:
            A.add(cl, (x - 60, y + 30 * C10, zc + 30 * S10), (10, 0, 0))
    mod = cq.Workplane('XY').box(2278, 1134, 35, centered=(True, True, False)).faces('<Z').shell(-2) if False else cq.Workplane('XY').box(2278, 1134, 35, centered=(True, True, False))
    pv = buy('SC-401', 'PV module 550 W', mod, 'Monocrystalline 550 Wp module, 144 half-cells, approx. 2278 x 1134 x 35 mm, 28 kg, Vmp ~41.7 V, Imp ~13.2 A', PV, 28)
    for r in range(6):
        s = 50 + 1154 * r + 567
        y = Y0 + s * C10; zc = zt(y)
        for c in range(6):
            A.add(pv, (-884 + 16 + 1139 + 2298 * c, y - 120 * S10, zc + 120 * C10), (10, 0, 0))
    br = {}
    for (k, yp, pn) in ((0, YR, 'SC-301'), (2, YR, 'SC-301'), (2, YFp, 'SC-302')):
        ztop = zr_top if yp == YR else zf_top
        for a, b in ((0, 1), (1, 0)):
            yb = yp + (-12 if a == 0 else 12)
            p1 = (XF[k + a] + (90 if a == 0 else -90), yb, G + 250)
            p2 = (XF[k + b] + (90 if b == 0 else -90), yb, ztop - 250)
            pos, rot, Lg = between(p1, p2)
            if pn not in br:
                br[pn] = p_rod(pn, 'Bracing rod dia 16, ' + ('rear' if pn == 'SC-301' else 'front'), 16, round(Lg), GREEN, 'S355J2',
                               notes='Thread M16 x 150 one end for the turnbuckle; 10 mm gusset lugs on the posts.')
            A.add(br[pn], pos, rot)
    A.add(buy('SC-501', 'PV combiner box', box(400, 200, 500), 'DC combiner: 3 strings of 12 modules (approx. 500 V, 13 A each), string fuses 20 A gPV, '
              'type 2 DC surge arrester, 1000 V DC isolator', LGREY, 8), (XF[3], YR - 180, 1200))
    A.hw('M20x300 chemical anchor (post base plates, 4 per post)', 32)
    A.hw('Concrete footing 800 x 800 x 800, C25/30 (verify for local wind and soil)', 8)
    A.hw('PV mid clamp 35 mm with M8 T-bolt', 60)
    A.hw('PV end clamp 35 mm with M8 T-bolt', 24)
    A.hw('M12x150 hex bolt 8.8 through purlin + nut + washers', 84)
    A.hw('M16x60 hex bolt 8.8 (post caps)', 32)
    A.hw('Turnbuckle M16 + clevis', 6)
    A.hw('Solar cable 6 mm2 red/black, 200 m; MC4 connectors 80 pairs', 1)
    A.hw('Earth bonding strap + lug per module row, 16 mm2 Cu to earth rod', 1)
    return A


def build_EL():
    A = Asm('EL', 'Power system - inverter, battery, distribution, generator',
            desc='19.8 kWp PV on a 20 kW three-phase hybrid inverter with a 40 kWh LiFePO4 battery. Backup generator for cloudy days. '
                 'Connected machine load approx. 27 kW; mixing and pressing are scheduled for the strongest sun.')
    cab = box(600, 600, 2000).union(cq.Workplane('XZ').workplane(offset=-308).center(0, 1650).rect(120, 120).extrude(8))
    A.add(buy('EL-001', 'Battery cabinet 40 kWh LiFePO4', cab, '8 x 5.12 kWh 51.2 V LiFePO4 rack modules (40.96 kWh) in a 600 x 600 x 2000 cabinet with BMS, '
              'DC breaker 250 A, busbars; ventilated; non-combustible plinth', NAVY, 420), (LY.EL[0] + 300, LY.EL[1] + 300, 0))
    A.add(buy('EL-002', 'Hybrid inverter 20 kW 3-phase', box(520, 240, 680), '20 kW 400 V three-phase hybrid inverter/charger, 2 MPPT (150-850 V), 48 V battery port, '
              'generator input with auto-start contact, IP65', WHITE, 48), (10900, 125, 1400))
    A.add(buy('EL-003', 'Main distribution board', box(250, 600, 800), 'Steel DB 600 x 800 x 250, IP54: 63 A 4-pole main switch, type 2 AC SPD, 30 mA RCDs, MCBs/motor breakers per machine, '
              'E-stop loop relay, energy meter', LGREY, 30), (LY.CT_L - 125, 1250, 1000))
    gen = box(1500, 800, 1000).union(cq.Workplane('XY').workplane(offset=1000).center(-500, 200).circle(30).extrude(300))
    A.add(buy('EL-004', 'Backup diesel generator 20 kVA', gen, 'Silent canopy diesel generator 20 kVA / 16 kW, 400 V 50 Hz, 2-wire auto-start', YELLOW, 650), (13100, 500, G))
    A.hw('Armoured cable 5 x 10 mm2 (DB to inverter), 12 m', 1)
    A.hw('Cable tray 100 mm along the back wall at 2.55 m, 12 m, with drops to each machine', 1)
    A.hw('Machine supply cables H07RN-F, sizes per load schedule', 1)
    A.hw('Earth electrode 2 x 2.4 m copper-clad rods + 16 mm2 main earth; bond container, canopy and every machine frame', 1)
    A.hw('Emergency-stop loop: buttons at every station wired in series to the main contactor', 1)
    return A


def build_FG():
    A = Asm('FG', 'Finished goods pallet', desc='Approved tiles are stacked on edge-protected pallets, 100 per shift (about 220 kg).')
    pal = box(1200, 1000, 22).translate((0, 0, 122))
    for y in (-450, 0, 450):
        pal = pal.union(box(1200, 100, 100).translate((0, y, 22))).union(box(1200, 100, 22).translate((0, y, 0)))
    A.add(buy('FG-001', 'Pallet 1200 x 1000', pal, 'Timber pallet 1200 x 1000 mm, 4-way entry, 1000 kg', WOOD, 22), (0, 0, 0))
    for sx in (-380, 0, 380):
        for k in range(10):
            A.add('TL-001', (sx - TW / 2, -TLEN / 2, 160 + k * 22))
    return A
