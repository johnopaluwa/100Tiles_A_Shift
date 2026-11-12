"""Engineering narrative for every machine + the written manufacturing guide + data for the hub page."""
import os
from .core import PARTS, ASMS, HARDWARE, Asm
from . import export, plant
from .drawing import PROC_NAME

BASIS = [
    ('Product', 'Double-roman roof tile 420 x 330 mm, 8 mm wall, 2.2 kg (model: 2.19 kg at 1.72 g/cm3)'),
    ('Output', '100 tiles per 8 h shift = 220 kg of finished product'),
    ('Starting recipe', '70 % dry screened sand + 30 % HDPE flakes, by weight (to be tuned by testing)'),
    ('Raw material per shift', 'about 162 kg sand and 69 kg HDPE including 5 % flash and rejects, which are re-ground and reused'),
    ('Batch', '9.5 kg = 6.65 kg sand + 2.85 kg HDPE = 4 tiles; 25 batches per shift, one every 15-16 min'),
    ('Press cycle', '2 tiles per cycle, 50 cycles per shift; 60-90 s under pressure; 1030 kN at 210 bar = 3.7 MPa on the tiles'),
    ('Cooling', 'about 20 min in the cavity insert on the rack; 10 inserts in rotation'),
    ('Melt temperature', '180-200 C in the mixer (HDPE melts at ~130 C; keep below 230 C to avoid fumes and degradation)'),
    ('Footprint', 'one 40 ft high-cube container (12.03 x 2.35 x 2.69 m inside) under a 13.8 x 6.9 m solar canopy'),
    ('Power', '36 x 550 W = 19.8 kWp PV, 20 kW hybrid inverter, 40 kWh LiFePO4 battery, 20 kVA backup generator'),
    ('Crew', '2 operators on the line (prep + mixing, pressing + finishing) plus yard / loader help'),
]
ENERGY = [
    ('Mixer heaters (8.1 kW)', '25 batches x ~1.15 kWh', 29),
    ('Sand dryer heater + blower (4.7 kW)', '2.7 h', 13),
    ('Hydraulic power unit (4 kW)', '25 % duty over 6.5 h', 6.5),
    ('Shredder (4 kW)', '2 h at 60 % load', 5),
    ('Wall fans + fume fan (0.85 kW)', '8 h', 7),
    ('Dust collector (0.75 kW)', '3 h', 2.5),
    ('Agitator (2.2 kW)', '5 h at 50 % load', 5.5),
    ('Screws, vibrator, trim spindle', 'intermittent', 3),
    ('Lighting and controls', '8 h', 3.5),
]
VALIDATE = [
    ('Recipe', 'Mould test tiles at 60/40, 65/35, 70/30 and 75/25 sand/HDPE. Break five of each on the test rig and compare with your local tile standard. Sand grading and plastic grade change the answer.'),
    ('Heating temperatures', 'Find the lowest melt temperature that still wets every grain (start at 190 C). Log wall and melt thermocouples; confirm the 8 kW heaters reach it in the 12 min batch time.'),
    ('Press force', 'The 1000 kN / 3.7 MPa figure is an estimate. Check tiles for voids and short corners at 100, 150 and 210 bar and set the relief valve at the lowest pressure that gives sound tiles.'),
    ('Cooling time', 'Measure when a tile releases without warping (target 20 min). This fixes how many inserts you really need.'),
    ('Structure', 'The press crossheads, columns, canopy and the cut container need checking by a structural / mechanical engineer for your steel grades, wind zone and soil. Calculations here are first-pass sizing only.'),
    ('Electrical protection', 'Cable sizes, breaker ratings, earthing, RCDs, PV string design and battery protection must be designed and signed off by a qualified electrician to the local code.'),
    ('Ventilation', 'Measure fume and respirable silica dust at the operator positions with the fans running. Sand dust is a serious lung hazard; molten plastic fume must be extracted at source.'),
]
DEVIATIONS = [
    'Handing: the model is laid out as a mirror image of the video. Standing at the open side, material flows from right (sorting) to left (finished tiles); in the video it runs left to right. The process and every machine are the same - mirror the layout on site if the other hand suits your yard better.',
    'Sand feed: the video shows one tube from the outside hopper to the dryer. A single tube at that height would block the walking aisle, so the model uses a 45 deg elevating screw outside plus a horizontal transfer screw that crosses the aisle overhead with 2.09 m headroom.',
    'Weigh hoppers are filled by hand scoop from the sand and flake totes. The two overhead feed spouts in the video are left out (they would need two more conveyors and day bins); they can be added later.',
    'Moulds: a steel carrier holds two separate cast-aluminium cavity inserts. Each insert (about 18 kg + tile) is lifted to the rack by hand; a one-piece two-cavity steel mould would weigh over 140 kg and need a hoist.',
    'The mixer stands 250 mm higher than drawn in the video so the melt discharges at table height onto the dough scale.',
    'The container roof is kept (the video removes it only to show the inside). The open long side gets a welded header beam and three posts.',
    'The hydraulic power unit sits on the press crown; the press is 1.0 m wide along the line with the two cavities one behind the other.',
    'The canopy is drawn as 6 x 6 modules in landscape (13.8 x 6.9 m) on four portal frames.',
    'People, the skid-steer loader, the house and the landscaping are not modelled.',
]
SAFETY = [
    'PVC must never reach the shredder or mixer: heated PVC releases hydrogen chloride gas. Train the sorter, keep the red reject bin at the table and do a float test when unsure (HDPE floats in water, PVC and PET sink).',
    'Silica dust: run the dust collector whenever the dryer and screen run; wear P3 / N99 masks when handling dry sand; damp down spillage instead of dry sweeping.',
    'Hot work at 200 C: long sleeves, face shield and 250 C contact gloves at the mixer and press. Keep a burns kit and running water within 10 m.',
    'Press: never bypass the two-hand control or light curtain. Fit the mechanical safety prop before reaching between the platens for tool changes. Hoses rated 280 bar minimum.',
    'Shredder: the hopper is deep enough that hands cannot reach the knives; never stand on anything to reach in. Lock off the isolator before clearing a jam. Reversing starter recommended.',
    'Mixer: lid interlock stops the paddle; discharge only with the guard closed. Fume hood fan interlocked with the heaters.',
    'Electrical: battery cabinet on a non-combustible plinth, 1 m clear, CO2 extinguisher beside it. All frames bonded to earth. E-stops at every station in one loop.',
    'Housekeeping: the 1.0 m aisle stays clear; one-way flow from raw material to finished tiles; plastic stock stored away from the mixer.',
]
WORKSHOP = [
    ('Cutting', 'Band saw or cold saw for sections up to 200 x 100; plasma cutter; access to a laser / waterjet shop for the DXF plate parts (about 137 profiles)'),
    ('Forming', 'Three-roll bender for 3-6 mm plate up to 1.5 m wide; press brake or box folder for 1.5-3 mm sheet'),
    ('Welding', 'MAG 250 A (135) for structural work, TIG for stainless sheet; flat welding table 2 x 1 m; clamps and squares'),
    ('Machining', 'Centre lathe 1.6 m between centres with steady (press columns); milling machine; access to a horizontal borer for the press crossheads and a 3-axis CNC mill 600 x 500 for the mould'),
    ('Other', 'Pillar drill, magnetic drill, taps and dies to M20, torque wrench to 400 N.m, 2 t chain block or forklift, laser level'),
]
SEQUENCE = [
    'Site: cast six container pads and eight canopy footings; lay the earth electrode. Let concrete cure 7 days.',
    'Canopy first (it gives shade and power for the rest of the build): posts, rafters, purlins, modules, combiner; then inverter, battery and distribution board on temporary mounts.',
    'Container: set level, weld in header and posts, cut the side, cut wall openings, paint, floor coating, lights, fans, louvres, cable tray.',
    'Fabricate all frames (the cut list CSV groups members by section), prime and paint.',
    'Build the simple machines first to train the team: sorting table, cooling rack, roller tables, trim station, dust collector.',
    'Screw conveyors (three use the same flights, bearings and stub shafts), then the receiving hopper, weigh batcher and vibrating screen.',
    'Rotary dryer, shredder, mixer.',
    'Press: crossheads fabricated, stress-relieved and bored together; columns turned as a matched set; assemble on the base frame, fit cylinder and power unit, pressure-test at 1.1 x working pressure.',
    'Mould tooling: pattern, castings, CNC machining, trial fit in the press with modelling clay to check the 8 mm wall.',
    'Place machines to the plant datums (drawing set PLANT), anchor, wire, bond, test every E-stop, then commission station by station with material.',
    'Run the validation programme with the test rig before any tile is sold.',
]

M = {}
M['CT'] = dict(
    specs=[('Container', 'ISO 40 ft high-cube, 12.19 x 2.44 x 2.90 m'), ('Clear side opening', '12.03 m x 2.49 m high'), ('Header', 'RHS 200 x 100 x 6 on 3 posts SHS 100 x 100 x 5 at 3.0 m centres'),
           ('Ventilation', '3 x dia 500 wall fans (about 18 000 m3/h total, > 60 air changes/h) + 4 louvres'), ('Lighting', '6 x 50 W LED battens, target 300 lux')],
    build=['Follow the route on sheet CT-001: support, reinforce, then cut. Never cut the side wall before the header and posts are welded in - the wall is part of the container structure.',
           'Fit louvres from outside on a bead of sealant, fans from inside with their shutters outside.', 'Hang the LED battens on the roof bows at 1.3 m from the back wall, above the machine fronts.',
           'Fix the cable tray along the back wall at 2.55 m.'],
    check=['Diagonals of the open side within 5 mm after cutting.', 'Roof does not pond water; no daylight through the weld seams.', 'Every opening has no sharp edges.'],
    safety=['A cut container has lost its racking strength: do not lift or transport it without re-bracing the open side.'])
M['ST'] = dict(
    specs=[('Table', '900 x 600 x 850 mm, HDPE top'), ('Bins', 'red = reject (PVC, PET, PP, unknown), green = HDPE only')],
    build=['Weld frame ST-100, paint, screw the top on.', 'Anchor against the back wall next to the shredder.'],
    check=['Top is level and does not rock.'],
    operate=['Tip the incoming sack on the table. Keep only items marked 2 / HDPE (jerry cans, crates, bottle caps, detergent bottles). Remove labels, metal and dirt.',
             'Cut pieces larger than 250 mm with a hand saw so they drop into the shredder hopper.'],
    safety=['Cut-resistant gloves; contaminated containers (pesticide, oil) are rejected, not washed.'])
M['SH'] = dict(
    specs=[('Type', 'single shaft, 15 hooked knives dia 180 x 10 mm on a 36 A/F hex shaft'), ('Drive', '4 kW gearmotor, about 70 rpm, 450 N.m'), ('Cutting chamber', '220 x 302 mm'),
           ('Screen', 'dia 8 mm perforation'), ('Capacity', '30-50 kg/h HDPE'), ('Feed opening', '700 x 600 mm hopper, 400 mm deep')],
    build=['Weld the frame and deck; weld the cutting chamber SH-210 on a dummy shaft so both bearing bores stay in line.',
           'Bolt the chamber to the deck. Fit the two UCF207 bearings loosely.', 'Build the rotor on the bench: slide knives A, B, C, A ... and spacers alternately on the hex shaft (15 + 15), '
           'then pass the shaft through the chamber and bearings. Centre the stack with 1 mm clearance to each end plate and lock the bearing grub screws.',
           'Fit the two combs on their support angles with the fingers in the spacer gaps, 1 mm side clearance, 2 mm from the spacers; then the screen underneath.',
           'Push the gearmotor on the shaft with the key, fit the torque arm to the deck through rubber bushes.', 'Bolt on hopper flange and hopper, hang the discharge skirt, place the tote.'],
    check=['Turn the rotor one full turn by hand: no knife touches a comb finger or the screen.', 'Run empty 10 min: bearing temperature below 60 C, no knocking.',
           'Feed a jerry can cut in half: flakes below 10 mm, motor current below nameplate.'],
    operate=['Start empty, feed steadily, never over-fill the hopper. Reverse for 2 s if it stalls.', 'Empty the flake tote into the HDPE weigh-hopper stock when two-thirds full.'],
    safety=['Lockable isolator off and padlocked before opening the chamber or removing the tote skirt.', 'Hearing protection (expect 85-90 dB).'])
M['SF'] = dict(
    specs=[('Hopper', '1100 x 1100 mm top, 0.36 m3 (about 550 kg of sand, 3 shifts)'), ('Elevating screw', 'dia 98 flight in 114.3 x 3.6 tube, 45 deg, 0.75 kW, 120 rpm'),
           ('Transfer screw', 'same section, horizontal, 0.37 kW, 90 rpm, 2.09 m headroom over the aisle'), ('Capacity', 'well above the 60 kg/h the dryer needs - run on a timer or level switch')],
    build=['Weld the stand, set it on its pads outside the open side, anchor.', 'Weld the hopper, band, rim angles and grizzly; lower it into the stand and bolt the rim.',
           'Make both screws (see part CM-F98-80 for the flights): flights on the centre pipe, stub shafts pinned in, straighten, slide into the casing, fit end flanges and bearings.',
           'Offer the elevating screw through the feed boot at 45 deg, scribe and weld the boot, bolt the boot to the hopper outlet, support the top end on its post.',
           'Hang the transfer screw from the two roof clamps and its outside post so its inlet stub sits under the elevating screw spout and its long spout drops into the dryer inlet collar.'],
    check=['Both screws turn freely by hand before the motors are fitted.', 'Direction: material moves toward the drive end.', 'Run with dry sand: no leakage at the boot, spout sock in place.'],
    operate=['Keep the hopper topped up by loader. Damp sand above about 8 % moisture bridges - rod it through the grizzly, never by hand.'],
    safety=['Grizzly bars stay welded in. Isolate before clearing a blockage. The loader works outside the posts; no one stands under the bucket.'])
M['DR'] = dict(
    specs=[('Drum', 'dia 400 x 1400 mm, 3 mm shell, 8 lifters'), ('Speed', 'about 5 rpm via friction rollers (0.37 kW, VFD)'), ('Slope', 'adjustable 0-4 deg (2 deg as drawn)'),
           ('Heating', '4.5 kW duct heater + 400 m3/h blower, air at 150-200 C, co-current'), ('Capacity', '60 kg/h from 5 % to below 0.5 % moisture')],
    build=['Weld frame and cradle. Bolt the eight UCP204 units on the risers, fit shafts and rollers (flanged pair at ring No. 2), align both shafts parallel within 0.5 mm.',
           'Roll and weld the drum, fit rings, lifters and dam rings. Lower the drum on the rollers; the rings must sit on all four rollers.',
           'Pin the cradle to the frame at the discharge end; set the slope with the two M20 jack screws at the feed end and lock them.',
           'Fit the gearmotor on the drive shaft with the motor pointing to the back wall, then the insulated cowl on its stays.', 'Fix the feed hood on its posts with the drum mouth 20 mm inside it; bolt heater and blower to the hood front.',
           'Hang the discharge hood on its arms over the screen feed end; connect its top spigot to the dust collector.'],
    check=['Drum turns without walking off: the flanged rollers just touch the ring.', 'Heater cannot switch on without the blower (air-flow interlock) and the drum drive.',
           'Sand leaving the drum feels dry and does not ball in the fist (below 0.5 %).'],
    operate=['Start blower, drum, heater; wait for 120 C outlet air; then start the feed screws. Stop in reverse order and let the drum run 10 min to cool.',
             'Residence time is set by slope and speed: too wet - reduce the slope or the feed rate.'],
    safety=['Hot surfaces under the cowl. Rotating drum: keep the nip between ring and rollers guarded with the side panels (mesh, by fabricator).'])
M['VS'] = dict(
    specs=[('Deck', '430 x 836 mm woven wire, 2.0 mm aperture, 8 deg'), ('Drive', '0.12 kW vibrator, 3000 rpm, on four springs'), ('Products', 'undersize sand to tote below; stones and oversize off the front into a bucket')],
    build=['Weld the frame and the screen box; fit mesh between support flats and clamp strips, pulled tight.', 'Stand the box on the four springs, bolt the vibrator on the bridge plate, hang the undersize pan below the deck.',
           'Fit hood posts, bearers and dust hood; connect to the dust collector with flexible duct.'],
    check=['Box moves freely on the springs and touches nothing.', 'Set the vibrator weights so sand travels the deck in 5-10 s.', 'No holes or loose edges in the mesh.'],
    operate=['Check and empty the stones bucket each hour. Swap the sand tote before it overflows.'],
    safety=['Never run without the dust hood connected.'])
M['DC'] = dict(
    specs=[('Fan', '0.75 kW radial, about 1000 m3/h at 1500 Pa'), ('Filter', 'one pleated cartridge dia 325 x 600, about 10 m2, class M'), ('Collection', '30 L sealed bucket')],
    build=['Fold / weld the body and hopper, seal all seams with sealant.', 'Mount the cartridge under the top plate, the fan on top, the door with its gasket.', 'Connect dia 125 flexible ducts from the screen hood and the dryer discharge hood through a Y-branch.'],
    check=['Smoke test at both hoods: smoke is pulled in from 150 mm away.', 'No dust at the fan outlet.'],
    operate=['Rap or pulse the cartridge and empty the bucket (wet the dust first) at the end of each shift.'],
    safety=['Collected dust is fine silica: mask on, bag it damp, do not blow down with compressed air.'])
M['WB'] = dict(
    specs=[('Weigh hoppers', '2 x 29 L stainless, each on a 100 kg single-point load cell'), ('Accuracy', '+/-20 g on a 6.65 kg charge'), ('Gates', 'manual 100 x 100 slide gates'),
           ('Incline screw', 'dia 98, 45 deg, 0.37 kW, lifts the batch 1.2 m into the mixer')],
    build=['Weld the frame; weld hoppers, bands and support plates.', 'Bolt each load cell to the rear rail on its spacer (arrow on the cell pointing down), then the hopper tongue to the free end. '
           'Check nothing else touches the hopper - not the frame, not a cable.', 'Hang the collecting hopper in the middle rails; scribe and weld the inlet chute to the screw casing.',
           'Fit the incline screw with its top post; its spout must sit centrally in the mixer charge collar.', 'Mount the two indicators on the display bar and calibrate with certified test weights (5 and 10 kg).'],
    check=['Indicator returns to zero within 5 g after loading and unloading 10 kg.', 'Corner test: 5 kg placed at each corner of the hopper reads within 20 g.'],
    operate=['Tare. Scoop sand to 6.65 kg, flakes to 2.85 kg (the indicators can show % of target). Add up to 5 % regrind as part of the plastic weight.',
             'With the mixer running and at temperature, start the screw, then open the sand gate, then the flake gate.'],
    safety=['Always weigh - volume scoops drift by 10 % or more with moisture and flake size.'])
M['MX'] = dict(
    specs=[('Drum', 'dia 450 x 320 mm inside, 6 mm S355 wall, 12 mm base'), ('Heating', '3 x 1.7 kW band heaters + 3 kW base heater = 8.1 kW, PID controlled'),
           ('Agitator', 'anchor paddle, 30 rpm, 2.2 kW gearmotor, 630 N.m'), ('Insulation', '50 mm ceramic fibre + stainless cladding'), ('Batch', '9.5 kg, about 12 min to 190 C'),
           ('Fume control', '1000 x 1000 hood, dia 200 duct, 800 m3/h fan through the back wall')],
    build=['Weld the frame and deck. Weld the drum (shell, base, rim flange, nozzle, gate flange, standoffs).', 'Clamp the base heater under the drum, bolt the drum to the deck through ceramic washers.',
           'Fit the three band heaters, thermocouple to the wall, wrap the insulation and screw on the cladding.', 'Bolt the two columns to the deck (the bridge runs at 30 deg to the line so the chute and the batch screw stay clear), weld the bridge on top with its mounting plate, bolt the UCF208 underneath and the gearmotor on top.',
           'Weld the paddle; lower the shaft through gearbox and bearing, bolt the paddle hub on with the cross bolt. Set 3 mm clearance to the floor and 4 mm to the wall.',
           'Fit lids, charge collar, gate blade, chute, guard panel, control panel; hang the hood on its wall brackets and duct it to the fan.'],
    check=['Paddle turns a full revolution by hand without touching.', 'Cold run 10 min; then heat empty to 200 C: both controllers hold +/-5 C, cladding below 60 C.',
           'Lid switch stops the paddle; heaters trip if the fume fan stops.', 'First batch: melt is uniformly dark, no white sand pockets, no smoke.'],
    operate=['Keep the drum hot all shift (set 230 C wall, expect 190-200 C melt). Charge through the rear port with the paddle running.',
             'Mix until the batch pulls into a dough that leaves the wall clean (about 10 min). Lift the gate, let the paddle push out one 4.5 kg portion, close, weigh, mould; repeat.',
             'At the end of shift discharge everything; a cold plug is very hard to remove.'],
    safety=['200 C surfaces and melt: gloves, face shield, apron. Never add wet sand - steam throws hot material out.', 'Keep below 230 C; if white acrid fume appears, stop heating and ventilate: there is PVC in the batch.'])
M['RC'] = dict(
    specs=[('Transfer height', '885 mm (top of rollers = top of press lower bolster)'), ('Rollers', 'dia 50 x 900 gravity rollers at 110 mm pitch'), ('Return line', 'gravity rollers at 350 mm under the press for the empty carrier'),
           ('Dough station', '15 kg x 5 g bench scale with stainless tray at the mixer chute')],
    build=['Weld two roller-table frames, bolt on the roller rails, spring the rollers in.', 'Set the tables either side of the press, tops level with the lower bolster within 1 mm, anchor.',
           'Fit the press-section return rails on the bearers in the press base.', 'Stand the scale shelf under the mixer chute.'],
    check=['A loaded carrier (about 50 kg) rolls from the charge table into the press with one hand.'],
    operate=['Charge both cavities on the infeed table, push in to the end stop, press, flip the stop down, pull out to the outfeed table with the hook.'],
    safety=['Use the hook tool, not hands, on hot carriers.'])
M['HP'] = dict(
    specs=[('Force', '1030 kN at 210 bar (bore 250 mm)'), ('Stroke / daylight', '300 mm / 483 mm bed to platen'), ('Columns', '4 x dia 80 chromed 42CrMo4 at 670 x 960 mm centres'),
           ('Platen', '860 x 1140 mm on bronze bushes'), ('Power unit', '4 kW hi-lo pump: fast approach ~10 mm/s, pressing ~1.7 mm/s'), ('Tooling', '2 punches on the upper bolster; carrier with 2 cavity inserts on spring die-lifters'),
           ('Mass', 'about 3.3 t - spread over the container cross-members with 10 mm floor plates under the feet')],
    build=['Fabricate bed, crown and platen; stress-relieve; machine faces; line-bore the column holes of all three stacked together.',
           'Stand the base frame on the floor plates, level within 0.5 mm/m, anchor through the floor to the container cross-members.',
           'Lower the bed on the base and bolt it. Stand the four columns in the bed with their lower nuts, slide the platen (bushes greased) down onto blocks.',
           'Lower the crown onto the column shoulders, fit the top nuts and tighten in a cross pattern (2000 N.m or hydraulic tensioner).',
           'Lift the cylinder up through the crown from below so its head flange bears under the crown bottom plate; 8 x M20 10.9. Screw the rod flange on and bolt it to the platen.',
           'Mount the power unit on the crown, pipe it, fill with oil, bleed. Bolt lower bolster (with die-lifter bars) and upper bolster with the two punches.',
           'Fit rear guard, light curtains, two-hand console and gauge.'],
    check=['Platen parallel to bed within 0.15 mm over 800 mm at three heights.', 'Pressure test at 230 bar for 10 min: no leaks, no creep with the pilot check holding.',
           'Light curtain and two-hand control each stop the down-stroke; stopping time measured and the safety distance confirmed.',
           'Clay test in each cavity: 8.0 +/-0.3 mm wall everywhere, lands closing together.'],
    operate=['See the moulding sheet TL-001. Dwell 60-90 s, then open fully before pulling the carrier.', 'Grease the column bushes weekly; check the column nuts monthly.'],
    safety=['Crush hazard: guards and controls are not optional. Use the safety prop when hands are between the tools.', 'Burst hazard: replace any hose that is kinked, blistered or older than 6 years.'])
M['TL'] = dict(
    specs=[('Tile', '420 x 330 x 8 mm double-roman, 2 nibs, 2.19 kg'), ('Cavity insert', 'A356-T6 aluminium, 470 x 380 x 75, about 18 kg, 10 off'), ('Punch', 'S355 steel, 470 x 380, 2 off'),
           ('Carrier', '540 x 840 x 25 steel tray, 2 off'), ('Shrinkage', 'allow about 1.2 % - measure the first tiles and correct the next tooling')],
    build=['Order of work: punch and one insert first; prove the tile; then cast and machine the other nine inserts.', 'Machine both halves from the STEP files (TL-101, TL-102) - the profile is a free-form surface and is defined only by the model.',
           'Weld the carriers using two finished inserts as the jig.'],
    check=['Insert drops into the carrier pocket freely and has less than 1 mm play.', 'Punch enters each of the ten inserts with 0.3-0.5 mm gap all round.', 'Tile weight 2.1-2.3 kg, wall 8 +/-0.5 mm, lies flat within 3 mm.'],
    safety=['Inserts with a tile weigh about 20 kg and may be at 80-100 C: gloves, two hands on the finger grooves, short carry only.'])
M['CR'] = dict(
    specs=[('Shelves', '4 levels at 450 / 800 / 1150 / 1500 mm, 2 inserts each'), ('Cooling', 'ambient air from the dia 500 wall fan directly behind'), ('Frame', '560 x 900 x 1800 mm')],
    build=['Weld the frame with the eight runners square and parallel (inserts must slide).', 'Anchor to the floor and tie the top to the container wall.'],
    check=['An insert slides to the back stop and out again on every shelf.'],
    operate=['Fill from the bottom shelf up; chalk the time on the shelf. Release when the tile is loose in the cavity (below about 60 C).', 'Return the empty insert to the carrier on the infeed side.'],
    safety=['Top shelf loading is at shoulder height - lighter or taller operators use only the lower three.'])
M['TR'] = dict(
    specs=[('Table', '850 x 700 x 850 mm, white steel top'), ('Trim tool', '0.75 kW spindle with dia 12 carbide burr, foot switch'), ('Guard', '600 x 450 x 380 polycarbonate enclosure, 180 mm front opening'),
           ('Regrind', 'offcuts fall through the funnel into a 60 L tote')],
    build=['Weld frame and guard frame, fit top, funnel, spindle, fence and panels.', 'Connect a dia 50 hose from the guard to the dust collector if trimming makes dust.'],
    check=['Burr runs true; guard panels complete; foot switch stops the spindle within 3 s.'],
    operate=['Slide each edge of the tile along the fence past the burr. Inspect both faces for cracks, voids, short corners and warping; weigh one tile per batch.',
             'Good tiles to the pallet; rejects into the tote with the offcuts - they go back through the shredder into the next batches (max 5 % per batch).'],
    safety=['Eye protection even with the guard. Composite dust is abrasive: do not blow it off, vacuum it.'])
M['FG'] = dict(specs=[('Pallet', '1200 x 1000 mm, 100 tiles = 220 kg per shift')], build=['Stack tiles flat in interlocked stacks of 10, three stacks per layer.'], check=['Count 100, label with date, batch numbers and recipe.'])
M['EL'] = dict(
    specs=[('PV', '36 x 550 W in 3 strings of 12 (about 500 V, 13 A each)'), ('Inverter', '20 kW 3-phase hybrid, generator input'), ('Battery', '40.96 kWh LiFePO4, 51.2 V'),
           ('Connected load', 'about 27 kW; expected simultaneous demand 15-18 kW'), ('Daily energy', 'about 75 kWh used vs. about 77 kWh generated at 5 peak sun hours')],
    build=['Mount the battery cabinet on a steel plinth at the right-hand end, inverter on the back wall, distribution board on the end wall.', 'Run PV strings from the combiner on the canopy to the inverter in conduit.',
           'One circuit and isolator per machine from the board; E-stop loop through every station.', 'Bond container, canopy, every frame and the generator to the earth bar.'],
    check=['Insulation resistance and earth continuity tested and recorded.', 'RCD trip test; E-stop loop test at every button.', 'Inverter transfers to generator and back without tripping machines.'],
    operate=['Schedule mixing and pressing between 09:30 and 15:30 when the sun is strongest; shred and dry sand outside those hours from the battery if needed.'],
    safety=['Work on PV and battery circuits only by a qualified electrician: 500 V DC does not let go.'])
M['SC'] = dict(
    specs=[('Array', '6 columns x 6 rows landscape, 13.77 x 6.90 m, 10 deg tilt'), ('Frames', '4 portal frames at 4.6 m: posts SHS 150 x 150 x 5, rafters RHS 200 x 100 x 5'),
           ('Purlins', '7 lines RHS 120 x 60 x 3 at 1154 mm pitch'), ('Clear height', '3.1 m at the rear, 4.1 m at the front'), ('Design loads assumed', '0.25 kN/m2 dead, 1.0 kN/m2 wind - verify locally')],
    build=['Set out footings from the container corner; cast in or drill anchors.', 'Shop-weld base and cap plates to posts, cleats to rafters. Hot-dip galvanise or paint (primer + 2 coats).',
           'Erect posts plumb, bolt rafters, fit knee braces and rod bracing, then purlins.', 'Lay modules from the low edge upward, mid-clamps between rows on each purlin, end-clamps at the outer edges; torque clamps to the module maker\'s figure.',
           'Wire strings, bond every row to earth.'],
    check=['Posts plumb within 5 mm; rafter tops in one plane within 10 mm.', 'String open-circuit voltage within 3 % of each other before connecting.'],
    safety=['Work at height: scaffold tower or lift, harness on the rafters. Modules are live in daylight - cover or keep connectors apart until commissioning.'])
M['TT'] = dict(
    specs=[('Method', 'three-point bending, supports 280 mm apart, load at mid-span across the full tile width'), ('Load', '5 t hand-pump ram with gauge (or 20 kN load cell)'), ('Record', 'breaking load, where it broke, recipe, date')],
    build=['Weld the frame; set the support beam and saddles; hang the ram from the top beam with the nose holder on its rod.'],
    check=['Supports parallel and level; gauge calibrated against a known load.'],
    operate=['Rest the tile weather-side up on the two bars, bring the nose down on the roll crowns, pump steadily (about 10 s per kN) until it breaks.',
             'Test 5 tiles per recipe, at least 7 days after moulding. Also soak 24 h and re-test, and leave samples in the sun for creep and warping.'],
    safety=['Stand to the side; fragments can fly.'])


def md_escape(s):
    return str(s).replace('|', '/')


def make(root):
    from .drawing import find_holes, holes_text
    for pn, p in PARTS.items():
        if getattr(p, 'holes_txt', None) is None:
            try:
                p.holes_txt = [' | '.join(r) for r in holes_text(find_holes(p.shape()))] if p.kind != 'buy' else []
            except Exception:
                p.holes_txt = []
    q = export.plant_qty()
    extra = dict(basis=BASIS, energy=ENERGY, validate=VALIDATE, deviations=DEVIATIONS, safety=SAFETY, workshop=WORKSHOP, sequence=SEQUENCE,
                 narrative=M, procname=PROC_NAME)
    data = export.export_data(root, extra)
    # ---------------- written guide (Markdown)
    L = []
    A = L.append
    A('# Solar plastic-sand roof tile microfactory - manufacturing and assembly guide\n')
    A('Generated from the CAD model in `cad_source/`. Every part number below has a STEP solid, an STL mesh, a drawing sheet and (for plate / sheet parts) a DXF profile.\n')
    A('> **Status: concept design.** The source video itself says "a concept layout, not a finished machine drawing". Sizes, forces, temperatures, structure and electrics here are first-pass engineering '
      'and must be validated by qualified engineers before anything is built or operated. See section 3.\n')
    A('## 1. Design basis\n')
    A('| Item | Value |\n|---|---|')
    for k, v in BASIS:
        A(f'| {k} | {md_escape(v)} |')
    A('\n### Energy per shift (estimate)\n')
    A('| Consumer | Basis | kWh |\n|---|---|---|')
    for k, b, v in ENERGY:
        A(f'| {k} | {b} | {v} |')
    A(f'| **Total** | | **{sum(e[2] for e in ENERGY):g}** |')
    A('\nPV yield at 5 peak sun hours: 19.8 kWp x 5 h x 0.78 = about 77 kWh per day.\n')
    A('## 2. Where this design differs from the video\n')
    for d in DEVIATIONS:
        A(f'- {d}')
    A('\n## 3. Still to be validated (from the video\'s own checklist)\n')
    for k, v in VALIDATE:
        A(f'- **{k}** - {v}')
    A('\n## 4. Safety\n')
    for s in SAFETY:
        A(f'- {s}')
    A('\n## 5. Workshop needed\n')
    for k, v in WORKSHOP:
        A(f'- **{k}:** {v}')
    A('\n## 6. Build sequence\n')
    for i, s in enumerate(SEQUENCE):
        A(f'{i + 1}. {s}')
    A('\n## 7. Machines\n')
    for a, pos in plant.MACHINES:
        n = M.get(a.code, {})
        c = a.counts()
        A(f'\n### {a.code} - {a.name}\n')
        A(a.desc + '\n')
        A(f'Drawing set: `drawings/{a.code}_drawing_set.pdf` - assembly model: `models/step/assemblies/{a.code}.step` - '
          f'{len(c)} unique parts, {sum(c.values())} pieces.\n')
        if n.get('specs'):
            A('| Specification | Value |\n|---|---|')
            for k, v in n['specs']:
                A(f'| {k} | {md_escape(v)} |')
            A('')
        for title, key in (('Build and assembly', 'build'), ('Checks before use', 'check'), ('Operation', 'operate'), ('Safety', 'safety')):
            if n.get(key):
                A(f'**{title}**\n')
                for i, s in enumerate(n[key]):
                    A(f'{i + 1}. {s}')
                A('')
        subs = [s for s in ASMS.values() if s.kind == 'weldment' and any(pn.startswith(a.code + '-') for pn in s.counts()) and s.code.startswith(a.code)]
        for s in subs:
            A(f'**Weldment {s.code} - {s.name}:** {s.weld}\n')
        A('**Parts**\n')
        A('| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |\n|---|---|---|---|---|---|---|---|')
        for pn, nq in c.items():
            p = PARTS[pn]; kg = p.kg()
            A(f'| {pn} | {md_escape(p.name)} | {nq} | {"buy" if p.kind == "buy" else "make"} | {p.mat} | {md_escape(p.stock)[:60]} | {PROC_NAME.get(p.proc, p.proc)} | {"" if kg is None else f"{kg:.2f}"} |')
        if HARDWARE.get(a.code):
            A('\n**Hardware and consumables**\n')
            for d, nq in HARDWARE[a.code]:
                A(f'- {nq} x {d}')
        for sc, rows in HARDWARE.items():
            if sc != a.code and sc.startswith(a.code + '-'):
                for d, nq in rows:
                    A(f'- ({sc}) {nq} x {d}')
    A('\n## 8. How to make each part\n')
    A('Parts are listed by number. Positions in hole tables on the drawings are measured from the minimum-X, minimum-Y, minimum-Z corner of the part as drawn.\n')
    for pn in sorted(PARTS):
        p = PARTS[pn]
        kg = p.kg(); bb = p.bbox()
        A(f'\n#### {pn} - {p.name}\n')
        A(f'- **Quantity in plant:** {q.get(pn, 0)} - **{("Purchased" if p.kind == "buy" else "Made in-house")}** - {PROC_NAME.get(p.proc, p.proc)}')
        A(f'- **Material / stock:** {p.mat} - {p.stock}')
        A(f'- **Envelope:** {bb[0]:.0f} x {bb[1]:.0f} x {bb[2]:.0f} mm' + ('' if kg is None else f' - **mass** {kg:.2f} kg'))
        if p.dims:
            A('- **Key dimensions:** ' + '; '.join(f'{k}: {v}' for k, v in p.dims.items()))
        fl = f'`models/step/parts/{pn}.step`, `models/stl/{pn}.stl`, `drawings/parts/{pn}.svg`' + (f', `models/dxf/{pn}.dxf`' if getattr(p, 'has_dxf', False) else '')
        A(f'- **Files:** {fl}')
        if p.spec:
            A(f'- **Purchase specification:** {p.spec}')
        if p.notes:
            A(f'- **Notes:** {p.notes}')
        for i, s in enumerate(getattr(p, 'route_final', []) or []):
            A(f'  {i + 1}. {s}')
    with open(f'{root}/docs/Manufacturing_Guide.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    return data
