# Solar plastic-sand roof tile microfactory - manufacturing and assembly guide

Generated from the CAD model in `cad_source/`. Every part number below has a STEP solid, an STL mesh, a drawing sheet and (for plate / sheet parts) a DXF profile.

> **Status: concept design.** The source video itself says "a concept layout, not a finished machine drawing". Sizes, forces, temperatures, structure and electrics here are first-pass engineering and must be validated by qualified engineers before anything is built or operated. See section 3.

## 1. Design basis

| Item | Value |
|---|---|
| Product | Double-roman roof tile 420 x 330 mm, 8 mm wall, 2.2 kg (model: 2.19 kg at 1.72 g/cm3) |
| Output | 100 tiles per 8 h shift = 220 kg of finished product |
| Starting recipe | 70 % dry screened sand + 30 % HDPE flakes, by weight (to be tuned by testing) |
| Raw material per shift | about 162 kg sand and 69 kg HDPE including 5 % flash and rejects, which are re-ground and reused |
| Batch | 9.5 kg = 6.65 kg sand + 2.85 kg HDPE = 4 tiles; 25 batches per shift, one every 15-16 min |
| Press cycle | 2 tiles per cycle, 50 cycles per shift; 60-90 s under pressure; 1030 kN at 210 bar = 3.7 MPa on the tiles |
| Cooling | about 20 min in the cavity insert on the rack; 10 inserts in rotation |
| Melt temperature | 180-200 C in the mixer (HDPE melts at ~130 C; keep below 230 C to avoid fumes and degradation) |
| Footprint | one 40 ft high-cube container (12.03 x 2.35 x 2.69 m inside) under a 13.8 x 6.9 m solar canopy |
| Power | 36 x 550 W = 19.8 kWp PV, 20 kW hybrid inverter, 40 kWh LiFePO4 battery, 20 kVA backup generator |
| Crew | 2 operators on the line (prep + mixing, pressing + finishing) plus yard / loader help |

### Energy per shift (estimate)

| Consumer | Basis | kWh |
|---|---|---|
| Mixer heaters (8.1 kW) | 25 batches x ~1.15 kWh | 29 |
| Sand dryer heater + blower (4.7 kW) | 2.7 h | 13 |
| Hydraulic power unit (4 kW) | 25 % duty over 6.5 h | 6.5 |
| Shredder (4 kW) | 2 h at 60 % load | 5 |
| Wall fans + fume fan (0.85 kW) | 8 h | 7 |
| Dust collector (0.75 kW) | 3 h | 2.5 |
| Agitator (2.2 kW) | 5 h at 50 % load | 5.5 |
| Screws, vibrator, trim spindle | intermittent | 3 |
| Lighting and controls | 8 h | 3.5 |
| **Total** | | **75** |

PV yield at 5 peak sun hours: 19.8 kWp x 5 h x 0.78 = about 77 kWh per day.

## 2. Where this design differs from the video

- Handing: the model is laid out as a mirror image of the video. Standing at the open side, material flows from right (sorting) to left (finished tiles); in the video it runs left to right. The process and every machine are the same - mirror the layout on site if the other hand suits your yard better.
- Sand feed: the video shows one tube from the outside hopper to the dryer. A single tube at that height would block the walking aisle, so the model uses a 45 deg elevating screw outside plus a horizontal transfer screw that crosses the aisle overhead with 2.09 m headroom.
- Weigh hoppers are filled by hand scoop from the sand and flake totes. The two overhead feed spouts in the video are left out (they would need two more conveyors and day bins); they can be added later.
- Moulds: a steel carrier holds two separate cast-aluminium cavity inserts. Each insert (about 18 kg + tile) is lifted to the rack by hand; a one-piece two-cavity steel mould would weigh over 140 kg and need a hoist.
- The mixer stands 250 mm higher than drawn in the video so the melt discharges at table height onto the dough scale.
- The container roof is kept (the video removes it only to show the inside). The open long side gets a welded header beam and three posts.
- The hydraulic power unit sits on the press crown; the press is 1.0 m wide along the line with the two cavities one behind the other.
- The canopy is drawn as 6 x 6 modules in landscape (13.8 x 6.9 m) on four portal frames.
- People, the skid-steer loader, the house and the landscaping are not modelled.

## 3. Still to be validated (from the video's own checklist)

- **Recipe** - Mould test tiles at 60/40, 65/35, 70/30 and 75/25 sand/HDPE. Break five of each on the test rig and compare with your local tile standard. Sand grading and plastic grade change the answer.
- **Heating temperatures** - Find the lowest melt temperature that still wets every grain (start at 190 C). Log wall and melt thermocouples; confirm the 8 kW heaters reach it in the 12 min batch time.
- **Press force** - The 1000 kN / 3.7 MPa figure is an estimate. Check tiles for voids and short corners at 100, 150 and 210 bar and set the relief valve at the lowest pressure that gives sound tiles.
- **Cooling time** - Measure when a tile releases without warping (target 20 min). This fixes how many inserts you really need.
- **Structure** - The press crossheads, columns, canopy and the cut container need checking by a structural / mechanical engineer for your steel grades, wind zone and soil. Calculations here are first-pass sizing only.
- **Electrical protection** - Cable sizes, breaker ratings, earthing, RCDs, PV string design and battery protection must be designed and signed off by a qualified electrician to the local code.
- **Ventilation** - Measure fume and respirable silica dust at the operator positions with the fans running. Sand dust is a serious lung hazard; molten plastic fume must be extracted at source.

## 4. Safety

- PVC must never reach the shredder or mixer: heated PVC releases hydrogen chloride gas. Train the sorter, keep the red reject bin at the table and do a float test when unsure (HDPE floats in water, PVC and PET sink).
- Silica dust: run the dust collector whenever the dryer and screen run; wear P3 / N99 masks when handling dry sand; damp down spillage instead of dry sweeping.
- Hot work at 200 C: long sleeves, face shield and 250 C contact gloves at the mixer and press. Keep a burns kit and running water within 10 m.
- Press: never bypass the two-hand control or light curtain. Fit the mechanical safety prop before reaching between the platens for tool changes. Hoses rated 280 bar minimum.
- Shredder: the hopper is deep enough that hands cannot reach the knives; never stand on anything to reach in. Lock off the isolator before clearing a jam. Reversing starter recommended.
- Mixer: lid interlock stops the paddle; discharge only with the guard closed. Fume hood fan interlocked with the heaters.
- Electrical: battery cabinet on a non-combustible plinth, 1 m clear, CO2 extinguisher beside it. All frames bonded to earth. E-stops at every station in one loop.
- Housekeeping: the 1.0 m aisle stays clear; one-way flow from raw material to finished tiles; plastic stock stored away from the mixer.

## 5. Workshop needed

- **Cutting:** Band saw or cold saw for sections up to 200 x 100; plasma cutter; access to a laser / waterjet shop for the DXF plate parts (about 137 profiles)
- **Forming:** Three-roll bender for 3-6 mm plate up to 1.5 m wide; press brake or box folder for 1.5-3 mm sheet
- **Welding:** MAG 250 A (135) for structural work, TIG for stainless sheet; flat welding table 2 x 1 m; clamps and squares
- **Machining:** Centre lathe 1.6 m between centres with steady (press columns); milling machine; access to a horizontal borer for the press crossheads and a 3-axis CNC mill 600 x 500 for the mould
- **Other:** Pillar drill, magnetic drill, taps and dies to M20, torque wrench to 400 N.m, 2 t chain block or forklift, laser level

## 6. Build sequence

1. Site: cast six container pads and eight canopy footings; lay the earth electrode. Let concrete cure 7 days.
2. Canopy first (it gives shade and power for the rest of the build): posts, rafters, purlins, modules, combiner; then inverter, battery and distribution board on temporary mounts.
3. Container: set level, weld in header and posts, cut the side, cut wall openings, paint, floor coating, lights, fans, louvres, cable tray.
4. Fabricate all frames (the cut list CSV groups members by section), prime and paint.
5. Build the simple machines first to train the team: sorting table, cooling rack, roller tables, trim station, dust collector.
6. Screw conveyors (three use the same flights, bearings and stub shafts), then the receiving hopper, weigh batcher and vibrating screen.
7. Rotary dryer, shredder, mixer.
8. Press: crossheads fabricated, stress-relieved and bored together; columns turned as a matched set; assemble on the base frame, fit cylinder and power unit, pressure-test at 1.1 x working pressure.
9. Mould tooling: pattern, castings, CNC machining, trial fit in the press with modelling clay to check the 8 mm wall.
10. Place machines to the plant datums (drawing set PLANT), anchor, wire, bond, test every E-stop, then commission station by station with material.
11. Run the validation programme with the test rig before any tile is sold.

## 7. Machines


### CT - Container shell conversion (40 ft high-cube)

One long side wall is cut out and replaced by a welded header beam on three posts. The back wall gets three dia 500 exhaust fans, four intake louvres and the mixer fume duct. LED lighting under the roof.

Drawing set: `drawings/CT_drawing_set.pdf` - assembly model: `models/step/assemblies/CT.step` - 9 unique parts, 27 pieces.

| Specification | Value |
|---|---|
| Container | ISO 40 ft high-cube, 12.19 x 2.44 x 2.90 m |
| Clear side opening | 12.03 m x 2.49 m high |
| Header | RHS 200 x 100 x 6 on 3 posts SHS 100 x 100 x 5 at 3.0 m centres |
| Ventilation | 3 x dia 500 wall fans (about 18 000 m3/h total, > 60 air changes/h) + 4 louvres |
| Lighting | 6 x 50 W LED battens, target 300 lux |

**Build and assembly**

1. Follow the route on sheet CT-001: support, reinforce, then cut. Never cut the side wall before the header and posts are welded in - the wall is part of the container structure.
2. Fit louvres from outside on a bead of sealant, fans from inside with their shutters outside.
3. Hang the LED battens on the roof bows at 1.3 m from the back wall, above the machine fronts.
4. Fix the cable tray along the back wall at 2.55 m.

**Checks before use**

1. Diagonals of the open side within 5 mm after cutting.
2. Roof does not pond water; no daylight through the weld seams.
3. Every opening has no sharp edges.

**Safety**

1. A cut container has lost its racking strength: do not lift or transport it without re-bracing the open side.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| CT-001 | 40 ft high-cube container, modified | 1 | buy | Purchased | ISO 1AAA container 12.19 x 2.44 x 2.90 m, cargo-worthy | Purchased + modified on site | 3900.00 |
| CT-002 | Container roof (part of CT-001, kept) | 1 | buy | Purchased | part of container | Purchased item | 0.00 |
| CT-101 | Front header beam | 1 | make | S355J2 | RHS 200x100x6 | Saw to length | 326.42 |
| CT-103 | Post end plate | 6 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 3.09 |
| CT-102 | Front opening post | 3 | make | S355J2 | SHS 100x100x5 | Saw to length | 35.95 |
| CT-201 | Weather louvre 500 x 400 | 4 | buy | Purchased | Aluminium weather louvre 500 x 400 with insect mesh, flanged | Purchased item | 3.00 |
| CT-202 | Wall axial fan dia 500 | 3 | buy | Purchased | Plate-mounted axial exhaust fan dia 500, approx. 6000 m3/h,  | Purchased item | 9.00 |
| CT-203 | LED batten 1500 mm, 50 W | 6 | buy | Purchased | IP65 LED batten 1.5 m, 50 W, 4000 K, approx. 6500 lm (target | Purchased item | 2.00 |
| CT-204 | Fire extinguisher 6 kg ABC + CO2 2 kg set | 2 | buy | Purchased | 6 kg ABC powder + 2 kg CO2 extinguisher, wall brackets, sign | Purchased item | 12.00 |

**Hardware and consumables**

- 6 x Concrete pad 600 x 600 x 300 (container supports)
- 1 x Epoxy floor paint, 30 m2 two coats + yellow line paint
- 1 x First-aid kit, burns kit and eyewash station
- 1 x Angle 30x30x3 for louvre frames, 8 m

### ST - Station 1a - Sorting table

Hand sorting of incoming plastic. Only HDPE (resin code 2) goes on to the shredder.

Drawing set: `drawings/ST_drawing_set.pdf` - assembly model: `models/step/assemblies/ST.step` - 7 unique parts, 18 pieces.

| Specification | Value |
|---|---|
| Table | 900 x 600 x 850 mm, HDPE top |
| Bins | red = reject (PVC, PET, PP, unknown), green = HDPE only |

**Build and assembly**

1. Weld frame ST-100, paint, screw the top on.
2. Anchor against the back wall next to the shredder.

**Checks before use**

1. Top is level and does not rock.

**Operation**

1. Tip the incoming sack on the table. Keep only items marked 2 / HDPE (jerry cans, crates, bottle caps, detergent bottles). Remove labels, metal and dirt.
2. Cut pieces larger than 250 mm with a hand saw so they drop into the shredder hopper.

**Safety**

1. Cut-resistant gloves; contaminated containers (pesticide, oil) are rejected, not washed.

**Weldment ST-100 - Sorting table frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| ST-101 | Sorting table frame - leg | 4 | make | S235JR | SHS 40x40x2.5 | Saw to length | 2.42 |
| ST-104 | Sorting table frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.47 |
| ST-102 | Sorting table frame - long rail | 3 | make | S235JR | SHS 40x40x2.5 | Saw to length | 2.41 |
| ST-103 | Sorting table frame - cross rail | 4 | make | S235JR | SHS 40x40x2.5 | Saw to length | 1.53 |
| ST-201 | Sorting table top | 1 | make | HDPE | HDPE board 20 mm | Cut to size (saw/router) | 11.43 |
| ST-301 | Reject bin 80 L, red | 1 | buy | Purchased | 80 L rigid PP bin, RED, labelled "PVC / PET / unknown - REJE | Purchased item | 3.50 |
| ST-302 | HDPE bin 80 L, green | 1 | buy | Purchased | 80 L rigid PP bin, GREEN, labelled "HDPE only" | Purchased item | 3.50 |

**Hardware and consumables**

- 8 x M6x50 countersunk screw + rivet nut
- 8 x M12x100 floor anchor / through bolt

### SH - Station 1b - Low-speed shredder

Single-shaft, 15-knife low-speed shredder. 4 kW, ~70 rpm, 8 mm screen. 30-50 kg/h HDPE flakes.

Drawing set: `drawings/SH_drawing_set.pdf` - assembly model: `models/step/assemblies/SH.step` - 26 unique parts, 71 pieces.

| Specification | Value |
|---|---|
| Type | single shaft, 15 hooked knives dia 180 x 10 mm on a 36 A/F hex shaft |
| Drive | 4 kW gearmotor, about 70 rpm, 450 N.m |
| Cutting chamber | 220 x 302 mm |
| Screen | dia 8 mm perforation |
| Capacity | 30-50 kg/h HDPE |
| Feed opening | 700 x 600 mm hopper, 400 mm deep |

**Build and assembly**

1. Weld the frame and deck; weld the cutting chamber SH-210 on a dummy shaft so both bearing bores stay in line.
2. Bolt the chamber to the deck. Fit the two UCF207 bearings loosely.
3. Build the rotor on the bench: slide knives A, B, C, A ... and spacers alternately on the hex shaft (15 + 15), then pass the shaft through the chamber and bearings. Centre the stack with 1 mm clearance to each end plate and lock the bearing grub screws.
4. Fit the two combs on their support angles with the fingers in the spacer gaps, 1 mm side clearance, 2 mm from the spacers; then the screen underneath.
5. Push the gearmotor on the shaft with the key, fit the torque arm to the deck through rubber bushes.
6. Bolt on hopper flange and hopper, hang the discharge skirt, place the tote.

**Checks before use**

1. Turn the rotor one full turn by hand: no knife touches a comb finger or the screen.
2. Run empty 10 min: bearing temperature below 60 C, no knocking.
3. Feed a jerry can cut in half: flakes below 10 mm, motor current below nameplate.

**Operation**

1. Start empty, feed steadily, never over-fill the hopper. Reverse for 2 s if it stalls.
2. Empty the flake tote into the HDPE weigh-hopper stock when two-thirds full.

**Safety**

1. Lockable isolator off and padlocked before opening the chamber or removing the tote skirt.
2. Hearing protection (expect 85-90 dB).

**Weldment SH-100 - Shredder frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment SH-210 - Cutting chamber:** Clamp both end plates on a dummy shaft through the dia 50 bores so the bearing seats stay co-axial, tack the side plates and flanges, check the 220 inside width with a gauge block, then weld (a4 fillets outside, stitch inside).

**Weldment SH-2600 - Shredder feed hopper:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| SH-101 | Shredder frame - leg | 4 | make | S235JR | SHS 60x60x4 | Saw to length | 5.57 |
| SH-104 | Shredder frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.73 |
| SH-102 | Shredder frame - long rail | 3 | make | S235JR | SHS 60x60x4 | Saw to length | 4.78 |
| SH-103 | Shredder frame - cross rail | 4 | make | S235JR | SHS 60x60x4 | Saw to length | 5.84 |
| SH-201 | Shredder deck plate | 1 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 50.13 |
| SH-211 | Chamber end plate (bearing plate) | 2 | make | S355J2 | Plate 15 mm | Laser / plasma profile cut | 6.88 |
| SH-212 | Chamber side plate | 2 | make | S355J2 | Plate 12 mm | Laser / plasma profile cut | 7.11 |
| SH-213 | Chamber flange (top / bottom) | 2 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 6.31 |
| SH-242 | Comb support angle | 2 | make | S235JR | Angle 40x40x5 | Saw to length | 0.89 |
| SH-221 | Rotor shaft (hex 36 A/F) | 1 | make | C45 | Hexagon bar 36 A/F | Lathe turned | 5.16 |
| SH-231 | Rotary knife, type A (hex at 0 deg) | 5 | make | Hardox 450 | Plate 10 mm | Laser / plasma profile cut | 1.34 |
| SH-234 | Rotor spacer | 15 | make | S355J2 | Plate 10 mm | Laser / plasma profile cut | 0.16 |
| SH-232 | Rotary knife, type B (hex at 20 deg) | 5 | make | Hardox 450 | Plate 10 mm | Laser / plasma profile cut | 1.34 |
| SH-233 | Rotary knife, type C (hex at 40 deg) | 5 | make | Hardox 450 | Plate 10 mm | Laser / plasma profile cut | 1.34 |
| SH-241 | Fixed comb (counter knife) | 2 | make | Hardox 450 | Plate 10 mm | Laser / plasma profile cut | 0.93 |
| SH-251 | Screen, dia 8 perforation | 1 | make | S355J2 | Sheet 4 mm | Cut blank, roll, weld seam | 2.68 |
| CM-UCF207 | Flange bearing unit UCF207 (shaft 35) | 2 | buy | Purchased | UCF207 4-bolt flanged insert bearing unit, bore 35 mm, grub- | Purchased item | 1.50 |
| CM-G400-35-70 | Gearmotor 4 kW, 70 rpm, hollow shaft dia 35 | 1 | buy | Purchased | Shaft-mounted worm/helical gearmotor 4 kW, 400 V 3-ph 50 Hz, | Purchased item | 70.00 |
| SH-281 | Gearmotor torque arm | 1 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 1.10 |
| SH-2601 | Shredder feed hopper - front/back panel | 2 | make | S235JR | Sheet 3 mm | Laser / plasma profile cut | 4.62 |
| SH-2602 | Shredder feed hopper - side panel | 2 | make | S235JR | Sheet 3 mm | Laser / plasma profile cut | 4.95 |
| SH-263 | Hopper flange | 1 | make | S235JR | Plate 6 mm | Laser / plasma profile cut | 3.83 |
| SH-271 | Discharge skirt | 1 | make | DC01 galv. | Sheet 2 mm | Cut blank, fold | 4.99 |
| CM-TOTE60 | Stacking tote 600x400x320 (60 L) | 1 | buy | Purchased | Euro stacking container 600 x 400 x 320 mm, solid walls, PP, | Purchased item | 2.60 |
| SH-291 | Control post | 1 | make | S235JR | SHS 40x40x3 | Saw to length | 1.74 |
| CM-CTRL200 | Local control station 200x300x150 | 1 | buy | Purchased | Steel enclosure IP65 200x300x150 with start/stop, mushroom E | Purchased item | 4.00 |

**Hardware and consumables**

- 12 x M12x40 hex bolt 8.8 + nut + washers (chamber flange to deck, hopper flange)
- 8 x M12x45 hex bolt 8.8 + nyloc nut (UCF207 bearing units)
- 6 x M10x25 socket cap screw 12.9 (comb to support angle)
- 1 x Parallel key 10x8x160
- 8 x M12x100 floor anchor

### SF - Station 2a - Sand receiving hopper and feed screws

0.36 m3 receiving hopper outside the container (loaded by skid-steer), 45 deg elevating screw, overhead transfer screw crossing the aisle at 2.09 m clear height into the dryer inlet.

Drawing set: `drawings/SF_drawing_set.pdf` - assembly model: `models/step/assemblies/SF.step` - 33 unique parts, 154 pieces.

| Specification | Value |
|---|---|
| Hopper | 1100 x 1100 mm top, 0.36 m3 (about 550 kg of sand, 3 shifts) |
| Elevating screw | dia 98 flight in 114.3 x 3.6 tube, 45 deg, 0.75 kW, 120 rpm |
| Transfer screw | same section, horizontal, 0.37 kW, 90 rpm, 2.09 m headroom over the aisle |
| Capacity | well above the 60 kg/h the dryer needs - run on a timer or level switch |

**Build and assembly**

1. Weld the stand, set it on its pads outside the open side, anchor.
2. Weld the hopper, band, rim angles and grizzly; lower it into the stand and bolt the rim.
3. Make both screws (see part CM-F98-80 for the flights): flights on the centre pipe, stub shafts pinned in, straighten, slide into the casing, fit end flanges and bearings.
4. Offer the elevating screw through the feed boot at 45 deg, scribe and weld the boot, bolt the boot to the hopper outlet, support the top end on its post.
5. Hang the transfer screw from the two roof clamps and its outside post so its inlet stub sits under the elevating screw spout and its long spout drops into the dryer inlet collar.

**Checks before use**

1. Both screws turn freely by hand before the motors are fitted.
2. Direction: material moves toward the drive end.
3. Run with dry sand: no leakage at the boot, spout sock in place.

**Operation**

1. Keep the hopper topped up by loader. Damp sand above about 8 % moisture bridges - rod it through the grizzly, never by hand.

**Safety**

1. Grizzly bars stay welded in. Isolate before clearing a blockage. The loader works outside the posts; no one stands under the bucket.

**Weldment SF-100 - Sand hopper stand:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment SF-200 - Sand receiving hopper:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up. Then weld the top band, the rim angles and the grizzly (bars at 90 mm pitch keep stones, roots and hands out of the screw).

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| SF-101 | Sand hopper stand - leg | 4 | make | S235JR | SHS 80x80x4 | Saw to length | 12.71 |
| SF-104 | Sand hopper stand - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.04 |
| SF-102 | Sand hopper stand - long rail | 6 | make | S235JR | SHS 80x80x4 | Saw to length | 10.69 |
| SF-103 | Sand hopper stand - cross rail | 5 | make | S235JR | SHS 80x80x4 | Saw to length | 10.69 |
| SF-201 | Sand receiving hopper - front/back panel | 2 | make | S235JR | Sheet 4 mm | Laser / plasma profile cut | 17.36 |
| SF-202 | Sand receiving hopper - side panel | 2 | make | S235JR | Sheet 4 mm | Laser / plasma profile cut | 17.36 |
| SF-203 | Hopper top band | 4 | make | S235JR | Plate 4 mm | Laser / plasma profile cut | 5.20 |
| SF-204 | Hopper support rim angle | 4 | make | S235JR | Angle 50x50x5 | Saw to length | 4.32 |
| SF-205 | Grizzly bar | 11 | make | S235JR | Round bar dia 12 | Saw to length | 0.98 |
| SF-206 | Grizzly end flat | 2 | make | S235JR | Flat bar 30x5 | Saw to length | 1.30 |
| SF-251 | Flood-feed boot | 1 | make | S235JR | Plate 4 mm | Plate fabrication | 12.49 |
| SF-301 | Elevating screw (45 deg) - casing tube | 1 | make | S235JR | Tube OD114.3 x 3.6 | Saw to length | 33.57 |
| SF-302 | Elevating screw (45 deg) - end flange | 2 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.30 |
| CM-UCF205 | Flange bearing unit UCF205 (shaft 25) | 4 | buy | Purchased | UCF205 4-bolt flanged insert bearing unit, bore 25 mm, grub- | Purchased item | 0.80 |
| SF-303 | Elevating screw (45 deg) - screw centre pipe | 1 | make | S235JR | Tube OD33.7 x 4 | Saw to length | 10.15 |
| SF-304 | Elevating screw (45 deg) - tail stub shaft | 1 | make | C45 | Round bar dia 30 | Lathe turned | 0.53 |
| SF-305 | Elevating screw (45 deg) - drive stub shaft | 1 | make | C45 | Round bar dia 30 | Lathe turned | 0.95 |
| CM-F98-80 | Screw flight segment dia 98/34, pitch 80 | 80 | make | S355J2 | Plate 4 mm | Sectional flight, cut + formed | 0.21 |
| CM-G075-25-120 | Gearmotor 0.75 kW, 120 rpm, hollow shaft dia 25 | 1 | buy | Purchased | Shaft-mounted worm/helical gearmotor 0.75 kW, 400 V 3-ph 50  | Purchased item | 20.00 |
| SF-307 | Elevating screw (45 deg) - outlet spout | 1 | make | S235JR | Sheet 3 mm | Cut blank, fold | 1.10 |
| SF-501 | Elevating screw support post | 1 | make | S235JR | SHS 80x80x4 | Saw to length | 19.59 |
| SF-502 | Post base plate | 2 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 4.83 |
| SF-503 | Post saddle plate | 2 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 1.99 |
| SF-401 | Overhead transfer screw - casing tube | 1 | make | S235JR | Tube OD114.3 x 3.6 | Saw to length | 29.41 |
| SF-402 | Overhead transfer screw - end flange | 2 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.30 |
| SF-403 | Overhead transfer screw - screw centre pipe | 1 | make | S235JR | Tube OD33.7 x 4 | Saw to length | 8.91 |
| SF-404 | Overhead transfer screw - tail stub shaft | 1 | make | C45 | Round bar dia 30 | Lathe turned | 0.53 |
| SF-405 | Overhead transfer screw - drive stub shaft | 1 | make | C45 | Round bar dia 30 | Lathe turned | 0.95 |
| CM-G037-25-90 | Gearmotor 0.37 kW, 90 rpm, hollow shaft dia 25 | 1 | buy | Purchased | Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50  | Purchased item | 12.00 |
| SF-406 | Overhead transfer screw - inlet stub | 1 | make | S235JR | Sheet 3 mm | Cut blank, fold | 1.03 |
| SF-407 | Overhead transfer screw - outlet spout | 1 | make | S235JR | Sheet 3 mm | Cut blank, fold | 3.65 |
| SF-511 | Transfer screw support post | 1 | make | S235JR | SHS 80x80x4 | Saw to length | 21.41 |
| CM-CLAMP114 | Pipe clamp DN100 with M12 hanger rod | 2 | buy | Purchased | Two-piece steel pipe clamp for OD 114.3, M12 boss, with M12  | Purchased item | 1.20 |

**Hardware and consumables**

- 16 x M12x40 hex bolt + nut + washers (hopper rim to stand, boot flange)
- 2 x U-bolt M12 for OD 114 tube
- 16 x M16x150 chemical / wedge anchor into concrete pad (stand and posts)
- (SF-300) 8 x M10x35 hex bolt 8.8 + nyloc nut + 2 washers (bearing units)
- (SF-300) 4 x Spring pin dia 8 x 40 (stub shafts)
- (SF-300) 1 x Parallel key 8x7x90
- (SF-300) 1 x Torque-arm bolt M10x60 + rubber bush
- (SF-400) 8 x M10x35 hex bolt 8.8 + nyloc nut + 2 washers (bearing units)
- (SF-400) 4 x Spring pin dia 8 x 40 (stub shafts)
- (SF-400) 1 x Parallel key 8x7x90
- (SF-400) 1 x Torque-arm bolt M10x60 + rubber bush

### DR - Station 2b - Rotary sand dryer

Dia 400 x 1400 rotary drum on four trunnion rollers, friction driven at ~5 rpm, slope adjustable 0-4 deg, 4.5 kW electric hot-air heater. Dries ~60 kg/h of sand from 5 % to below 0.5 % moisture.

Drawing set: `drawings/DR_drawing_set.pdf` - assembly model: `models/step/assemblies/DR.step` - 42 unique parts, 93 pieces.

| Specification | Value |
|---|---|
| Drum | dia 400 x 1400 mm, 3 mm shell, 8 lifters |
| Speed | about 5 rpm via friction rollers (0.37 kW, VFD) |
| Slope | adjustable 0-4 deg (2 deg as drawn) |
| Heating | 4.5 kW duct heater + 400 m3/h blower, air at 150-200 C, co-current |
| Capacity | 60 kg/h from 5 % to below 0.5 % moisture |

**Build and assembly**

1. Weld frame and cradle. Bolt the eight UCP204 units on the risers, fit shafts and rollers (flanged pair at ring No. 2), align both shafts parallel within 0.5 mm.
2. Roll and weld the drum, fit rings, lifters and dam rings. Lower the drum on the rollers; the rings must sit on all four rollers.
3. Pin the cradle to the frame at the discharge end; set the slope with the two M20 jack screws at the feed end and lock them.
4. Fit the gearmotor on the drive shaft with the motor pointing to the back wall, then the insulated cowl on its stays.
5. Fix the feed hood on its posts with the drum mouth 20 mm inside it; bolt heater and blower to the hood front.
6. Hang the discharge hood on its arms over the screen feed end; connect its top spigot to the dust collector.

**Checks before use**

1. Drum turns without walking off: the flanged rollers just touch the ring.
2. Heater cannot switch on without the blower (air-flow interlock) and the drum drive.
3. Sand leaving the drum feels dry and does not ball in the fist (below 0.5 %).

**Operation**

1. Start blower, drum, heater; wait for 120 C outlet air; then start the feed screws. Stop in reverse order and let the drum run 10 min to cool.
2. Residence time is set by slope and speed: too wet - reduce the slope or the feed rate.

**Safety**

1. Hot surfaces under the cowl. Rotating drum: keep the nip between ring and rollers guarded with the side panels (mesh, by fabricator).

**Weldment DR-100 - Dryer frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment DR-200 - Tilting cradle:** Weld the two rails on the two end beams (square within 1 mm over the diagonals), add the four riser blocks. The riser tops must be co-planar within 0.5 mm - skim them after welding or shim under the bearings.

**Weldment DR-300 - Dryer drum:** Roll and seam-weld the shell, check roundness within 2 mm. Shrink or tack-weld the two riding rings on (ring faces square to the axis within 1 mm) and stitch-weld both sides. Stitch the 8 lifters inside at 45 deg spacing, weld the dam rings in each end.

**Weldment DR-500 - Feed hood:** Tack plates square (check diagonals), stitch-weld outside corners 25 mm every 100 mm, then seal all seams that must be dust tight with a continuous a2 fillet. Dress sharp edges.

**Weldment DR-700 - Discharge hood:** Tack plates square (check diagonals), stitch-weld outside corners 25 mm every 100 mm, then seal all seams that must be dust tight with a continuous a2 fillet. Dress sharp edges.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| DR-101 | Dryer frame - leg | 4 | make | S235JR | SHS 60x60x3 | Saw to length | 4.57 |
| DR-104 | Dryer frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.73 |
| DR-102 | Dryer frame - long rail | 6 | make | S235JR | SHS 60x60x3 | Saw to length | 7.62 |
| DR-103 | Dryer frame - cross rail | 6 | make | S235JR | SHS 60x60x3 | Saw to length | 3.11 |
| DR-105 | Dryer frame - jack cross rail | 1 | make | S235JR | SHS 60x60x3 | Saw to length | 3.11 |
| DR-201 | Cradle rail | 2 | make | S235JR | RHS 80x40x3 | Saw to length | 7.52 |
| DR-202 | Cradle end beam | 2 | make | S235JR | RHS 80x40x3 | Saw to length | 3.22 |
| DR-203 | Bearing riser block | 8 | make | S235JR | RHS 80x40x3 | Saw to length | 0.38 |
| DR-211 | Cradle pivot block | 2 | make | S235JR | Flat bar 30x30 | Milled | 0.43 |
| CM-UCP204 | Pillow block bearing UCP204 (shaft 20) | 8 | buy | Purchased | UCP204 pillow block insert bearing unit, bore 20 mm | Purchased item | 0.65 |
| DR-204 | Trunnion roller (plain) | 2 | make | C45 | Round bar dia 125 | Lathe turned | 4.32 |
| DR-207 | Trunnion roller (flanged, thrust) | 2 | make | C45 | Round bar dia 145 | Lathe turned | 5.52 |
| DR-205 | Drive shaft dia 20 | 1 | make | C45 | Round bar dia 20 h9 bright | Lathe turned | 2.74 |
| DR-206 | Idler shaft dia 20 | 1 | make | C45 | Round bar dia 20 | Saw to length | 2.47 |
| CM-G037-20-22 | Gearmotor 0.37 kW, 22 rpm, hollow shaft dia 20 | 1 | buy | Purchased | Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50  | Purchased item | 12.00 |
| DR-301 | Drum shell | 1 | make | S235JR | Sheet 3 mm | Cut blank, roll, weld seam | 41.12 |
| DR-302 | Riding ring | 2 | make | S355J2 | Flat bar 40x20 | Cut blank, roll, weld seam | 8.29 |
| DR-303 | Lifter flight | 8 | make | S235JR | Angle 30x30x3 | Saw to length | 1.61 |
| DR-304 | Feed-end dam ring | 1 | make | S235JR | Plate 3 mm | Laser / plasma profile cut | 2.13 |
| DR-305 | Discharge-end dam ring | 1 | make | S235JR | Plate 3 mm | Laser / plasma profile cut | 0.98 |
| DR-401 | Insulated drum cowl | 1 | make | DC01 galv. | Sheet 1.5 mm | Cut blank, roll, weld seam | 6.97 |
| DR-402 | Cowl stay | 4 | make | S235JR | Flat bar 30x5 | Cut blank, fold | 0.48 |
| DR-501 | Feed hood - top plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 1.74 |
| DR-502 | Feed hood - bottom plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 2.17 |
| DR-503 | Feed hood - front plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 1.64 |
| DR-504 | Feed hood - back plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 2.15 |
| DR-505 | Feed hood - left plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 3.26 |
| DR-506 | Feed hood - right plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 1.17 |
| DR-510 | Feed inlet collar | 1 | make | DC01 galv. | Sheet 2 mm | Cut blank, fold | 1.53 |
| DR-511 | Feed deflector plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 0.94 |
| DR-512 | Feed hood post | 2 | make | S235JR | SHS 40x40x3 | Saw to length | 0.83 |
| DR-601 | Duct air heater 4.5 kW | 1 | buy | Purchased | Finned electric duct heater 4.5 kW, 400 V 3-ph, 200 x 200 mm | Purchased item | 9.00 |
| DR-602 | Centrifugal blower 0.18 kW | 1 | buy | Purchased | Centrifugal blower 0.18 kW, approx. 400 m3/h at 300 Pa, 200  | Purchased item | 8.00 |
| DR-701 | Discharge hood - top plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 1.69 |
| DR-702 | Discharge hood - front/back plate | 2 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 2.01 |
| DR-703 | Discharge hood - left plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 2.29 |
| DR-704 | Discharge hood - right plate | 1 | make | S235JR | Plate 2 mm | Laser / plasma profile cut | 4.50 |
| DR-711 | Discharge hood support arm | 2 | make | S235JR | Angle 40x40x4 | Saw to length | 0.95 |
| DR-712 | Discharge hood post | 2 | make | S235JR | SHS 40x40x3 | Saw to length | 0.49 |
| DR-801 | Cradle jack screw M20 | 2 | buy | Purchased | M20 x 120 hex set screw 8.8 with 2 nuts (slope adjustment an | Purchased item | 0.40 |
| CM-CTRL200 | Local control station 200x300x150 | 1 | buy | Purchased | Steel enclosure IP65 200x300x150 with start/stop, mushroom E | Purchased item | 4.00 |
| DR-901 | Control post | 1 | make | S235JR | SHS 40x40x3 | Saw to length | 1.39 |

**Hardware and consumables**

- 16 x M10x60 hex bolt + nut (UCP204 to risers)
- 2 x Pin dia 16 x 110 with split pins (cradle pivot)
- 1 x Parallel key 6x6x100
- 8 x M8x12 grub screw (rollers)
- 1 x Mineral wool 25 mm foil faced, 0.6 m2 (cowl lining)
- 1 x PT100 air temperature sensor + PID controller (heater)
- 8 x M12x100 floor anchor

### VS - Station 2c - Vibrating screen

430 x 840 single-deck screen, 2 mm aperture, 8 deg slope, 0.12 kW vibrator. Passes dry sand to a tote, rejects stones and oversize.

Drawing set: `drawings/VS_drawing_set.pdf` - assembly model: `models/step/assemblies/VS.step` - 24 unique parts, 56 pieces.

| Specification | Value |
|---|---|
| Deck | 430 x 836 mm woven wire, 2.0 mm aperture, 8 deg |
| Drive | 0.12 kW vibrator, 3000 rpm, on four springs |
| Products | undersize sand to tote below; stones and oversize off the front into a bucket |

**Build and assembly**

1. Weld the frame and the screen box; fit mesh between support flats and clamp strips, pulled tight.
2. Stand the box on the four springs, bolt the vibrator on the bridge plate, hang the undersize pan below the deck.
3. Fit hood posts, bearers and dust hood; connect to the dust collector with flexible duct.

**Checks before use**

1. Box moves freely on the springs and touches nothing.
2. Set the vibrator weights so sand travels the deck in 5-10 s.
3. No holes or loose edges in the mesh.

**Operation**

1. Check and empty the stones bucket each hour. Swap the sand tote before it overflows.

**Safety**

1. Never run without the dust hood connected.

**Weldment VS-100 - Screen frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment VS-300 - Screen box:** Tack side plates to the back plate and the two cross tubes on a flat table, check square, weld fully. Add the four spring lugs LEVEL with the box tilted 8 deg on packers. All welds continuous - vibration finds every weak joint.

**Weldment VS-3100 - Undersize pan:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Weldment VS-400 - Screen dust hood:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| VS-101 | Screen frame - leg | 4 | make | S235JR | SHS 50x50x3 | Saw to length | 3.06 |
| VS-104 | Screen frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.60 |
| VS-102 | Screen frame - long rail | 3 | make | S235JR | SHS 50x50x3 | Saw to length | 2.21 |
| VS-103 | Screen frame - cross rail | 4 | make | S235JR | SHS 50x50x3 | Saw to length | 3.98 |
| VS-201 | Spring seat | 4 | make | S235JR | Plate 6 mm | Laser / plasma profile cut | 0.30 |
| VS-202 | Compression spring dia 50 x 90 | 4 | buy | Purchased | Compression spring OD 50, wire 6, free length 90, rate appro | Purchased item | 0.30 |
| VS-301 | Screen box side plate | 2 | make | S235JR | Plate 4 mm | Laser / plasma profile cut | 3.96 |
| VS-302 | Screen box back plate | 1 | make | S235JR | Plate 4 mm | Laser / plasma profile cut | 2.03 |
| VS-303 | Screen box cross tube | 2 | make | S235JR | Tube OD33.7 x 3 | Saw to length | 0.98 |
| VS-304 | Deck support flat | 2 | make | S235JR | Flat bar 25x5 | Saw to length | 0.82 |
| VS-307 | Vibrator bridge plate | 1 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 5.50 |
| VS-309 | Spring lug | 4 | make | S235JR | Angle 60x60x6 | Saw to length | 0.43 |
| VS-305 | Screen mesh panel 2 mm aperture | 1 | make | Woven wire 304 | Woven wire cloth, 2.0 mm aperture, 0.9 mm wire | Cut to size | 5.68 |
| VS-306 | Mesh clamp strip | 2 | make | S235JR | Flat bar 25x4 | Saw to length | 0.66 |
| VS-308 | Vibrator motor 0.12 kW | 1 | buy | Purchased | External electric vibrator motor 0.12 kW, 2-pole (3000 rpm), | Purchased item | 6.00 |
| VS-3101 | Undersize pan - front/back panel | 2 | make | DC01 galv. | Sheet 2 mm | Laser / plasma profile cut | 1.72 |
| VS-3102 | Undersize pan - side panel | 2 | make | DC01 galv. | Sheet 2 mm | Laser / plasma profile cut | 1.97 |
| VS-321 | Oversize chute | 1 | make | DC01 galv. | Sheet 2 mm | Cut blank, fold | 1.17 |
| VS-501 | Stones bucket 20 L | 1 | buy | Purchased | Steel bucket 20 L for stones and oversize | Purchased item | 1.50 |
| CM-TOTE60 | Stacking tote 600x400x320 (60 L) | 1 | buy | Purchased | Euro stacking container 600 x 400 x 320 mm, solid walls, PP, | Purchased item | 2.60 |
| VS-401 | Screen dust hood - front/back panel | 2 | make | DC01 galv. | Sheet 1.5 mm | Laser / plasma profile cut | 0.88 |
| VS-402 | Screen dust hood - side panel | 2 | make | DC01 galv. | Sheet 1.5 mm | Laser / plasma profile cut | 0.85 |
| VS-411 | Dust hood post | 4 | make | S235JR | SHS 30x30x2 | Saw to length | 0.56 |
| VS-412 | Dust hood bearer | 2 | make | S235JR | Angle 30x30x3 | Saw to length | 0.81 |

**Hardware and consumables**

- 12 x M6x16 pan-head screw (mesh clamp strips)
- 4 x M10x35 bolt + nyloc + spring washer (vibrator)
- 8 x M8x40 stud (spring location)
- 8 x M12x100 floor anchor

### DC - Station 2d - Cartridge dust collector

0.75 kW fan, ~1000 m3/h, one dia 325 x 600 cartridge (approx. 10 m2). Extracts the screen hood and the dryer discharge hood.

Drawing set: `drawings/DC_drawing_set.pdf` - assembly model: `models/step/assemblies/DC.step` - 16 unique parts, 29 pieces.

| Specification | Value |
|---|---|
| Fan | 0.75 kW radial, about 1000 m3/h at 1500 Pa |
| Filter | one pleated cartridge dia 325 x 600, about 10 m2, class M |
| Collection | 30 L sealed bucket |

**Build and assembly**

1. Fold / weld the body and hopper, seal all seams with sealant.
2. Mount the cartridge under the top plate, the fan on top, the door with its gasket.
3. Connect dia 125 flexible ducts from the screen hood and the dryer discharge hood through a Y-branch.

**Checks before use**

1. Smoke test at both hoods: smoke is pulled in from 150 mm away.
2. No dust at the fan outlet.

**Operation**

1. Rap or pulse the cartridge and empty the bucket (wet the dust first) at the end of each shift.

**Safety**

1. Collected dust is fine silica: mask on, bag it damp, do not blow down with compressed air.

**Weldment DC-100 - Dust collector stand:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment DC-200 - Dust collector body:** Tack plates square (check diagonals), stitch-weld outside corners 25 mm every 100 mm, then seal all seams that must be dust tight with a continuous a2 fillet. Dress sharp edges.

**Weldment DC-300 - Dust hopper:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| DC-101 | Dust collector stand - leg | 4 | make | S235JR | SHS 30x30x2.5 | Saw to length | 1.06 |
| DC-104 | Dust collector stand - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.36 |
| DC-102 | Dust collector stand - long rail | 3 | make | S235JR | SHS 30x30x2.5 | Saw to length | 0.84 |
| DC-103 | Dust collector stand - cross rail | 4 | make | S235JR | SHS 30x30x2.5 | Saw to length | 0.84 |
| DC-201 | Dust collector body - top plate | 1 | make | DC01 galv. | Plate 2 mm | Laser / plasma profile cut | 2.69 |
| DC-202 | Dust collector body - front plate | 1 | make | DC01 galv. | Plate 2 mm | Laser / plasma profile cut | 3.73 |
| DC-203 | Dust collector body - back plate | 1 | make | DC01 galv. | Plate 2 mm | Laser / plasma profile cut | 7.04 |
| DC-204 | Dust collector body - left plate | 1 | make | DC01 galv. | Plate 2 mm | Laser / plasma profile cut | 6.78 |
| DC-205 | Dust collector body - right plate | 1 | make | DC01 galv. | Plate 2 mm | Laser / plasma profile cut | 6.97 |
| DC-210 | Service door | 1 | make | DC01 galv. | Plate 2 mm | Laser / plasma profile cut | 4.27 |
| DC-301 | Dust hopper - front/back panel | 2 | make | DC01 galv. | Sheet 2 mm | Laser / plasma profile cut | 1.03 |
| DC-302 | Dust hopper - side panel | 2 | make | DC01 galv. | Sheet 2 mm | Laser / plasma profile cut | 1.03 |
| DC-304 | Hopper flange ring | 1 | make | DC01 galv. | Plate 3 mm | Laser / plasma profile cut | 1.37 |
| DC-401 | Filter cartridge dia 325 x 600 | 1 | buy | Purchased | Pleated polyester cartridge, OD 325 x 600, approx. 10 m2, fl | Purchased item | 4.00 |
| DC-402 | Centrifugal fan 0.75 kW | 1 | buy | Purchased | Radial fan 0.75 kW 2-pole, approx. 1000 m3/h at 1500 Pa, ver | Purchased item | 22.00 |
| DC-403 | Dust bucket 30 L | 1 | buy | Purchased | Steel dust bucket 30 L with quick-release band clamp | Purchased item | 2.00 |

**Hardware and consumables**

- 8 x M6 wing nut + stud (door)
- 1 x EPDM gasket 20x5, 2.3 m
- 1 x Flexible PU ducting dia 125, 4 m, with 4 hose clamps and one Y-branch 125/125/125

### WB - Station 3 - Weigh batcher

Two 29 L weigh hoppers (sand, HDPE flakes) on single-point load cells with indicators, slide gates, a common collecting hopper and a 45 deg screw that lifts each weighed batch into the mixer. Batch = 6.65 kg sand + 2.85 kg HDPE (70 : 30 by weight).

Drawing set: `drawings/WB_drawing_set.pdf` - assembly model: `models/step/assemblies/WB.step` - 32 unique parts, 98 pieces.

| Specification | Value |
|---|---|
| Weigh hoppers | 2 x 29 L stainless, each on a 100 kg single-point load cell |
| Accuracy | +/-20 g on a 6.65 kg charge |
| Gates | manual 100 x 100 slide gates |
| Incline screw | dia 98, 45 deg, 0.37 kW, lifts the batch 1.2 m into the mixer |

**Build and assembly**

1. Weld the frame; weld hoppers, bands and support plates.
2. Bolt each load cell to the rear rail on its spacer (arrow on the cell pointing down), then the hopper tongue to the free end. Check nothing else touches the hopper - not the frame, not a cable.
3. Hang the collecting hopper in the middle rails; scribe and weld the inlet chute to the screw casing.
4. Fit the incline screw with its top post; its spout must sit centrally in the mixer charge collar.
5. Mount the two indicators on the display bar and calibrate with certified test weights (5 and 10 kg).

**Checks before use**

1. Indicator returns to zero within 5 g after loading and unloading 10 kg.
2. Corner test: 5 kg placed at each corner of the hopper reads within 20 g.

**Operation**

1. Tare. Scoop sand to 6.65 kg, flakes to 2.85 kg (the indicators can show % of target). Add up to 5 % regrind as part of the plastic weight.
2. With the mixer running and at temperature, start the screw, then open the sand gate, then the flake gate.

**Safety**

1. Always weigh - volume scoops drift by 10 % or more with moisture and flake size.

**Weldment WB-100 - Weigh batcher frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment WB-200 - Collecting hopper:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Weldment WB-300 - Weigh hopper:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| WB-101 | Weigh batcher frame - leg | 4 | make | S235JR | SHS 50x50x3 | Saw to length | 6.61 |
| WB-104 | Weigh batcher frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.60 |
| WB-102 | Weigh batcher frame - long rail | 5 | make | S235JR | SHS 50x50x3 | Saw to length | 3.98 |
| WB-103 | Weigh batcher frame - cross rail | 5 | make | S235JR | SHS 50x50x3 | Saw to length | 2.21 |
| WB-201 | Collecting hopper - front/back panel | 2 | make | DC01 galv. | Sheet 2 mm | Laser / plasma profile cut | 3.32 |
| WB-202 | Collecting hopper - side panel | 2 | make | DC01 galv. | Sheet 2 mm | Laser / plasma profile cut | 2.42 |
| WB-251 | Screw inlet chute | 1 | make | S235JR | Sheet 3 mm | Plate fabrication | 1.90 |
| WB-301 | Weigh hopper - front/back panel | 4 | make | AISI 304 | Sheet 2 mm | Laser / plasma profile cut | 1.19 |
| WB-302 | Weigh hopper - side panel | 4 | make | AISI 304 | Sheet 2 mm | Laser / plasma profile cut | 1.19 |
| WB-303 | Weigh hopper band | 8 | make | AISI 304 | Plate 2 mm | Laser / plasma profile cut | 0.72 |
| WB-304 | Weigh hopper support plate | 2 | make | S235JR | Plate 6 mm | Laser / plasma profile cut | 2.91 |
| WB-321 | Slide gate body | 2 | make | AISI 304 | Plate 8 mm | Laser / plasma profile cut | 0.99 |
| WB-322 | Slide gate guide | 4 | make | AISI 304 | Angle 20x20x3 | Saw to length | 0.18 |
| WB-323 | Slide gate blade | 2 | make | AISI 304 | Plate 3 mm | Laser / plasma profile cut | 0.60 |
| WB-402 | Load cell spacer | 4 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 0.15 |
| WB-401 | Single-point load cell 100 kg | 2 | buy | Purchased | Aluminium single-point (platform) load cell, 100 kg, C3, rat | Purchased item | 0.90 |
| WB-501 | Weighing indicator | 2 | buy | Purchased | Weighing indicator with large LED display, set-point output  | Purchased item | 1.20 |
| WB-502 | Display post | 2 | make | S235JR | SHS 30x30x2 | Saw to length | 0.56 |
| WB-503 | Display cross bar | 1 | make | S235JR | SHS 30x30x2 | Saw to length | 1.39 |
| WB-601 | Batch incline screw (45 deg) - casing tube | 1 | make | S235JR | Tube OD114.3 x 3.6 | Saw to length | 19.21 |
| WB-602 | Batch incline screw (45 deg) - end flange | 2 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.30 |
| CM-UCF205 | Flange bearing unit UCF205 (shaft 25) | 2 | buy | Purchased | UCF205 4-bolt flanged insert bearing unit, bore 25 mm, grub- | Purchased item | 0.80 |
| WB-603 | Batch incline screw (45 deg) - screw centre pipe | 1 | make | S235JR | Tube OD33.7 x 4 | Saw to length | 5.87 |
| WB-604 | Batch incline screw (45 deg) - tail stub shaft | 1 | make | C45 | Round bar dia 30 | Lathe turned | 0.53 |
| WB-605 | Batch incline screw (45 deg) - drive stub shaft | 1 | make | C45 | Round bar dia 30 | Lathe turned | 0.95 |
| CM-F98-80 | Screw flight segment dia 98/34, pitch 80 | 24 | make | S355J2 | Plate 4 mm | Sectional flight, cut + formed | 0.21 |
| CM-G037-25-90 | Gearmotor 0.37 kW, 90 rpm, hollow shaft dia 25 | 1 | buy | Purchased | Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50  | Purchased item | 12.00 |
| WB-607 | Batch incline screw (45 deg) - outlet spout | 1 | make | S235JR | Sheet 3 mm | Cut blank, fold | 1.10 |
| WB-701 | Incline screw support post | 1 | make | S235JR | SHS 50x50x3 | Saw to length | 3.89 |
| WB-702 | Support post base plate | 1 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.57 |
| WB-703 | Support post saddle plate | 1 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.22 |
| CM-CTRL200 | Local control station 200x300x150 | 1 | buy | Purchased | Steel enclosure IP65 200x300x150 with start/stop, mushroom E | Purchased item | 4.00 |

**Hardware and consumables**

- 8 x M8x40 socket cap screw (load cells)
- 1 x M10 U-bolt for OD 114 tube
- 2 x Stainless hand scoop 2 L
- 12 x M12x100 floor anchor
- 2 x Shielded load-cell cable gland + junction box
- (WB-600) 8 x M10x35 hex bolt 8.8 + nyloc nut + 2 washers (bearing units)
- (WB-600) 4 x Spring pin dia 8 x 40 (stub shafts)
- (WB-600) 1 x Parallel key 8x7x90
- (WB-600) 1 x Torque-arm bolt M10x60 + rubber bush

### MX - Station 4 - Heated batch mixer

Dia 450 x 320 jacketed drum, 8 kW electric heating (3 band heaters + base heater), anchor paddle at 30 rpm driven by a 2.2 kW gearmotor. One batch = 9.5 kg (4 tiles) melted and mixed at 180-200 C in about 12 minutes.

Drawing set: `drawings/MX_drawing_set.pdf` - assembly model: `models/step/assemblies/MX.step` - 44 unique parts, 75 pieces.

| Specification | Value |
|---|---|
| Drum | dia 450 x 320 mm inside, 6 mm S355 wall, 12 mm base |
| Heating | 3 x 1.7 kW band heaters + 3 kW base heater = 8.1 kW, PID controlled |
| Agitator | anchor paddle, 30 rpm, 2.2 kW gearmotor, 630 N.m |
| Insulation | 50 mm ceramic fibre + stainless cladding |
| Batch | 9.5 kg, about 12 min to 190 C |
| Fume control | 1000 x 1000 hood, dia 200 duct, 800 m3/h fan through the back wall |

**Build and assembly**

1. Weld the frame and deck. Weld the drum (shell, base, rim flange, nozzle, gate flange, standoffs).
2. Clamp the base heater under the drum, bolt the drum to the deck through ceramic washers.
3. Fit the three band heaters, thermocouple to the wall, wrap the insulation and screw on the cladding.
4. Bolt the two columns to the deck (the bridge runs at 30 deg to the line so the chute and the batch screw stay clear), weld the bridge on top with its mounting plate, bolt the UCF208 underneath and the gearmotor on top.
5. Weld the paddle; lower the shaft through gearbox and bearing, bolt the paddle hub on with the cross bolt. Set 3 mm clearance to the floor and 4 mm to the wall.
6. Fit lids, charge collar, gate blade, chute, guard panel, control panel; hang the hood on its wall brackets and duct it to the fan.

**Checks before use**

1. Paddle turns a full revolution by hand without touching.
2. Cold run 10 min; then heat empty to 200 C: both controllers hold +/-5 C, cladding below 60 C.
3. Lid switch stops the paddle; heaters trip if the fume fan stops.
4. First batch: melt is uniformly dark, no white sand pockets, no smoke.

**Operation**

1. Keep the drum hot all shift (set 230 C wall, expect 190-200 C melt). Charge through the rear port with the paddle running.
2. Mix until the batch pulls into a dough that leaves the wall clean (about 10 min). Lift the gate, let the paddle push out one 4.5 kg portion, close, weigh, mould; repeat.
3. At the end of shift discharge everything; a cold plug is very hard to remove.

**Safety**

1. 200 C surfaces and melt: gloves, face shield, apron. Never add wet sand - steam throws hot material out.
2. Keep below 230 C; if white acrid fume appears, stop heating and ventilate: there is PVC in the batch.

**Weldment MX-100 - Mixer frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment MX-210 - Mixing drum:** Weld the shell to the base plate inside and out (full-penetration, the joint sees 200 C and abrasive melt). Dress the inside corner to a smooth R6. Weld the rim flange, discharge nozzle, gate flange and the four standoffs. Pressure is atmospheric - no pressure-vessel code applies, but use low-hydrogen filler and let the drum cool slowly to avoid distortion.

**Weldment MX-310 - Anchor paddle:** Weld hub to bottom blade square to the bore (check with the shaft fitted), then the two side scrapers. Hard-face the leading edges of the bottom blade and scrapers with 2 layers of chromium-carbide electrode - sand is very abrasive.

**Weldment MX-400 - Fume extraction hood:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Weldment MX-510 - Front guard panel:** Mitre or butt the 25 SHS frame, weld, then stitch the mesh to the inside every 100 mm. Powder-coat RAL 1023.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| MX-101 | Mixer frame - leg | 4 | make | S235JR | SHS 60x60x4 | Saw to length | 5.92 |
| MX-104 | Mixer frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.73 |
| MX-102 | Mixer frame - long rail | 4 | make | S235JR | SHS 60x60x4 | Saw to length | 5.49 |
| MX-103 | Mixer frame - cross rail | 4 | make | S235JR | SHS 60x60x4 | Saw to length | 5.49 |
| MX-201 | Mixer deck plate | 1 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 44.44 |
| MX-211 | Drum base plate | 1 | make | S355J2 | Plate 12 mm | Laser / plasma profile cut | 15.79 |
| MX-212 | Drum shell | 1 | make | S355J2 | Sheet 6 mm | Cut blank, roll, weld seam | 21.12 |
| MX-213 | Drum rim flange | 1 | make | S355J2 | Plate 8 mm | Laser / plasma profile cut | 7.18 |
| MX-214 | Drum standoff | 4 | make | S235JR | SHS 40x40x3 | Saw to length | 0.29 |
| MX-215 | Standoff pad | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.39 |
| MX-221 | Discharge nozzle | 1 | make | S355J2 | Plate 6 mm | Plate fabrication | 1.67 |
| MX-222 | Gate flange | 1 | make | S355J2 | Plate 8 mm | Laser / plasma profile cut | 1.65 |
| MX-224 | Gate guide spacer | 2 | make | S235JR | Flat bar 20x7 | Saw to length | 0.16 |
| MX-225 | Gate keeper strip | 2 | make | S235JR | Flat bar 35x5 | Saw to length | 0.21 |
| MX-223 | Discharge gate blade | 1 | make | S355J2 | Plate 6 mm | Laser / plasma profile cut | 1.78 |
| MX-231 | Discharge chute | 1 | make | AISI 304 | Sheet 3 mm | Cut blank, fold | 2.19 |
| MX-601 | Band heater dia 462 x 70, 1.7 kW | 3 | buy | Purchased | Mica or ceramic band heater, ID 462, width 70, 1.7 kW 230 V, | Purchased item | 2.50 |
| MX-602 | Base plate heater dia 340, 3 kW | 1 | buy | Purchased | Cast-in aluminium or mica disc heater OD 340, 3 kW 400 V, cl | Purchased item | 6.00 |
| MX-241 | Insulation cladding | 1 | make | AISI 304 | Sheet 1 mm | Cut blank, roll, weld seam | 5.59 |
| MX-312 | Paddle bottom blade | 1 | make | Hardox 450 | Plate 12 mm | Laser / plasma profile cut | 2.46 |
| MX-313 | Paddle side scraper | 2 | make | Hardox 450 | Flat bar 40x10 | Saw to length | 0.78 |
| MX-314 | Paddle hub | 1 | make | C45 | Round bar dia 70 | Lathe turned | 1.19 |
| MX-311 | Agitator shaft dia 40 | 1 | make | C45 | Round bar dia 40 h9 bright | Lathe turned | 9.32 |
| MX-302 | Column base plate | 2 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 1.96 |
| MX-301 | Bridge column | 2 | make | S235JR | SHS 80x80x4 | Saw to length | 7.46 |
| MX-303 | Mixer bridge beam | 1 | make | S235JR | SHS 100x100x5 | Saw to length | 12.59 |
| CM-UCF208 | Flange bearing unit UCF208 (shaft 40) | 1 | buy | Purchased | UCF208 4-bolt flanged insert bearing unit, bore 40 mm, grub- | Purchased item | 1.90 |
| MX-304 | Gearbox mounting plate | 1 | make | S235JR | Plate 12 mm | Laser / plasma profile cut | 2.08 |
| CM-G220-40-30 | Gearmotor 2.2 kW, 30 rpm, hollow shaft dia 40 | 1 | buy | Purchased | Shaft-mounted worm/helical gearmotor 2.2 kW, 400 V 3-ph 50 H | Purchased item | 45.00 |
| MX-321 | Rear lid with charge port | 1 | make | AISI 304 | Sheet 3 mm | Laser / plasma profile cut | 2.97 |
| MX-322 | Front lid (hinged, inspection) | 1 | make | AISI 304 | Sheet 3 mm | Laser / plasma profile cut | 3.30 |
| MX-323 | Charge collar | 1 | make | AISI 304 | Sheet 2 mm | Cut blank, fold | 0.48 |
| MX-401 | Fume extraction hood - front/back panel | 2 | make | DC01 galv. | Sheet 1.5 mm | Laser / plasma profile cut | 3.53 |
| MX-402 | Fume extraction hood - side panel | 2 | make | DC01 galv. | Sheet 1.5 mm | Laser / plasma profile cut | 3.53 |
| MX-411 | Hood wall bracket | 2 | make | S235JR | Angle 50x50x5 | Saw to length | 3.69 |
| MX-412 | Hood bracket wall plate | 2 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.39 |
| MX-420 | Spiral duct dia 200, vertical | 1 | buy | Purchased | Galvanised spiral duct dia 200 with 250x250-to-dia-200 squar | Purchased item | 3.00 |
| MX-421 | Inline extraction fan dia 200 | 1 | buy | Purchased | Inline duct fan dia 200, approx. 800 m3/h, metal casing, mot | Purchased item | 6.00 |
| MX-511 | Guard frame upright | 2 | make | S235JR | SHS 25x25x2 | Saw to length | 1.01 |
| MX-512 | Guard frame rail | 2 | make | S235JR | SHS 25x25x2 | Saw to length | 1.23 |
| MX-513 | Guard mesh infill | 1 | make | S235JR | Weld mesh 25x25x2.5 | Cut to size | 8.67 |
| MX-702 | Panel post | 1 | make | S235JR | SHS 40x40x3 | Saw to length | 5.23 |
| MX-703 | Panel post foot | 1 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.47 |
| MX-701 | Mixer heater control panel | 1 | buy | Purchased | Wall/post-mounted panel 400x500x200 IP54: 2 x PID temperatur | Purchased item | 18.00 |

**Hardware and consumables**

- 1 x Ceramic-fibre blanket 50 mm, 128 kg/m3, 1.2 m2
- 2 x Thermocouple type K, bayonet, with 3 m lead (1 wall, 1 melt probe through the rear lid)
- 4 x M12x40 bolt + nut + ceramic washer (drum standoffs)
- 8 x M12x40 bolt + nut (bridge columns)
- 1 x M12x90 bolt 10.9 + nyloc nut (paddle hub cross bolt)
- 1 x Parallel key 12x8x160
- 1 x Lid safety limit switch
- 8 x M12x100 floor anchor

### RC - Mould handling - roller tables, return line, charge station

Charge table and outfeed table at the 885 mm transfer height, a lower gravity return line for the empty carrier, and the dough-weighing shelf at the mixer discharge.

Drawing set: `drawings/RC_drawing_set.pdf` - assembly model: `models/step/assemblies/RC.step` - 15 unique parts, 83 pieces.

| Specification | Value |
|---|---|
| Transfer height | 885 mm (top of rollers = top of press lower bolster) |
| Rollers | dia 50 x 900 gravity rollers at 110 mm pitch |
| Return line | gravity rollers at 350 mm under the press for the empty carrier |
| Dough station | 15 kg x 5 g bench scale with stainless tray at the mixer chute |

**Build and assembly**

1. Weld two roller-table frames, bolt on the roller rails, spring the rollers in.
2. Set the tables either side of the press, tops level with the lower bolster within 1 mm, anchor.
3. Fit the press-section return rails on the bearers in the press base.
4. Stand the scale shelf under the mixer chute.

**Checks before use**

1. A loaded carrier (about 50 kg) rolls from the charge table into the press with one hand.

**Operation**

1. Charge both cavities on the infeed table, push in to the end stop, press, flip the stop down, pull out to the outfeed table with the hook.

**Safety**

1. Use the hook tool, not hands, on hot carriers.

**Weldment RC-100 - Roller table frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment RC-200 - Dough scale shelf:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| RC-101 | Roller table frame - leg | 8 | make | S235JR | SHS 40x40x3 | Saw to length | 2.80 |
| RC-104 | Roller table frame - foot plate | 8 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.47 |
| RC-102 | Roller table frame - long rail | 8 | make | S235JR | SHS 40x40x3 | Saw to length | 1.64 |
| RC-103 | Roller table frame - cross rail | 8 | make | S235JR | SHS 40x40x3 | Saw to length | 3.21 |
| RC-111 | Roller rail 550 | 8 | make | S235JR | Angle 40x80x5 | Saw to length | 2.48 |
| CM-ROLL900 | Gravity roller dia 50 x 900 | 21 | buy | Purchased | Steel gravity conveyor roller dia 50 x 1.5, face length 900, | Purchased item | 3.40 |
| RC-121 | Return rail, press section | 2 | make | S235JR | Flat bar 80x5 | Saw to length | 3.42 |
| RC-201 | Dough scale shelf - leg | 4 | make | S235JR | SHS 30x30x2.5 | Saw to length | 1.47 |
| RC-204 | Dough scale shelf - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.36 |
| RC-202 | Dough scale shelf - long rail | 4 | make | S235JR | SHS 30x30x2.5 | Saw to length | 0.39 |
| RC-203 | Dough scale shelf - cross rail | 4 | make | S235JR | SHS 30x30x2.5 | Saw to length | 0.78 |
| RC-255 | Scale shelf top | 1 | make | S235JR | Plate 3 mm | Laser / plasma profile cut | 2.37 |
| CM-SCALE15 | Bench scale 15 kg x 5 g | 1 | buy | Purchased | Stainless bench scale, 15 kg capacity, 5 g resolution, platf | Purchased item | 4.00 |
| RC-251 | Dough tray | 1 | make | AISI 304 | Sheet 2 mm | Cut blank, fold | 2.57 |
| RC-301 | Carrier hook tool | 1 | buy | Purchased | Steel pull hook dia 12 x 700 with T-handle, for moving hot m | Purchased item | 0.80 |

**Hardware and consumables**

- 24 x M12x100 floor anchor
- 24 x M8x25 bolt + nut (roller rails to frames)
- 4 x Heat-resistant gloves, 250 C contact (pairs)

### HP - Station 5 - Two-cavity hydraulic press, 1000 kN

Four-column down-stroking press. Bore 250 cylinder at 210 bar = 1030 kN (3.7 MPa on two tiles). 300 mm stroke, 4 kW power pack on the crown. Two tiles per cycle; the mould carrier rolls in from the charge table and out to the cooling side.

Drawing set: `drawings/HP_drawing_set.pdf` - assembly model: `models/step/assemblies/HP.step` - 39 unique parts, 107 pieces.

| Specification | Value |
|---|---|
| Force | 1030 kN at 210 bar (bore 250 mm) |
| Stroke / daylight | 300 mm / 483 mm bed to platen |
| Columns | 4 x dia 80 chromed 42CrMo4 at 670 x 960 mm centres |
| Platen | 860 x 1140 mm on bronze bushes |
| Power unit | 4 kW hi-lo pump: fast approach ~10 mm/s, pressing ~1.7 mm/s |
| Tooling | 2 punches on the upper bolster; carrier with 2 cavity inserts on spring die-lifters |
| Mass | about 3.3 t - spread over the container cross-members with 10 mm floor plates under the feet |

**Build and assembly**

1. Fabricate bed, crown and platen; stress-relieve; machine faces; line-bore the column holes of all three stacked together.
2. Stand the base frame on the floor plates, level within 0.5 mm/m, anchor through the floor to the container cross-members.
3. Lower the bed on the base and bolt it. Stand the four columns in the bed with their lower nuts, slide the platen (bushes greased) down onto blocks.
4. Lower the crown onto the column shoulders, fit the top nuts and tighten in a cross pattern (2000 N.m or hydraulic tensioner).
5. Lift the cylinder up through the crown from below so its head flange bears under the crown bottom plate; 8 x M20 10.9. Screw the rod flange on and bolt it to the platen.
6. Mount the power unit on the crown, pipe it, fill with oil, bleed. Bolt lower bolster (with die-lifter bars) and upper bolster with the two punches.
7. Fit rear guard, light curtains, two-hand console and gauge.

**Checks before use**

1. Platen parallel to bed within 0.15 mm over 800 mm at three heights.
2. Pressure test at 230 bar for 10 min: no leaks, no creep with the pilot check holding.
3. Light curtain and two-hand control each stop the down-stroke; stopping time measured and the safety distance confirmed.
4. Clay test in each cavity: 8.0 +/-0.3 mm wall everywhere, lands closing together.

**Operation**

1. See the moulding sheet TL-001. Dwell 60-90 s, then open fully before pulling the carrier.
2. Grease the column bushes weekly; check the column nuts monthly.

**Safety**

1. Crush hazard: guards and controls are not optional. Use the safety prop when hands are between the tools.
2. Burst hazard: replace any hose that is kinked, blistered or older than 6 years.

**Weldment HP-100 - Press base frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment HP-200 - Press bed (lower crosshead):** Tack the webs and stiffeners to the 30 mm load plate first, then the sleeves, then close with the second plate. Weld in a balanced back-step sequence (a6 fillets, both sides of every web). Stress-relieve at 580-620 C for 2 h, then machine: both outer faces parallel within 0.1 mm and the four column bores dia 72 H8 line-bored in ONE setting together with the other crosshead so the column centres match within 0.1 mm.

**Weldment HP-300 - Press crown (upper crosshead):** Tack the webs and stiffeners to the 30 mm load plate first, then the sleeves, then close with the second plate. Weld in a balanced back-step sequence (a6 fillets, both sides of every web). Stress-relieve at 580-620 C for 2 h, then machine: both outer faces parallel within 0.1 mm and the four column bores dia 72 H8 line-bored in ONE setting together with the other crosshead so the column centres match within 0.1 mm.

**Weldment HP-500 - Moving platen:** Same sequence and stress relief as the crossheads. After machining both faces parallel, bore the four bush housings dia 100 H7 in the same setting as the bed and crown column bores. Press in the bronze bushes and ream to dia 80 H8.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| HP-101 | Press base frame - leg | 4 | make | S235JR | SHS 100x100x5 | Saw to length | 8.31 |
| HP-104 | Press base frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 1.40 |
| HP-103 | Press base frame - cross rail | 2 | make | S235JR | SHS 100x100x5 | Saw to length | 14.32 |
| HP-102 | Press base frame - long rail | 2 | make | S235JR | SHS 100x100x5 | Saw to length | 11.93 |
| HP-105 | Press base - return conveyor bearer | 2 | make | S235JR | SHS 60x60x4 | Saw to length | 6.75 |
| HP-202 | Bed bottom plate | 1 | make | S355J2 | Plate 20 mm | Laser / plasma profile cut | 157.56 |
| HP-203 | Crosshead main web | 9 | make | S355J2 | Plate 16 mm | Laser / plasma profile cut | 34.97 |
| HP-204 | Crosshead stiffener, outer bay | 12 | make | S355J2 | Plate 12 mm | Laser / plasma profile cut | 4.70 |
| HP-205 | Crosshead stiffener, inner bay | 6 | make | S355J2 | Plate 12 mm | Laser / plasma profile cut | 4.16 |
| HP-206 | Column sleeve | 8 | make | S355J2 | Hollow bar OD 121 x ID 71 | Lathe turned | 13.56 |
| HP-201 | Bed top plate | 1 | make | S355J2 | Plate 30 mm | Laser / plasma profile cut | 236.13 |
| HP-301 | Crown bottom plate | 1 | make | S355J2 | Plate 30 mm | Laser / plasma profile cut | 217.86 |
| HP-303 | Crown centre stiffener | 2 | make | S355J2 | Plate 12 mm | Laser / plasma profile cut | 8.68 |
| HP-304 | Cylinder sleeve ring | 1 | make | S355J2 | Plate 16 mm | Cut blank, roll, weld seam | 32.10 |
| HP-302 | Crown top plate | 1 | make | S355J2 | Plate 20 mm | Laser / plasma profile cut | 145.71 |
| HP-401 | Press column dia 80 | 4 | make | 42CrMo4 | Round bar dia 80, hard-chromed | Lathe turned | 54.11 |
| HP-402 | Column nut M72x4 | 8 | make | C45 | Hexagon bar 105 A/F | Lathe turned | 2.49 |
| HP-501 | Platen bottom plate | 1 | make | S355J2 | Plate 30 mm | Laser / plasma profile cut | 217.97 |
| HP-503 | Platen web | 4 | make | S355J2 | Plate 16 mm | Laser / plasma profile cut | 20.87 |
| HP-504 | Platen end web | 2 | make | S355J2 | Plate 16 mm | Laser / plasma profile cut | 16.20 |
| HP-505 | Bush housing | 4 | make | S355J2 | Hollow bar OD 130 x ID 95 | Lathe turned | 8.51 |
| HP-506 | Column guide bush | 4 | make | Bronze CuSn12 | Cast bronze tube 105/75 | Lathe turned | 4.88 |
| HP-502 | Platen top plate | 1 | make | S355J2 | Plate 20 mm | Laser / plasma profile cut | 145.10 |
| HP-602 | Rod flange | 1 | make | C45 | Plate 40 mm | Lathe turned | 16.15 |
| HP-601 | Hydraulic cylinder 250/180 x 300 | 1 | buy | Purchased | Double-acting cylinder, bore 250, rod 180, stroke 300, 250 b | Purchased item | 430.00 |
| HP-610 | Hydraulic power unit 4 kW | 1 | buy | Purchased | Power pack: 4 kW 400 V motor, hi-lo double pump (approx. 30  | Purchased item | 95.00 |
| HP-701 | Lower bolster with lifter grooves | 1 | make | S355J2 | Plate 30 mm | Milled | 117.32 |
| HP-702 | Spring die-lifter bar 40x24x600 with balls | 2 | buy | Purchased | Spring-loaded ball die lifter for 42 mm groove, 600 long, li | Purchased item | 5.00 |
| HP-703 | Carrier end stop (flip-down) | 1 | make | S355J2 | Flat bar 45x30 | Milled | 2.12 |
| HP-711 | Upper bolster | 1 | make | S355J2 | Plate 30 mm | Milled | 106.03 |
| TL-102 | Punch (upper mould half) | 2 | make | S355J2 | Plate 100 mm | 3-axis CNC surface machined | 84.86 |
| TL-111 | Carrier base plate | 1 | make | S355J2 | Plate 10 mm | Laser / plasma profile cut | 35.55 |
| TL-112 | Carrier long rim bar | 2 | make | S235JR | Flat bar 20x15 | Saw to length | 1.94 |
| TL-113 | Carrier cross rim bar | 3 | make | S235JR | Flat bar 20x15 | Saw to length | 1.11 |
| TL-101 | Cavity insert (lower mould half) | 2 | make | Al A356-T6 | Sand casting, or 5083 tooling plate 80 mm | Sand cast + CNC finish | 18.73 |
| HP-640 | Safety light curtain, 500 mm, type 4 | 2 | buy | Purchased | Type 4 safety light curtain pair (IEC 61496), 500 mm protect | Purchased item | 1.50 |
| HP-650 | Rear fixed guard | 1 | make | S235JR | Weld mesh 25x25x2.5 in 25x25 angle frame | Cut to size | 9.67 |
| HP-630 | Two-hand control console | 1 | buy | Purchased | Two-hand control station type IIIC (ISO 13851) on pedestal,  | Purchased item | 14.00 |
| HP-620 | Pressure gauge 0-400 bar | 1 | buy | Purchased | Glycerine-filled gauge dia 100, 0-400 bar, with gauge isolat | Purchased item | 0.60 |

**Hardware and consumables**

- 8 x M20x110 hex bolt 10.9 + hardened washers (cylinder flange to crown)
- 6 x M20x70 socket cap screw 12.9 (rod flange to platen)
- 12 x M16x50 socket cap screw 12.9 (bolsters)
- 12 x M12x50 socket cap screw 12.9 (punches to upper bolster)
- 1 x M12 shoulder bolt (end stop pivot)
- 2 x Hydraulic hoses 2 x 1/2 in, 280 bar, with fittings
- 1 x Hydraulic oil ISO VG 46, 60 l
- 8 x M16x150 anchor (base frame to floor, through to container cross-members)

### CR - Station 6 - Cooling rack

Four shelves, two cavity inserts per shelf (eight cooling positions). Tiles cool in the insert for about 20 min under the wall fan, then release by shrinkage. With two more inserts in the press, ten inserts keep the press from ever waiting.

Drawing set: `drawings/CR_drawing_set.pdf` - assembly model: `models/step/assemblies/CR.step` - 7 unique parts, 39 pieces.

| Specification | Value |
|---|---|
| Shelves | 4 levels at 450 / 800 / 1150 / 1500 mm, 2 inserts each |
| Cooling | ambient air from the dia 500 wall fan directly behind |
| Frame | 560 x 900 x 1800 mm |

**Build and assembly**

1. Weld the frame with the eight runners square and parallel (inserts must slide).
2. Anchor to the floor and tie the top to the container wall.

**Checks before use**

1. An insert slides to the back stop and out again on every shelf.

**Operation**

1. Fill from the bottom shelf up; chalk the time on the shelf. Release when the tile is loose in the cavity (below about 60 C).
2. Return the empty insert to the carrier on the infeed side.

**Safety**

1. Top shelf loading is at shoulder height - lighter or taller operators use only the lower three.

**Weldment CR-100 - Cooling rack frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| CR-101 | Cooling rack frame - leg | 4 | make | S235JR | SHS 40x40x3 | Saw to length | 6.25 |
| CR-104 | Cooling rack frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.47 |
| CR-102 | Cooling rack frame - long rail | 7 | make | S235JR | SHS 40x40x3 | Saw to length | 1.67 |
| CR-103 | Cooling rack frame - cross rail | 4 | make | S235JR | SHS 40x40x3 | Saw to length | 2.86 |
| CR-201 | Shelf runner | 8 | make | S235JR | Angle 40x40x4 | Saw to length | 1.96 |
| TL-101 | Cavity insert (lower mould half) | 6 | make | Al A356-T6 | Sand casting, or 5083 tooling plate 80 mm | Sand cast + CNC finish | 18.73 |
| TL-001 | Roof tile, double-roman, plastic-sand | 6 | make | Plastic-sand composite | 70 % dry sand + 30 % HDPE by weight | Compression moulded | 2.19 |

**Hardware and consumables**

- 8 x M12x100 floor anchor
- 2 x Wall fixing bracket + M10 bolts (anti-tip, top rail to container wall)

### TR - Station 7 - Guarded trim, check and stack station

Flash is trimmed against a carbide burr inside a polycarbonate guard; offcuts and rejects fall into the regrind tote and go back to the next batch.

Drawing set: `drawings/TR_drawing_set.pdf` - assembly model: `models/step/assemblies/TR.step` - 19 unique parts, 38 pieces.

| Specification | Value |
|---|---|
| Table | 850 x 700 x 850 mm, white steel top |
| Trim tool | 0.75 kW spindle with dia 12 carbide burr, foot switch |
| Guard | 600 x 450 x 380 polycarbonate enclosure, 180 mm front opening |
| Regrind | offcuts fall through the funnel into a 60 L tote |

**Build and assembly**

1. Weld frame and guard frame, fit top, funnel, spindle, fence and panels.
2. Connect a dia 50 hose from the guard to the dust collector if trimming makes dust.

**Checks before use**

1. Burr runs true; guard panels complete; foot switch stops the spindle within 3 s.

**Operation**

1. Slide each edge of the tile along the fence past the burr. Inspect both faces for cracks, voids, short corners and warping; weigh one tile per batch.
2. Good tiles to the pallet; rejects into the tote with the offcuts - they go back through the shredder into the next batches (max 5 % per batch).

**Safety**

1. Eye protection even with the guard. Composite dust is abrasive: do not blow it off, vacuum it.

**Weldment TR-100 - Trim table frame:** Tack on a flat welding table, check diagonals within 2 mm, then fully weld all joints (fillet a3 all round, MAG 135). Grind top face flush. Prime + 2 coats enamel.

**Weldment TR-2100 - Offcut funnel:** Tack the four panels corner-to-corner on the inside dimensions, check both openings are square, then seal-weld all four corner seams continuously on the outside (fillet a3). Grind inside seams smooth so material does not hang up.

**Weldment TR-310 - Trim guard frame:** Weld square, grind, powder-coat yellow RAL 1023. Polycarbonate panels are screwed on with M5 button heads and washers at 120 pitch.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| TR-101 | Trim table frame - leg | 4 | make | S235JR | SHS 40x40x2.5 | Saw to length | 2.47 |
| TR-104 | Trim table frame - foot plate | 4 | make | S235JR | Plate 8 mm | Laser / plasma profile cut | 0.47 |
| TR-102 | Trim table frame - long rail | 3 | make | S235JR | SHS 40x40x2.5 | Saw to length | 2.27 |
| TR-103 | Trim table frame - cross rail | 4 | make | S235JR | SHS 40x40x2.5 | Saw to length | 1.83 |
| TR-201 | Trim table top | 1 | make | S235JR | Plate 4 mm | Laser / plasma profile cut | 19.81 |
| TR-2101 | Offcut funnel - front/back panel | 2 | make | DC01 galv. | Sheet 1.5 mm | Laser / plasma profile cut | 0.41 |
| TR-2102 | Offcut funnel - side panel | 2 | make | DC01 galv. | Sheet 1.5 mm | Laser / plasma profile cut | 0.32 |
| CM-TOTE60 | Stacking tote 600x400x320 (60 L) | 1 | buy | Purchased | Euro stacking container 600 x 400 x 320 mm, solid walls, PP, | Purchased item | 2.60 |
| TR-301 | Trim spindle 0.75 kW with carbide burr | 1 | buy | Purchased | Router / die-grinder spindle 0.75 kW, 10 000-20 000 rpm vari | Purchased item | 4.00 |
| TR-311 | Guard post | 4 | make | S235JR | SHS 25x25x2 | Saw to length | 0.55 |
| TR-312 | Guard top rail, long | 2 | make | S235JR | SHS 25x25x2 | Saw to length | 0.79 |
| TR-313 | Guard top rail, short | 2 | make | S235JR | SHS 25x25x2 | Saw to length | 0.58 |
| TR-321 | Guard panel, top | 1 | make | Polycarbonate | Polycarbonate sheet 4 mm | Cut to size (saw/router) | 1.30 |
| TR-322 | Guard panel, back | 1 | make | Polycarbonate | Polycarbonate sheet 4 mm | Cut to size (saw/router) | 1.09 |
| TR-323 | Guard panel, side | 2 | make | Polycarbonate | Polycarbonate sheet 4 mm | Cut to size (saw/router) | 0.82 |
| TR-324 | Guard panel, front upper | 1 | make | Polycarbonate | Polycarbonate sheet 4 mm | Cut to size (saw/router) | 0.58 |
| TR-401 | Trim fence | 1 | make | HDPE | HDPE board 20 mm | Cut to size (saw/router) | 0.23 |
| CM-CTRL200 | Local control station 200x300x150 | 1 | buy | Purchased | Steel enclosure IP65 200x300x150 with start/stop, mushroom E | Purchased item | 4.00 |
| TR-901 | Control post | 1 | make | S235JR | SHS 30x30x2 | Saw to length | 0.53 |

**Hardware and consumables**

- 40 x M5x16 button-head screw + washer (guard panels)
- 1 x Go / no-go gauge: tile must sit flat on the table top without rocking more than 3 mm
- 8 x M12x100 floor anchor

### FG - Finished goods pallet

Approved tiles are stacked on edge-protected pallets, 100 per shift (about 220 kg).

Drawing set: `drawings/FG_drawing_set.pdf` - assembly model: `models/step/assemblies/FG.step` - 2 unique parts, 31 pieces.

| Specification | Value |
|---|---|
| Pallet | 1200 x 1000 mm, 100 tiles = 220 kg per shift |

**Build and assembly**

1. Stack tiles flat in interlocked stacks of 10, three stacks per layer.

**Checks before use**

1. Count 100, label with date, batch numbers and recipe.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| FG-001 | Pallet 1200 x 1000 | 1 | buy | Purchased | Timber pallet 1200 x 1000 mm, 4-way entry, 1000 kg | Purchased item | 22.00 |
| TL-001 | Roof tile, double-roman, plastic-sand | 30 | make | Plastic-sand composite | 70 % dry sand + 30 % HDPE by weight | Compression moulded | 2.19 |

### EL - Power system - inverter, battery, distribution, generator

19.8 kWp PV on a 20 kW three-phase hybrid inverter with a 40 kWh LiFePO4 battery. Backup generator for cloudy days. Connected machine load approx. 27 kW; mixing and pressing are scheduled for the strongest sun.

Drawing set: `drawings/EL_drawing_set.pdf` - assembly model: `models/step/assemblies/EL.step` - 4 unique parts, 4 pieces.

| Specification | Value |
|---|---|
| PV | 36 x 550 W in 3 strings of 12 (about 500 V, 13 A each) |
| Inverter | 20 kW 3-phase hybrid, generator input |
| Battery | 40.96 kWh LiFePO4, 51.2 V |
| Connected load | about 27 kW; expected simultaneous demand 15-18 kW |
| Daily energy | about 75 kWh used vs. about 77 kWh generated at 5 peak sun hours |

**Build and assembly**

1. Mount the battery cabinet on a steel plinth at the right-hand end, inverter on the back wall, distribution board on the end wall.
2. Run PV strings from the combiner on the canopy to the inverter in conduit.
3. One circuit and isolator per machine from the board; E-stop loop through every station.
4. Bond container, canopy, every frame and the generator to the earth bar.

**Checks before use**

1. Insulation resistance and earth continuity tested and recorded.
2. RCD trip test; E-stop loop test at every button.
3. Inverter transfers to generator and back without tripping machines.

**Operation**

1. Schedule mixing and pressing between 09:30 and 15:30 when the sun is strongest; shred and dry sand outside those hours from the battery if needed.

**Safety**

1. Work on PV and battery circuits only by a qualified electrician: 500 V DC does not let go.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| EL-001 | Battery cabinet 40 kWh LiFePO4 | 1 | buy | Purchased | 8 x 5.12 kWh 51.2 V LiFePO4 rack modules (40.96 kWh) in a 60 | Purchased item | 420.00 |
| EL-002 | Hybrid inverter 20 kW 3-phase | 1 | buy | Purchased | 20 kW 400 V three-phase hybrid inverter/charger, 2 MPPT (150 | Purchased item | 48.00 |
| EL-003 | Main distribution board | 1 | buy | Purchased | Steel DB 600 x 800 x 250, IP54: 63 A 4-pole main switch, typ | Purchased item | 30.00 |
| EL-004 | Backup diesel generator 20 kVA | 1 | buy | Purchased | Silent canopy diesel generator 20 kVA / 16 kW, 400 V 50 Hz,  | Purchased item | 650.00 |

**Hardware and consumables**

- 1 x Armoured cable 5 x 10 mm2 (DB to inverter), 12 m
- 1 x Cable tray 100 mm along the back wall at 2.55 m, 12 m, with drops to each machine
- 1 x Machine supply cables H07RN-F, sizes per load schedule
- 1 x Earth electrode 2 x 2.4 m copper-clad rods + 16 mm2 main earth; bond container, canopy and every machine frame
- 1 x Emergency-stop loop: buttons at every station wired in series to the main contactor

### SC - Solar canopy 19.8 kWp

36 x 550 W modules (6 columns x 6 rows, landscape) at 10 deg on a 13.8 x 6.9 m steel canopy. Four portal frames at 4.6 m centres, seven purlin lines. The canopy shades the container and the work apron.

Drawing set: `drawings/SC_drawing_set.pdf` - assembly model: `models/step/assemblies/SC.step` - 13 unique parts, 128 pieces.

| Specification | Value |
|---|---|
| Array | 6 columns x 6 rows landscape, 13.77 x 6.90 m, 10 deg tilt |
| Frames | 4 portal frames at 4.6 m: posts SHS 150 x 150 x 5, rafters RHS 200 x 100 x 5 |
| Purlins | 7 lines RHS 120 x 60 x 3 at 1154 mm pitch |
| Clear height | 3.1 m at the rear, 4.1 m at the front |
| Design loads assumed | 0.25 kN/m2 dead, 1.0 kN/m2 wind - verify locally |

**Build and assembly**

1. Set out footings from the container corner; cast in or drill anchors.
2. Shop-weld base and cap plates to posts, cleats to rafters. Hot-dip galvanise or paint (primer + 2 coats).
3. Erect posts plumb, bolt rafters, fit knee braces and rod bracing, then purlins.
4. Lay modules from the low edge upward, mid-clamps between rows on each purlin, end-clamps at the outer edges; torque clamps to the module maker's figure.
5. Wire strings, bond every row to earth.

**Checks before use**

1. Posts plumb within 5 mm; rafter tops in one plane within 10 mm.
2. String open-circuit voltage within 3 % of each other before connecting.

**Safety**

1. Work at height: scaffold tower or lift, harness on the rafters. Modules are live in daylight - cover or keep connectors apart until commissioning.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| SC-101 | Rafter | 4 | make | S355J2 | RHS 200x100x5 | Saw to length | 159.35 |
| SC-102 | Post base plate | 8 | make | S355J2 | Plate 16 mm | Laser / plasma profile cut | 15.20 |
| SC-111 | Rear post | 4 | make | S355J2 | SHS 150x150x5 | Saw to length | 73.42 |
| SC-103 | Post cap plate | 8 | make | S355J2 | Plate 12 mm | Laser / plasma profile cut | 4.99 |
| SC-104 | Knee brace, rear | 4 | make | S235JR | SHS 60x60x3 | Saw to length | 5.34 |
| SC-112 | Front post | 4 | make | S355J2 | SHS 150x150x5 | Saw to length | 95.50 |
| SC-105 | Knee brace, front | 4 | make | S235JR | SHS 60x60x3 | Saw to length | 4.39 |
| SC-201 | Purlin | 21 | make | S355J2 | RHS 120x60x3, hot-dip galvanised | Saw to length | 37.62 |
| SC-203 | Purlin cleat | 28 | make | S355J2 | Angle 100x75x8 | Saw to length | 1.26 |
| SC-401 | PV module 550 W | 36 | buy | Purchased | Monocrystalline 550 Wp module, 144 half-cells, approx. 2278  | Purchased item | 28.00 |
| SC-301 | Bracing rod dia 16, rear | 4 | make | S355J2 | Round bar dia 16 | Saw to length | 8.21 |
| SC-302 | Bracing rod dia 16, front | 2 | make | S355J2 | Round bar dia 16 | Saw to length | 9.11 |
| SC-501 | PV combiner box | 1 | buy | Purchased | DC combiner: 3 strings of 12 modules (approx. 500 V, 13 A ea | Purchased item | 8.00 |

**Hardware and consumables**

- 32 x M20x300 chemical anchor (post base plates, 4 per post)
- 8 x Concrete footing 800 x 800 x 800, C25/30 (verify for local wind and soil)
- 60 x PV mid clamp 35 mm with M8 T-bolt
- 24 x PV end clamp 35 mm with M8 T-bolt
- 84 x M12x150 hex bolt 8.8 through purlin + nut + washers
- 32 x M16x60 hex bolt 8.8 (post caps)
- 6 x Turnbuckle M16 + clevis
- 1 x Solar cable 6 mm2 red/black, 200 m; MC4 connectors 80 pairs
- 1 x Earth bonding strap + lug per module row, 16 mm2 Cu to earth rod

### TT - Tile test rig (transverse breaking load)

Three-point bending frame with a 5 t hand-pump ram and gauge. Supports at 280 mm span (2/3 of tile length). Test at least 5 tiles from every new recipe before production; record the breaking load.

Drawing set: `drawings/TT_drawing_set.pdf` - assembly model: `models/step/assemblies/TT.step` - 10 unique parts, 17 pieces.

| Specification | Value |
|---|---|
| Method | three-point bending, supports 280 mm apart, load at mid-span across the full tile width |
| Load | 5 t hand-pump ram with gauge (or 20 kN load cell) |
| Record | breaking load, where it broke, recipe, date |

**Build and assembly**

1. Weld the frame; set the support beam and saddles; hang the ram from the top beam with the nose holder on its rod.

**Checks before use**

1. Supports parallel and level; gauge calibrated against a known load.

**Operation**

1. Rest the tile weather-side up on the two bars, bring the nose down on the roll crowns, pump steadily (about 10 s per kN) until it breaks.
2. Test 5 tiles per recipe, at least 7 days after moulding. Also soak 24 h and re-test, and leave samples in the sun for creep and warping.

**Safety**

1. Stand to the side; fragments can fly.

**Weldment TT-100 - Test rig frame:** Fully weld (a5). The top beam takes the ram reaction - weld both upright joints all round.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| TT-101 | Base runner | 2 | make | S235JR | RHS 100x50x4 | Saw to length | 7.13 |
| TT-102 | Base plate | 1 | make | S235JR | Plate 10 mm | Laser / plasma profile cut | 31.40 |
| TT-103 | Upright | 2 | make | S235JR | SHS 80x80x4 | Saw to length | 11.93 |
| TT-104 | Top beam | 1 | make | S235JR | SHS 80x80x4 | Saw to length | 6.47 |
| TT-105 | Support beam | 1 | make | S235JR | RHS 150x100x5 | Saw to length | 7.54 |
| TT-106 | Support saddle | 4 | make | S235JR | Flat bar 40x20 | Milled | 0.34 |
| TT-201 | Support / loading bar dia 30 | 3 | make | C45 | Round bar dia 30 | Saw to length | 2.00 |
| TL-001 | Roof tile, double-roman, plastic-sand | 1 | make | Plastic-sand composite | 70 % dry sand + 30 % HDPE by weight | Compression moulded | 2.19 |
| TT-202 | Loading nose holder | 1 | make | S235JR | Flat bar 60x40 | Milled | 0.96 |
| TT-301 | Hydraulic ram 5 t with hand pump and gauge | 1 | buy | Purchased | Single-acting 5 t ram, stroke >= 100 mm, with hand pump, hos | Purchased item | 9.00 |

**Hardware and consumables**

- 1 x M16 rod coupler (ram to nose holder)
- 1 x Steel rule and dial gauge (deflection reading, optional)

### TL - Mould tooling and product

The tile, the cast-aluminium cavity insert (10 off), the steel punch (2 off) and the mould carrier (2 off).

Drawing set: `drawings/TL_drawing_set.pdf` - assembly model: `models/step/assemblies/TL.step` - 6 unique parts, 11 pieces.

| Specification | Value |
|---|---|
| Tile | 420 x 330 x 8 mm double-roman, 2 nibs, 2.19 kg |
| Cavity insert | A356-T6 aluminium, 470 x 380 x 75, about 18 kg, 10 off |
| Punch | S355 steel, 470 x 380, 2 off |
| Carrier | 540 x 840 x 25 steel tray, 2 off |
| Shrinkage | allow about 1.2 % - measure the first tiles and correct the next tooling |

**Build and assembly**

1. Order of work: punch and one insert first; prove the tile; then cast and machine the other nine inserts.
2. Machine both halves from the STEP files (TL-101, TL-102) - the profile is a free-form surface and is defined only by the model.
3. Weld the carriers using two finished inserts as the jig.

**Checks before use**

1. Insert drops into the carrier pocket freely and has less than 1 mm play.
2. Punch enters each of the ten inserts with 0.3-0.5 mm gap all round.
3. Tile weight 2.1-2.3 kg, wall 8 +/-0.5 mm, lies flat within 3 mm.

**Safety**

1. Inserts with a tile weigh about 20 kg and may be at 80-100 C: gloves, two hands on the finger grooves, short carry only.

**Weldment TL-110 - Mould carrier:** Stitch-weld the rim bars to the base plate (30 every 100) with the two inserts in place as a jig and 0.75 mm shims all round, so each insert drops in freely but cannot shift. Skim the underside flat after welding if it has pulled more than 0.5 mm.

**Parts**

| Part | Name | Qty | Make/Buy | Material | Stock | Process | kg each |
|---|---|---|---|---|---|---|---|
| TL-001 | Roof tile, double-roman, plastic-sand | 1 | make | Plastic-sand composite | 70 % dry sand + 30 % HDPE by weight | Compression moulded | 2.19 |
| TL-101 | Cavity insert (lower mould half) | 2 | make | Al A356-T6 | Sand casting, or 5083 tooling plate 80 mm | Sand cast + CNC finish | 18.73 |
| TL-111 | Carrier base plate | 1 | make | S355J2 | Plate 10 mm | Laser / plasma profile cut | 35.55 |
| TL-112 | Carrier long rim bar | 2 | make | S235JR | Flat bar 20x15 | Saw to length | 1.94 |
| TL-113 | Carrier cross rim bar | 3 | make | S235JR | Flat bar 20x15 | Saw to length | 1.11 |
| TL-102 | Punch (upper mould half) | 2 | make | S355J2 | Plate 100 mm | 3-axis CNC surface machined | 84.86 |

## 8. How to make each part

Parts are listed by number. Positions in hole tables on the drawings are measured from the minimum-X, minimum-Y, minimum-Z corner of the part as drawn.


#### CM-CLAMP114 - Pipe clamp DN100 with M12 hanger rod

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Two-piece steel pipe clamp for OD 114.3, M12 boss, with M12 threaded rod 500 mm and roof/beam fixing
- **Envelope:** 30 x 126 x 605 mm - **mass** 1.20 kg
- **Files:** `models/step/parts/CM-CLAMP114.step`, `models/stl/CM-CLAMP114.stl`, `drawings/parts/CM-CLAMP114.svg`
- **Purchase specification:** Two-piece steel pipe clamp for OD 114.3, M12 boss, with M12 threaded rod 500 mm and roof/beam fixing
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-CTRL200 - Local control station 200x300x150

- **Quantity in plant:** 4 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Steel enclosure IP65 200x300x150 with start/stop, mushroom E-stop (EN ISO 13850), motor starter / contactor with overload, lockable isolator
- **Envelope:** 200 x 158 x 300 mm - **mass** 4.00 kg
- **Files:** `models/step/parts/CM-CTRL200.step`, `models/stl/CM-CTRL200.stl`, `drawings/parts/CM-CTRL200.svg`
- **Purchase specification:** Steel enclosure IP65 200x300x150 with start/stop, mushroom E-stop (EN ISO 13850), motor starter / contactor with overload, lockable isolator
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-F98-80 - Screw flight segment dia 98/34, pitch 80

- **Quantity in plant:** 104 - **Made in-house** - Sectional flight, cut + formed
- **Material / stock:** S355J2 - Plate 4 mm
- **Envelope:** 84 x 98 x 98 mm - **mass** 0.21 kg
- **Key dimensions:** Flight OD: 98; Flight ID: 34; Pitch: 80; Thickness: 4; Blank outer radius R: 55.1; Blank inner radius r: 23.1; Blank included angle: 330.6 deg
- **Files:** `models/step/parts/CM-F98-80.step`, `models/stl/CM-F98-80.stl`, `drawings/parts/CM-F98-80.svg`, `models/dxf/CM-F98-80.dxf`
- **Notes:** One blank makes one full pitch. Right-hand helix.
  1. Laser-cut the annular blank from 4 mm S355 using the DXF. One blank = one pitch (80 mm) of right-hand flight. Cut one extra per screw as a spare.
  2. Clamp one cut end of the blank in the vice or tack it to the bench. Grip the other end with a lever or chain block and pull the ring axially until the ends are 80 mm apart; dress out kinks over a dia 34 bar. A pair of 80 mm pitch forming dies in a 20 t press gives a better result if many are needed.
  3. Slide the flight onto the centre pipe, butt it to the previous segment, check the 98 mm OD in the casing tube itself, tack at four points on the inner edge.
  4. When all segments are on: weld the butt joints between segments (grind flush) and stitch-weld the inner edge to the pipe 25 mm every 75 mm, both sides alternately to keep the pipe straight.
  5. Straighten the finished screw between centres to within 1.5 mm TIR; it must turn freely in the casing with about 4.5 mm radial clearance.

#### CM-G037-20-22 - Gearmotor 0.37 kW, 22 rpm, hollow shaft dia 20

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50 Hz, output approx. 22 rpm, hollow bore 20 H7 with keyway, torque arm, IP55
- **Envelope:** 125 x 150 x 340 mm - **mass** 12.00 kg
- **Files:** `models/step/parts/CM-G037-20-22.step`, `models/stl/CM-G037-20-22.stl`, `drawings/parts/CM-G037-20-22.svg`
- **Purchase specification:** Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50 Hz, output approx. 22 rpm, hollow bore 20 H7 with keyway, torque arm, IP55
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-G037-25-90 - Gearmotor 0.37 kW, 90 rpm, hollow shaft dia 25

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50 Hz, output approx. 90 rpm, hollow bore 25 H7 with keyway, torque arm, IP55
- **Envelope:** 125 x 150 x 340 mm - **mass** 12.00 kg
- **Files:** `models/step/parts/CM-G037-25-90.step`, `models/stl/CM-G037-25-90.stl`, `drawings/parts/CM-G037-25-90.svg`
- **Purchase specification:** Shaft-mounted worm/helical gearmotor 0.37 kW, 400 V 3-ph 50 Hz, output approx. 90 rpm, hollow bore 25 H7 with keyway, torque arm, IP55
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-G075-25-120 - Gearmotor 0.75 kW, 120 rpm, hollow shaft dia 25

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Shaft-mounted worm/helical gearmotor 0.75 kW, 400 V 3-ph 50 Hz, output approx. 120 rpm, hollow bore 25 H7 with keyway, torque arm, IP55
- **Envelope:** 145 x 176 x 410 mm - **mass** 20.00 kg
- **Files:** `models/step/parts/CM-G075-25-120.step`, `models/stl/CM-G075-25-120.stl`, `drawings/parts/CM-G075-25-120.svg`
- **Purchase specification:** Shaft-mounted worm/helical gearmotor 0.75 kW, 400 V 3-ph 50 Hz, output approx. 120 rpm, hollow bore 25 H7 with keyway, torque arm, IP55
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-G220-40-30 - Gearmotor 2.2 kW, 30 rpm, hollow shaft dia 40

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Shaft-mounted worm/helical gearmotor 2.2 kW, 400 V 3-ph 50 Hz, output approx. 30 rpm, hollow bore 40 H7 with keyway, torque arm, IP55
- **Envelope:** 180 x 226 x 530 mm - **mass** 45.00 kg
- **Files:** `models/step/parts/CM-G220-40-30.step`, `models/stl/CM-G220-40-30.stl`, `drawings/parts/CM-G220-40-30.svg`
- **Purchase specification:** Shaft-mounted worm/helical gearmotor 2.2 kW, 400 V 3-ph 50 Hz, output approx. 30 rpm, hollow bore 40 H7 with keyway, torque arm, IP55
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-G400-35-70 - Gearmotor 4 kW, 70 rpm, hollow shaft dia 35

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Shaft-mounted worm/helical gearmotor 4 kW, 400 V 3-ph 50 Hz, output approx. 70 rpm, hollow bore 35 H7 with keyway, torque arm, IP55
- **Envelope:** 220 x 274 x 620 mm - **mass** 70.00 kg
- **Files:** `models/step/parts/CM-G400-35-70.step`, `models/stl/CM-G400-35-70.stl`, `drawings/parts/CM-G400-35-70.svg`
- **Purchase specification:** Shaft-mounted worm/helical gearmotor 4 kW, 400 V 3-ph 50 Hz, output approx. 70 rpm, hollow bore 35 H7 with keyway, torque arm, IP55
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-ROLL900 - Gravity roller dia 50 x 900

- **Quantity in plant:** 21 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Steel gravity conveyor roller dia 50 x 1.5, face length 900, spring-loaded axle dia 12 (hex 11), precision bearings, 60 kg rating
- **Envelope:** 930 x 50 x 50 mm - **mass** 3.40 kg
- **Files:** `models/step/parts/CM-ROLL900.step`, `models/stl/CM-ROLL900.stl`, `drawings/parts/CM-ROLL900.svg`
- **Purchase specification:** Steel gravity conveyor roller dia 50 x 1.5, face length 900, spring-loaded axle dia 12 (hex 11), precision bearings, 60 kg rating
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-SCALE15 - Bench scale 15 kg x 5 g

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Stainless bench scale, 15 kg capacity, 5 g resolution, platform approx. 350 x 300 mm, IP65
- **Envelope:** 350 x 300 x 55 mm - **mass** 4.00 kg
- **Files:** `models/step/parts/CM-SCALE15.step`, `models/stl/CM-SCALE15.stl`, `drawings/parts/CM-SCALE15.svg`
- **Purchase specification:** Stainless bench scale, 15 kg capacity, 5 g resolution, platform approx. 350 x 300 mm, IP65
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-TOTE60 - Stacking tote 600x400x320 (60 L)

- **Quantity in plant:** 3 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Euro stacking container 600 x 400 x 320 mm, solid walls, PP, blue
- **Envelope:** 600 x 400 x 320 mm - **mass** 2.60 kg
- **Files:** `models/step/parts/CM-TOTE60.step`, `models/stl/CM-TOTE60.stl`, `drawings/parts/CM-TOTE60.svg`
- **Purchase specification:** Euro stacking container 600 x 400 x 320 mm, solid walls, PP, blue
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-UCF205 - Flange bearing unit UCF205 (shaft 25)

- **Quantity in plant:** 6 - **Purchased** - Purchased item
- **Material / stock:** Purchased - UCF205 4-bolt flanged insert bearing unit, bore 25 mm, grub-screw locking
- **Envelope:** 36 x 95 x 95 mm - **mass** 0.80 kg
- **Files:** `models/step/parts/CM-UCF205.step`, `models/stl/CM-UCF205.stl`, `drawings/parts/CM-UCF205.svg`
- **Purchase specification:** UCF205 4-bolt flanged insert bearing unit, bore 25 mm, grub-screw locking
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-UCF207 - Flange bearing unit UCF207 (shaft 35)

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - UCF207 4-bolt flanged insert bearing unit, bore 35 mm, grub-screw locking
- **Envelope:** 44 x 117 x 117 mm - **mass** 1.50 kg
- **Files:** `models/step/parts/CM-UCF207.step`, `models/stl/CM-UCF207.stl`, `drawings/parts/CM-UCF207.svg`
- **Purchase specification:** UCF207 4-bolt flanged insert bearing unit, bore 35 mm, grub-screw locking
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-UCF208 - Flange bearing unit UCF208 (shaft 40)

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - UCF208 4-bolt flanged insert bearing unit, bore 40 mm, grub-screw locking
- **Envelope:** 51 x 130 x 130 mm - **mass** 1.90 kg
- **Files:** `models/step/parts/CM-UCF208.step`, `models/stl/CM-UCF208.stl`, `drawings/parts/CM-UCF208.svg`
- **Purchase specification:** UCF208 4-bolt flanged insert bearing unit, bore 40 mm, grub-screw locking
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CM-UCP204 - Pillow block bearing UCP204 (shaft 20)

- **Quantity in plant:** 8 - **Purchased** - Purchased item
- **Material / stock:** Purchased - UCP204 pillow block insert bearing unit, bore 20 mm
- **Envelope:** 38 x 127 x 62 mm - **mass** 0.65 kg
- **Files:** `models/step/parts/CM-UCP204.step`, `models/stl/CM-UCP204.stl`, `drawings/parts/CM-UCP204.svg`
- **Purchase specification:** UCP204 pillow block insert bearing unit, bore 20 mm
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CR-101 - Cooling rack frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 1792 x 40 x 40 mm - **mass** 6.25 kg
- **Key dimensions:** Cut length: 1792; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/CR-101.step`, `models/stl/CR-101.stl`, `drawings/parts/CR-101.svg`
  1. Saw SHS 40x40x3 (S235JR) to 1792 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### CR-102 - Cooling rack frame - long rail

- **Quantity in plant:** 7 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 480 x 40 x 40 mm - **mass** 1.67 kg
- **Key dimensions:** Cut length: 480; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/CR-102.step`, `models/stl/CR-102.stl`, `drawings/parts/CR-102.svg`
  1. Saw SHS 40x40x3 (S235JR) to 480 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### CR-103 - Cooling rack frame - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 820 x 40 x 40 mm - **mass** 2.86 kg
- **Key dimensions:** Cut length: 820; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/CR-103.step`, `models/stl/CR-103.stl`, `drawings/parts/CR-103.svg`
  1. Saw SHS 40x40x3 (S235JR) to 820 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### CR-104 - Cooling rack frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 60 x 130 x 8 mm - **mass** 0.47 kg
- **Key dimensions:** Length: 60; Width: 130; Thickness: 8
- **Files:** `models/step/parts/CR-104.step`, `models/stl/CR-104.stl`, `drawings/parts/CR-104.svg`, `models/dxf/CR-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### CR-201 - Shelf runner

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 40x40x4
- **Envelope:** 820 x 40 x 40 mm - **mass** 1.96 kg
- **Key dimensions:** Cut length: 820; Section: L 40 x 40 x 4
- **Files:** `models/step/parts/CR-201.step`, `models/stl/CR-201.stl`, `drawings/parts/CR-201.svg`
- **Notes:** Welded to the uprights; the horizontal leg carries the insert edge (35 mm bearing each side).
  1. Saw Angle 40x40x4 (S235JR) to 820 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### CT-001 - 40 ft high-cube container, modified

- **Quantity in plant:** 1 - **Purchased** - Purchased + modified on site
- **Material / stock:** Purchased - ISO 1AAA container 12.19 x 2.44 x 2.90 m, cargo-worthy
- **Envelope:** 12192 x 2438 x 2860 mm - **mass** 3900.00 kg
- **Key dimensions:** External: 12192 x 2438 x 2896; Internal: 12032 x 2352 x 2690; Side opening: 12032 x 2490 clear (front long side); Fan openings: 3 x dia 520 at 2250 above floor; Louvre openings: 4 x 500 x 400 at 2300 above floor; Duct opening: dia 210 at 2500
- **Files:** `models/step/parts/CT-001.step`, `models/stl/CT-001.stl`, `drawings/parts/CT-001.svg`
- **Purchase specification:** Used ISO 40 ft high-cube dry container, wind- and water-tight, floor sound, CSC plate not required. Internal 12.03 x 2.35 x 2.69 m.
  1. Set the container level on six concrete pads or sleepers (four corner castings + two mid-span under the bottom side rails), 170 mm floor height. Check diagonals.
  2. BEFORE cutting anything: tack the header beam CT-101 under the front top side rail and fit the three posts CT-102 with their plates (CT-103) plumb at x = 3008, 6016 and 9024 mm. Fully weld header to top rail (stitch 50/150 both sides) and posts to header and to the bottom side rail.
  3. Only then cut out the corrugated front side panel between the corner posts, flush with the top and bottom rails (plasma or 1 mm slitting discs). Grind the cut edges smooth and cap with 30 x 3 flat if ragged.
  4. Mark the back-wall openings from inside (heights from the floor): 3 fan holes dia 520, 4 louvre openings 500 x 400, 1 duct hole dia 210. Frame each rectangular opening with 30 x 30 x 3 angle welded to the corrugation so the louvre has a flat seat.
  5. Wire-brush, prime (zinc phosphate) and repaint all cut edges. Seal the plywood floor with two coats of epoxy floor paint; mark the 1.0 m walking aisle and one-way arrows in yellow.
  6. Bond the container to the earth electrode (see electrical notes) before any machine is powered.

#### CT-002 - Container roof (part of CT-001, kept)

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - part of container
- **Envelope:** 12192 x 2438 x 36 mm - **mass** 0.00 kg
- **Files:** `models/step/parts/CT-002.step`, `models/stl/CT-002.stl`, `drawings/parts/CT-002.svg`
- **Purchase specification:** Original roof panel is retained - shown transparent.
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CT-101 - Front header beam

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - RHS 200x100x6
- **Envelope:** 12032 x 100 x 200 mm - **mass** 326.42 kg
- **Key dimensions:** Cut length: 12032.0; Section: 200 x 100 x 6; Note: supplied as 2 x 6016, full-penetration butt weld over the centre post
- **Files:** `models/step/parts/CT-101.step`, `models/stl/CT-101.stl`, `drawings/parts/CT-101.svg`
  1. Saw RHS 200x100x6 (S355J2) to 12032 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### CT-102 - Front opening post

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - SHS 100x100x5
- **Envelope:** 2410 x 100 x 100 mm - **mass** 35.95 kg
- **Key dimensions:** Cut length: 2410.0; Section: 100 x 100 x 5 wall
- **Files:** `models/step/parts/CT-102.step`, `models/stl/CT-102.stl`, `drawings/parts/CT-102.svg`
  1. Saw SHS 100x100x5 (S355J2) to 2410 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### CT-103 - Post end plate

- **Quantity in plant:** 6 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 200 x 200 x 10 mm - **mass** 3.09 kg
- **Key dimensions:** Length: 200; Width: 200; Thickness: 10
- **Files:** `models/step/parts/CT-103.step`, `models/stl/CT-103.stl`, `drawings/parts/CT-103.svg`, `models/dxf/CT-103.dxf`
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### CT-201 - Weather louvre 500 x 400

- **Quantity in plant:** 4 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Aluminium weather louvre 500 x 400 with insect mesh, flanged frame
- **Envelope:** 540 x 45 x 440 mm - **mass** 3.00 kg
- **Files:** `models/step/parts/CT-201.step`, `models/stl/CT-201.stl`, `drawings/parts/CT-201.svg`
- **Purchase specification:** Aluminium weather louvre 500 x 400 with insect mesh, flanged frame
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CT-202 - Wall axial fan dia 500

- **Quantity in plant:** 3 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Plate-mounted axial exhaust fan dia 500, approx. 6000 m3/h, 0.25 kW, IP55, with finger guard and gravity shutter
- **Envelope:** 540 x 120 x 540 mm - **mass** 9.00 kg
- **Files:** `models/step/parts/CT-202.step`, `models/stl/CT-202.stl`, `drawings/parts/CT-202.svg`
- **Purchase specification:** Plate-mounted axial exhaust fan dia 500, approx. 6000 m3/h, 0.25 kW, IP55, with finger guard and gravity shutter
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CT-203 - LED batten 1500 mm, 50 W

- **Quantity in plant:** 6 - **Purchased** - Purchased item
- **Material / stock:** Purchased - IP65 LED batten 1.5 m, 50 W, 4000 K, approx. 6500 lm (target 300 lux on the work surfaces)
- **Envelope:** 1500 x 80 x 60 mm - **mass** 2.00 kg
- **Files:** `models/step/parts/CT-203.step`, `models/stl/CT-203.stl`, `drawings/parts/CT-203.svg`
- **Purchase specification:** IP65 LED batten 1.5 m, 50 W, 4000 K, approx. 6500 lm (target 300 lux on the work surfaces)
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### CT-204 - Fire extinguisher 6 kg ABC + CO2 2 kg set

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - 6 kg ABC powder + 2 kg CO2 extinguisher, wall brackets, sign
- **Envelope:** 150 x 150 x 500 mm - **mass** 12.00 kg
- **Files:** `models/step/parts/CT-204.step`, `models/stl/CT-204.stl`, `drawings/parts/CT-204.svg`
- **Purchase specification:** 6 kg ABC powder + 2 kg CO2 extinguisher, wall brackets, sign
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DC-101 - Dust collector stand - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2.5
- **Envelope:** 489 x 30 x 30 mm - **mass** 1.06 kg
- **Key dimensions:** Cut length: 489; Section: 30 x 30 x 2.5 wall
- **Files:** `models/step/parts/DC-101.step`, `models/stl/DC-101.stl`, `drawings/parts/DC-101.svg`
  1. Saw SHS 30x30x2.5 (S235JR) to 489 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DC-102 - Dust collector stand - long rail

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2.5
- **Envelope:** 390 x 30 x 30 mm - **mass** 0.84 kg
- **Key dimensions:** Cut length: 390; Section: 30 x 30 x 2.5 wall
- **Files:** `models/step/parts/DC-102.step`, `models/stl/DC-102.stl`, `drawings/parts/DC-102.svg`
  1. Saw SHS 30x30x2.5 (S235JR) to 390 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DC-103 - Dust collector stand - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2.5
- **Envelope:** 390 x 30 x 30 mm - **mass** 0.84 kg
- **Key dimensions:** Cut length: 390; Section: 30 x 30 x 2.5 wall
- **Files:** `models/step/parts/DC-103.step`, `models/stl/DC-103.stl`, `drawings/parts/DC-103.svg`
  1. Saw SHS 30x30x2.5 (S235JR) to 390 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DC-104 - Dust collector stand - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 50 x 120 x 8 mm - **mass** 0.36 kg
- **Key dimensions:** Length: 50; Width: 120; Thickness: 8
- **Files:** `models/step/parts/DC-104.step`, `models/stl/DC-104.stl`, `drawings/parts/DC-104.svg`, `models/dxf/DC-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-201 - Dust collector body - top plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 2 mm
- **Envelope:** 450 x 450 x 2 mm - **mass** 2.69 kg
- **Key dimensions:** Length: 450; Width: 450; Thickness: 2
- **Files:** `models/step/parts/DC-201.step`, `models/stl/DC-201.stl`, `drawings/parts/DC-201.svg`, `models/dxf/DC-201.dxf`
  1. Profile-cut from Plate 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (2 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-202 - Dust collector body - front plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 2 mm
- **Envelope:** 450 x 996 x 2 mm - **mass** 3.73 kg
- **Key dimensions:** Length: 450; Width: 996; Thickness: 2
- **Files:** `models/step/parts/DC-202.step`, `models/stl/DC-202.stl`, `drawings/parts/DC-202.svg`, `models/dxf/DC-202.dxf`
  1. Profile-cut from Plate 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-203 - Dust collector body - back plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 2 mm
- **Envelope:** 450 x 996 x 2 mm - **mass** 7.04 kg
- **Key dimensions:** Length: 450; Width: 996; Thickness: 2
- **Files:** `models/step/parts/DC-203.step`, `models/stl/DC-203.stl`, `drawings/parts/DC-203.svg`, `models/dxf/DC-203.dxf`
  1. Profile-cut from Plate 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-204 - Dust collector body - left plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 2 mm
- **Envelope:** 446 x 996 x 2 mm - **mass** 6.78 kg
- **Key dimensions:** Length: 446; Width: 996; Thickness: 2
- **Files:** `models/step/parts/DC-204.step`, `models/stl/DC-204.stl`, `drawings/parts/DC-204.svg`, `models/dxf/DC-204.dxf`
  1. Profile-cut from Plate 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (2 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-205 - Dust collector body - right plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 2 mm
- **Envelope:** 446 x 996 x 2 mm - **mass** 6.97 kg
- **Key dimensions:** Length: 446; Width: 996; Thickness: 2
- **Files:** `models/step/parts/DC-205.step`, `models/stl/DC-205.stl`, `drawings/parts/DC-205.svg`, `models/dxf/DC-205.dxf`
  1. Profile-cut from Plate 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-210 - Service door

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 2 mm
- **Envelope:** 400 x 680 x 2 mm - **mass** 4.27 kg
- **Key dimensions:** Length: 400; Width: 680; Thickness: 2
- **Files:** `models/step/parts/DC-210.step`, `models/stl/DC-210.stl`, `drawings/parts/DC-210.svg`, `models/dxf/DC-210.dxf`
- **Notes:** Bolted with 8 x M6 wing nuts over a 20 x 5 EPDM gasket.
  1. Profile-cut from Plate 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (2 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-301 - Dust hopper - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 380 x 246 x 2 mm - **mass** 1.03 kg
- **Key dimensions:** Bottom width: 150; Top width: 380; Slant height: 246.5; Thickness: 2; Wall angle to horizontal: 62.2 deg
- **Files:** `models/step/parts/DC-301.step`, `models/stl/DC-301.stl`, `drawings/parts/DC-301.svg`, `models/dxf/DC-301.dxf`
  1. Profile-cut from Sheet 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-302 - Dust hopper - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 380 x 246 x 2 mm - **mass** 1.03 kg
- **Key dimensions:** Bottom width: 150; Top width: 380; Slant height: 246.5; Thickness: 2; Wall angle to horizontal: 62.2 deg
- **Files:** `models/step/parts/DC-302.step`, `models/stl/DC-302.stl`, `drawings/parts/DC-302.svg`, `models/dxf/DC-302.dxf`
  1. Profile-cut from Sheet 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-304 - Hopper flange ring

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Plate 3 mm
- **Envelope:** 450 x 450 x 3 mm - **mass** 1.37 kg
- **Key dimensions:** Length: 450; Width: 450; Thickness: 3
- **Files:** `models/step/parts/DC-304.step`, `models/stl/DC-304.stl`, `drawings/parts/DC-304.svg`, `models/dxf/DC-304.dxf`
- **Notes:** Sits on the stand top rails; the body stands on it and the hopper is welded underneath.
  1. Profile-cut from Plate 3 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DC-401 - Filter cartridge dia 325 x 600

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Pleated polyester cartridge, OD 325 x 600, approx. 10 m2, flange top, M class (EN 60335-2-69) or better
- **Envelope:** 325 x 325 x 600 mm - **mass** 4.00 kg
- **Files:** `models/step/parts/DC-401.step`, `models/stl/DC-401.stl`, `drawings/parts/DC-401.svg`
- **Purchase specification:** Pleated polyester cartridge, OD 325 x 600, approx. 10 m2, flange top, M class (EN 60335-2-69) or better
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DC-402 - Centrifugal fan 0.75 kW

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Radial fan 0.75 kW 2-pole, approx. 1000 m3/h at 1500 Pa, vertical shaft, inlet dia 200
- **Envelope:** 530 x 420 x 400 mm - **mass** 22.00 kg
- **Files:** `models/step/parts/DC-402.step`, `models/stl/DC-402.stl`, `drawings/parts/DC-402.svg`
- **Purchase specification:** Radial fan 0.75 kW 2-pole, approx. 1000 m3/h at 1500 Pa, vertical shaft, inlet dia 200
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DC-403 - Dust bucket 30 L

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Steel dust bucket 30 L with quick-release band clamp
- **Envelope:** 300 x 300 x 250 mm - **mass** 2.00 kg
- **Files:** `models/step/parts/DC-403.step`, `models/stl/DC-403.stl`, `drawings/parts/DC-403.svg`
- **Purchase specification:** Steel dust bucket 30 L with quick-release band clamp
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DR-101 - Dryer frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x3
- **Envelope:** 852 x 60 x 60 mm - **mass** 4.57 kg
- **Key dimensions:** Cut length: 852.0; Section: 60 x 60 x 3 wall
- **Files:** `models/step/parts/DR-101.step`, `models/stl/DR-101.stl`, `drawings/parts/DR-101.svg`
  1. Saw SHS 60x60x3 (S235JR) to 852 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-102 - Dryer frame - long rail

- **Quantity in plant:** 6 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x3
- **Envelope:** 1420 x 60 x 60 mm - **mass** 7.62 kg
- **Key dimensions:** Cut length: 1420; Section: 60 x 60 x 3 wall
- **Files:** `models/step/parts/DR-102.step`, `models/stl/DR-102.stl`, `drawings/parts/DR-102.svg`
  1. Saw SHS 60x60x3 (S235JR) to 1420 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-103 - Dryer frame - cross rail

- **Quantity in plant:** 6 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x3
- **Envelope:** 580 x 60 x 60 mm - **mass** 3.11 kg
- **Key dimensions:** Cut length: 580; Section: 60 x 60 x 3 wall
- **Files:** `models/step/parts/DR-103.step`, `models/stl/DR-103.stl`, `drawings/parts/DR-103.svg`
  1. Saw SHS 60x60x3 (S235JR) to 580 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-104 - Dryer frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 80 x 150 x 8 mm - **mass** 0.73 kg
- **Key dimensions:** Length: 80; Width: 150; Thickness: 8
- **Files:** `models/step/parts/DR-104.step`, `models/stl/DR-104.stl`, `drawings/parts/DR-104.svg`, `models/dxf/DR-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-105 - Dryer frame - jack cross rail

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x3
- **Envelope:** 580 x 60 x 60 mm - **mass** 3.11 kg
- **Key dimensions:** Cut length: 580; Section: 60 x 60 x 3 wall
- **Files:** `models/step/parts/DR-105.step`, `models/stl/DR-105.stl`, `drawings/parts/DR-105.svg`
  1. Saw SHS 60x60x3 (S235JR) to 580 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-201 - Cradle rail

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - RHS 80x40x3
- **Envelope:** 1400 x 80 x 40 mm - **mass** 7.52 kg
- **Key dimensions:** Cut length: 1400; Section: 80 x 40 x 3 (laid flat)
- **Files:** `models/step/parts/DR-201.step`, `models/stl/DR-201.stl`, `drawings/parts/DR-201.svg`
  1. Saw RHS 80x40x3 (S235JR) to 1400 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-202 - Cradle end beam

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - RHS 80x40x3
- **Envelope:** 600 x 80 x 40 mm - **mass** 3.22 kg
- **Key dimensions:** Cut length: 600; Section: 80 x 40 x 3 (laid flat)
- **Files:** `models/step/parts/DR-202.step`, `models/stl/DR-202.stl`, `drawings/parts/DR-202.svg`
  1. Saw RHS 80x40x3 (S235JR) to 600 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-203 - Bearing riser block

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - RHS 80x40x3
- **Envelope:** 70 x 80 x 40 mm - **mass** 0.38 kg
- **Key dimensions:** Cut length: 70; Section: 80 x 40 x 3 (laid flat, tube axis along the drum); Holes: 2 x dia 11 at 95 mm centres across the 80 mm width
- **Files:** `models/step/parts/DR-203.step`, `models/stl/DR-203.stl`, `drawings/parts/DR-203.svg`
- **Notes:** One block under each UCP204 unit; the roller runs in the 80 mm gap between the two blocks. Drill 2 x dia 11 through the top wall. Because the 95 mm bolt centres are wider than the 80 mm block, weld a 130 x 60 x 8 flat on top (or use M10 studs welded to the block sides).
  1. Saw RHS 80x40x3 (S235JR) to 70 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-204 - Trunnion roller (plain)

- **Quantity in plant:** 2 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 125
- **Envelope:** 50 x 120 x 120 mm - **mass** 4.32 kg
- **Key dimensions:** OD: 120; Width: 50; Bore: 20 H7; Grub screws: 2 x M8 at 90 deg
- **Files:** `models/step/parts/DR-204.step`, `models/stl/DR-204.stl`, `drawings/parts/DR-204.svg`
  1. Saw dia 125 C45 bar to 54 mm.
  2. Lathe: face, drill and ream the bore to dia 20 H7, turn the OD to 120, chamfer 2 x 45 deg.
  3. Reverse on a mandrel, face to 50 mm wide.
  4. Drill and tap 2 x M8 radially at 90 deg for grub screws.
  5. Optional: flame-harden the running surface or sleeve with 10 mm polyurethane for a quieter drive.

#### DR-205 - Drive shaft dia 20

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 20 h9 bright
- **Envelope:** 1120 x 20 x 20 mm - **mass** 2.74 kg
- **Key dimensions:** Length: 1120; Diameter: 20 h9 (bright bar as drawn); Keyway: 6 x 3.5 deep x 110 at the motor end
- **Files:** `models/step/parts/DR-205.step`, `models/stl/DR-205.stl`, `drawings/parts/DR-205.svg`
  1. Saw Round bar dia 20 h9 bright (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### DR-206 - Idler shaft dia 20

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** C45 - Round bar dia 20
- **Envelope:** 1000 x 20 x 20 mm - **mass** 2.47 kg
- **Key dimensions:** Cut length: 1000; Diameter: 20
- **Files:** `models/step/parts/DR-206.step`, `models/stl/DR-206.stl`, `drawings/parts/DR-206.svg`
- **Notes:** Bright drawn bar dia 20 h9, saw and chamfer only.
  1. Saw Round bar dia 20 (C45) to 1000 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-207 - Trunnion roller (flanged, thrust)

- **Quantity in plant:** 2 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 145
- **Envelope:** 58 x 140 x 140 mm - **mass** 5.52 kg
- **Key dimensions:** Tread OD: 120; Tread width: 42 (ring is 40); Flange OD: 140; Flange width: 8; Bore: 20 H7
- **Files:** `models/step/parts/DR-207.step`, `models/stl/DR-207.stl`, `drawings/parts/DR-207.svg`
- **Notes:** The two flanges straddle riding ring No. 2 and take the downhill thrust of the tilted drum.
  1. Saw dia 145 C45 bar to 62 mm.
  2. Lathe: face, drill and ream dia 20 H7.
  3. On a mandrel turn the two flanges to OD 140 x 8 wide and the 42 mm tread to OD 120 with R2 root radii.
  4. Drill and tap 2 x M8 grub screws through one flange hub.

#### DR-211 - Cradle pivot block

- **Quantity in plant:** 2 - **Made in-house** - Milled
- **Material / stock:** S235JR - Flat bar 30x30
- **Envelope:** 80 x 30 x 30 mm - **mass** 0.43 kg
- **Key dimensions:** Size: 80 x 30 x 30; Cross hole: dia 16.4
- **Files:** `models/step/parts/DR-211.step`, `models/stl/DR-211.stl`, `drawings/parts/DR-211.svg`
- **Notes:** Welded under the discharge-end beam. A dia 16 pin through the block and two lugs on the frame forms the tilt hinge.
  1. Saw Flat bar 30x30 (S235JR) to size + 2 mm.
  2. Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.
  3. Drill (and tap where noted) the holes in the hole table. Deburr.

#### DR-301 - Drum shell

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 1400 x 400 x 400 mm - **mass** 41.12 kg
- **Key dimensions:** OD: 400; Wall: 3; Length: 1400; Developed blank: 1247 x 1400
- **Files:** `models/step/parts/DR-301.step`, `models/stl/DR-301.stl`, `drawings/parts/DR-301.svg`, `models/dxf/DR-301.dxf`
  1. Cut the flat blank (1247 x 1400 mm) from Sheet 3 mm S235JR; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### DR-302 - Riding ring

- **Quantity in plant:** 2 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** S355J2 - Flat bar 40x20
- **Envelope:** 40 x 440 x 440 mm - **mass** 8.29 kg
- **Key dimensions:** OD: 440; ID: 400; Width: 40; Developed length: 1319
- **Files:** `models/step/parts/DR-302.step`, `models/stl/DR-302.stl`, `drawings/parts/DR-302.svg`, `models/dxf/DR-302.dxf`
- **Notes:** Roll the flat bar the easy way to ID 400, butt-weld, grind flush. Ideally skim the OD and both faces in a lathe after welding to the shell.
  1. Cut the flat blank (see DXF mm) from Flat bar 40x20 S355J2; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### DR-303 - Lifter flight

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 30x30x3
- **Envelope:** 1200 x 30 x 30 mm - **mass** 1.61 kg
- **Key dimensions:** Cut length: 1200; Section: L 30 x 30 x 3
- **Files:** `models/step/parts/DR-303.step`, `models/stl/DR-303.stl`, `drawings/parts/DR-303.svg`
  1. Saw Angle 30x30x3 (S235JR) to 1200 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-304 - Feed-end dam ring

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 3 mm
- **Envelope:** 394 x 394 x 3 mm - **mass** 2.13 kg
- **Key dimensions:** OD: 394; Thickness: 3; Bore: 200
- **Files:** `models/step/parts/DR-304.step`, `models/stl/DR-304.stl`, `drawings/parts/DR-304.svg`, `models/dxf/DR-304.dxf`
  1. Profile-cut from Plate 3 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (3 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-305 - Discharge-end dam ring

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 3 mm
- **Envelope:** 394 x 394 x 3 mm - **mass** 0.98 kg
- **Key dimensions:** OD: 394; Thickness: 3; Bore: 320
- **Files:** `models/step/parts/DR-305.step`, `models/stl/DR-305.stl`, `drawings/parts/DR-305.svg`, `models/dxf/DR-305.dxf`
  1. Profile-cut from Plate 3 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (3 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-401 - Insulated drum cowl

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 700 x 540 x 270 mm - **mass** 6.97 kg
- **Key dimensions:** Inside radius: 268.5; Length: 700; Flat blank: 846 x 700
- **Files:** `models/step/parts/DR-401.step`, `models/stl/DR-401.stl`, `drawings/parts/DR-401.svg`, `models/dxf/DR-401.dxf`
- **Notes:** Roll to a half cylinder. Line the inside with 25 mm foil-faced mineral wool held by weld pins. Keeps the heat in and hands off the hot drum.
  1. Cut the flat blank (846 x 700 mm) from Sheet 1.5 mm DC01 galv.; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### DR-402 - Cowl stay

- **Quantity in plant:** 4 - **Made in-house** - Cut blank, fold
- **Material / stock:** S235JR - Flat bar 30x5
- **Envelope:** 95 x 30 x 316 mm - **mass** 0.48 kg
- **Key dimensions:** Developed length: 406; Section: 30 x 5; Bend: 90 deg, 95 mm foot
- **Files:** `models/step/parts/DR-402.step`, `models/stl/DR-402.stl`, `drawings/parts/DR-402.svg`, `models/dxf/DR-402.dxf`
  1. Cut the developed blank from Flat bar 30x5 S235JR (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### DR-501 - Feed hood - top plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 300 x 460 x 2 mm - **mass** 1.74 kg
- **Key dimensions:** Length: 300; Width: 460; Thickness: 2
- **Files:** `models/step/parts/DR-501.step`, `models/stl/DR-501.stl`, `drawings/parts/DR-501.svg`, `models/dxf/DR-501.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-502 - Feed hood - bottom plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 300 x 460 x 2 mm - **mass** 2.17 kg
- **Key dimensions:** Length: 300; Width: 460; Thickness: 2
- **Files:** `models/step/parts/DR-502.step`, `models/stl/DR-502.stl`, `drawings/parts/DR-502.svg`, `models/dxf/DR-502.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-503 - Feed hood - front plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 300 x 456 x 2 mm - **mass** 1.64 kg
- **Key dimensions:** Length: 300; Width: 456; Thickness: 2
- **Files:** `models/step/parts/DR-503.step`, `models/stl/DR-503.stl`, `drawings/parts/DR-503.svg`, `models/dxf/DR-503.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-504 - Feed hood - back plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 300 x 456 x 2 mm - **mass** 2.15 kg
- **Key dimensions:** Length: 300; Width: 456; Thickness: 2
- **Files:** `models/step/parts/DR-504.step`, `models/stl/DR-504.stl`, `drawings/parts/DR-504.svg`, `models/dxf/DR-504.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-505 - Feed hood - left plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 456 x 456 x 2 mm - **mass** 3.26 kg
- **Key dimensions:** Length: 456; Width: 456; Thickness: 2
- **Files:** `models/step/parts/DR-505.step`, `models/stl/DR-505.stl`, `drawings/parts/DR-505.svg`, `models/dxf/DR-505.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-506 - Feed hood - right plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 456 x 456 x 2 mm - **mass** 1.17 kg
- **Key dimensions:** Length: 456; Width: 456; Thickness: 2
- **Files:** `models/step/parts/DR-506.step`, `models/stl/DR-506.stl`, `drawings/parts/DR-506.svg`, `models/dxf/DR-506.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (2 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-510 - Feed inlet collar

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 164 x 164 x 150 mm - **mass** 1.53 kg
- **Key dimensions:** Inside: 160 x 160; Height: 150
- **Files:** `models/step/parts/DR-510.step`, `models/stl/DR-510.stl`, `drawings/parts/DR-510.svg`, `models/dxf/DR-510.dxf`
- **Notes:** Fold from one strip; the transfer-screw spout hangs 40 mm inside it. Fit a canvas dust sock between the two.
  1. Cut the developed blank from Sheet 2 mm DC01 galv. (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### DR-511 - Feed deflector plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 300 x 200 x 2 mm - **mass** 0.94 kg
- **Key dimensions:** Length: 300; Width: 200; Thickness: 2
- **Files:** `models/step/parts/DR-511.step`, `models/stl/DR-511.stl`, `drawings/parts/DR-511.svg`, `models/dxf/DR-511.dxf`
- **Notes:** Welded inside the hood at 50 deg so the sand slides into the drum mouth.
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-512 - Feed hood post

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 237 x 40 x 40 mm - **mass** 0.83 kg
- **Key dimensions:** Cut length: 237; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/DR-512.step`, `models/stl/DR-512.stl`, `drawings/parts/DR-512.svg`
  1. Saw SHS 40x40x3 (S235JR) to 237 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-601 - Duct air heater 4.5 kW

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Finned electric duct heater 4.5 kW, 400 V 3-ph, 200 x 200 mm duct, with over-temperature cut-out and air-flow interlock; outlet air 150-200 C
- **Envelope:** 200 x 250 x 200 mm - **mass** 9.00 kg
- **Files:** `models/step/parts/DR-601.step`, `models/stl/DR-601.stl`, `drawings/parts/DR-601.svg`
- **Purchase specification:** Finned electric duct heater 4.5 kW, 400 V 3-ph, 200 x 200 mm duct, with over-temperature cut-out and air-flow interlock; outlet air 150-200 C
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DR-602 - Centrifugal blower 0.18 kW

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Centrifugal blower 0.18 kW, approx. 400 m3/h at 300 Pa, 200 x 200 outlet flange
- **Envelope:** 240 x 260 x 240 mm - **mass** 8.00 kg
- **Files:** `models/step/parts/DR-602.step`, `models/stl/DR-602.stl`, `drawings/parts/DR-602.svg`
- **Purchase specification:** Centrifugal blower 0.18 kW, approx. 400 m3/h at 300 Pa, 200 x 200 outlet flange
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DR-701 - Discharge hood - top plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 230 x 520 x 2 mm - **mass** 1.69 kg
- **Key dimensions:** Length: 230; Width: 520; Thickness: 2
- **Files:** `models/step/parts/DR-701.step`, `models/stl/DR-701.stl`, `drawings/parts/DR-701.svg`, `models/dxf/DR-701.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (2 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-702 - Discharge hood - front/back plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 230 x 556 x 2 mm - **mass** 2.01 kg
- **Key dimensions:** Length: 230; Width: 556; Thickness: 2
- **Files:** `models/step/parts/DR-702.step`, `models/stl/DR-702.stl`, `drawings/parts/DR-702.svg`, `models/dxf/DR-702.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-703 - Discharge hood - left plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 516 x 556 x 2 mm - **mass** 2.29 kg
- **Key dimensions:** Length: 516; Width: 556; Thickness: 2
- **Files:** `models/step/parts/DR-703.step`, `models/stl/DR-703.stl`, `drawings/parts/DR-703.svg`, `models/dxf/DR-703.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (2 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-704 - Discharge hood - right plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 2 mm
- **Envelope:** 516 x 556 x 2 mm - **mass** 4.50 kg
- **Key dimensions:** Length: 516; Width: 556; Thickness: 2
- **Files:** `models/step/parts/DR-704.step`, `models/stl/DR-704.stl`, `drawings/parts/DR-704.svg`, `models/dxf/DR-704.dxf`
  1. Profile-cut from Plate 2 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### DR-711 - Discharge hood support arm

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 40x40x4
- **Envelope:** 400 x 40 x 40 mm - **mass** 0.95 kg
- **Key dimensions:** Cut length: 400; Section: L 40 x 40 x 4
- **Files:** `models/step/parts/DR-711.step`, `models/stl/DR-711.stl`, `drawings/parts/DR-711.svg`
  1. Saw Angle 40x40x4 (S235JR) to 400 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-712 - Discharge hood post

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 142 x 40 x 40 mm - **mass** 0.49 kg
- **Key dimensions:** Cut length: 142; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/DR-712.step`, `models/stl/DR-712.stl`, `drawings/parts/DR-712.svg`
  1. Saw SHS 40x40x3 (S235JR) to 142 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### DR-801 - Cradle jack screw M20

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - M20 x 120 hex set screw 8.8 with 2 nuts (slope adjustment and lock)
- **Envelope:** 20 x 20 x 120 mm - **mass** 0.40 kg
- **Files:** `models/step/parts/DR-801.step`, `models/stl/DR-801.stl`, `drawings/parts/DR-801.svg`
- **Purchase specification:** M20 x 120 hex set screw 8.8 with 2 nuts (slope adjustment and lock)
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### DR-901 - Control post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 400 x 40 x 40 mm - **mass** 1.39 kg
- **Key dimensions:** Cut length: 400; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/DR-901.step`, `models/stl/DR-901.stl`, `drawings/parts/DR-901.svg`
  1. Saw SHS 40x40x3 (S235JR) to 400 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### EL-001 - Battery cabinet 40 kWh LiFePO4

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - 8 x 5.12 kWh 51.2 V LiFePO4 rack modules (40.96 kWh) in a 600 x 600 x 2000 cabinet with BMS, DC breaker 250 A, busbars; ventilated; non-combustible plinth
- **Envelope:** 600 x 608 x 2000 mm - **mass** 420.00 kg
- **Files:** `models/step/parts/EL-001.step`, `models/stl/EL-001.stl`, `drawings/parts/EL-001.svg`
- **Purchase specification:** 8 x 5.12 kWh 51.2 V LiFePO4 rack modules (40.96 kWh) in a 600 x 600 x 2000 cabinet with BMS, DC breaker 250 A, busbars; ventilated; non-combustible plinth
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### EL-002 - Hybrid inverter 20 kW 3-phase

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - 20 kW 400 V three-phase hybrid inverter/charger, 2 MPPT (150-850 V), 48 V battery port, generator input with auto-start contact, IP65
- **Envelope:** 520 x 240 x 680 mm - **mass** 48.00 kg
- **Files:** `models/step/parts/EL-002.step`, `models/stl/EL-002.stl`, `drawings/parts/EL-002.svg`
- **Purchase specification:** 20 kW 400 V three-phase hybrid inverter/charger, 2 MPPT (150-850 V), 48 V battery port, generator input with auto-start contact, IP65
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### EL-003 - Main distribution board

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Steel DB 600 x 800 x 250, IP54: 63 A 4-pole main switch, type 2 AC SPD, 30 mA RCDs, MCBs/motor breakers per machine, E-stop loop relay, energy meter
- **Envelope:** 250 x 600 x 800 mm - **mass** 30.00 kg
- **Files:** `models/step/parts/EL-003.step`, `models/stl/EL-003.stl`, `drawings/parts/EL-003.svg`
- **Purchase specification:** Steel DB 600 x 800 x 250, IP54: 63 A 4-pole main switch, type 2 AC SPD, 30 mA RCDs, MCBs/motor breakers per machine, E-stop loop relay, energy meter
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### EL-004 - Backup diesel generator 20 kVA

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Silent canopy diesel generator 20 kVA / 16 kW, 400 V 50 Hz, 2-wire auto-start
- **Envelope:** 1500 x 800 x 1300 mm - **mass** 650.00 kg
- **Files:** `models/step/parts/EL-004.step`, `models/stl/EL-004.stl`, `drawings/parts/EL-004.svg`
- **Purchase specification:** Silent canopy diesel generator 20 kVA / 16 kW, 400 V 50 Hz, 2-wire auto-start
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### FG-001 - Pallet 1200 x 1000

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Timber pallet 1200 x 1000 mm, 4-way entry, 1000 kg
- **Envelope:** 1200 x 1000 x 144 mm - **mass** 22.00 kg
- **Files:** `models/step/parts/FG-001.step`, `models/stl/FG-001.stl`, `drawings/parts/FG-001.svg`
- **Purchase specification:** Timber pallet 1200 x 1000 mm, 4-way entry, 1000 kg
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-101 - Press base frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 100x100x5
- **Envelope:** 557 x 100 x 100 mm - **mass** 8.31 kg
- **Key dimensions:** Cut length: 557.0; Section: 100 x 100 x 5 wall
- **Files:** `models/step/parts/HP-101.step`, `models/stl/HP-101.stl`, `drawings/parts/HP-101.svg`
  1. Saw SHS 100x100x5 (S235JR) to 557 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### HP-102 - Press base frame - long rail

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 100x100x5
- **Envelope:** 800 x 100 x 100 mm - **mass** 11.93 kg
- **Key dimensions:** Cut length: 800; Section: 100 x 100 x 5 wall
- **Files:** `models/step/parts/HP-102.step`, `models/stl/HP-102.stl`, `drawings/parts/HP-102.svg`
  1. Saw SHS 100x100x5 (S235JR) to 800 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### HP-103 - Press base frame - cross rail

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 100x100x5
- **Envelope:** 960 x 100 x 100 mm - **mass** 14.32 kg
- **Key dimensions:** Cut length: 960; Section: 100 x 100 x 5 wall
- **Files:** `models/step/parts/HP-103.step`, `models/stl/HP-103.stl`, `drawings/parts/HP-103.svg`
  1. Saw SHS 100x100x5 (S235JR) to 960 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### HP-104 - Press base frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 120 x 190 x 8 mm - **mass** 1.40 kg
- **Key dimensions:** Length: 120; Width: 190; Thickness: 8
- **Files:** `models/step/parts/HP-104.step`, `models/stl/HP-104.stl`, `drawings/parts/HP-104.svg`, `models/dxf/HP-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-105 - Press base - return conveyor bearer

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 960 x 60 x 60 mm - **mass** 6.75 kg
- **Key dimensions:** Cut length: 960; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/HP-105.step`, `models/stl/HP-105.stl`, `drawings/parts/HP-105.svg`
  1. Saw SHS 60x60x4 (S235JR) to 960 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### HP-201 - Bed top plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 30 mm
- **Envelope:** 880 x 1160 x 30 mm - **mass** 236.13 kg
- **Key dimensions:** Length: 880; Width: 1160; Thickness: 30
- **Files:** `models/step/parts/HP-201.step`, `models/stl/HP-201.stl`, `drawings/parts/HP-201.svg`, `models/dxf/HP-201.dxf`
- **Notes:** 6 x dia 14 are tapping-drill positions for M16 (lower bolster screws) - drill and tap after machining the face.
  1. Profile-cut from Plate 30 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (30 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-202 - Bed bottom plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 20 mm
- **Envelope:** 880 x 1160 x 20 mm - **mass** 157.56 kg
- **Key dimensions:** Length: 880; Width: 1160; Thickness: 20
- **Files:** `models/step/parts/HP-202.step`, `models/stl/HP-202.stl`, `drawings/parts/HP-202.svg`, `models/dxf/HP-202.dxf`
  1. Profile-cut from Plate 20 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (20 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-203 - Crosshead main web

- **Quantity in plant:** 9 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 16 mm
- **Envelope:** 1160 x 240 x 16 mm - **mass** 34.97 kg
- **Key dimensions:** Length: 1160; Width: 240; Thickness: 16
- **Files:** `models/step/parts/HP-203.step`, `models/stl/HP-203.stl`, `drawings/parts/HP-203.svg`, `models/dxf/HP-203.dxf`
  1. Profile-cut from Plate 16 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-204 - Crosshead stiffener, outer bay

- **Quantity in plant:** 12 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 12 mm
- **Envelope:** 208 x 240 x 12 mm - **mass** 4.70 kg
- **Key dimensions:** Length: 208; Width: 240; Thickness: 12
- **Files:** `models/step/parts/HP-204.step`, `models/stl/HP-204.stl`, `drawings/parts/HP-204.svg`, `models/dxf/HP-204.dxf`
  1. Profile-cut from Plate 12 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-205 - Crosshead stiffener, inner bay

- **Quantity in plant:** 6 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 12 mm
- **Envelope:** 184 x 240 x 12 mm - **mass** 4.16 kg
- **Key dimensions:** Length: 184; Width: 240; Thickness: 12
- **Files:** `models/step/parts/HP-205.step`, `models/stl/HP-205.stl`, `drawings/parts/HP-205.svg`, `models/dxf/HP-205.dxf`
  1. Profile-cut from Plate 12 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-206 - Column sleeve

- **Quantity in plant:** 8 - **Made in-house** - Lathe turned
- **Material / stock:** S355J2 - Hollow bar OD 121 x ID 71
- **Envelope:** 240 x 121 x 121 mm - **mass** 13.56 kg
- **Key dimensions:** OD: 121; ID: 74 (finish-bored to 72 H8 after welding); Length: 240
- **Files:** `models/step/parts/HP-206.step`, `models/stl/HP-206.stl`, `drawings/parts/HP-206.svg`
  1. Saw Hollow bar OD 121 x ID 71 (S355J2) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### HP-301 - Crown bottom plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 30 mm
- **Envelope:** 880 x 1160 x 30 mm - **mass** 217.86 kg
- **Key dimensions:** Length: 880; Width: 1160; Thickness: 30
- **Files:** `models/step/parts/HP-301.step`, `models/stl/HP-301.stl`, `drawings/parts/HP-301.svg`, `models/dxf/HP-301.dxf`
- **Notes:** Load face: the cylinder head flange bears on the underside. 8 x dia 22 on PCD 380 for M20 flange bolts.
  1. Profile-cut from Plate 30 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (30 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-302 - Crown top plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 20 mm
- **Envelope:** 880 x 1160 x 20 mm - **mass** 145.71 kg
- **Key dimensions:** Length: 880; Width: 1160; Thickness: 20
- **Files:** `models/step/parts/HP-302.step`, `models/stl/HP-302.stl`, `drawings/parts/HP-302.svg`, `models/dxf/HP-302.dxf`
  1. Profile-cut from Plate 20 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (20 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-303 - Crown centre stiffener

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 12 mm
- **Envelope:** 384 x 240 x 12 mm - **mass** 8.68 kg
- **Key dimensions:** Length: 384; Width: 240; Thickness: 12
- **Files:** `models/step/parts/HP-303.step`, `models/stl/HP-303.stl`, `drawings/parts/HP-303.svg`, `models/dxf/HP-303.dxf`
  1. Profile-cut from Plate 12 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-304 - Cylinder sleeve ring

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** S355J2 - Plate 16 mm
- **Envelope:** 240 x 355 x 355 mm - **mass** 32.10 kg
- **Key dimensions:** OD: 355; Wall: 16; Height: 240; Developed blank: 1065 x 240
- **Files:** `models/step/parts/HP-304.step`, `models/stl/HP-304.stl`, `drawings/parts/HP-304.svg`, `models/dxf/HP-304.dxf`
  1. Cut the flat blank (1065 x 240 mm) from Plate 16 mm S355J2; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### HP-401 - Press column dia 80

- **Quantity in plant:** 4 - **Made in-house** - Lathe turned
- **Material / stock:** 42CrMo4 - Round bar dia 80, hard-chromed
- **Envelope:** 1510 x 80 x 80 mm - **mass** 54.11 kg
- **Key dimensions:** Overall length: 1510.0; Body: dia 80 f7 x 780 (chromed, ground); Ends: dia 72 x 365, threaded M72x4 for 80 mm; Shoulder length tolerance: +/-0.05 mm, all four columns matched
- **Files:** `models/step/parts/HP-401.step`, `models/stl/HP-401.stl`, `drawings/parts/HP-401.svg`
  1. Saw 42CrMo4 (QT, hard-chromed and ground dia 80 f7 bar) to length + 6 mm.
  2. Lathe with steady rest: face and centre both ends.
  3. Between centres: turn both ends to dia 72 g6 for 365 mm, leaving a sharp square shoulder with a 1 x 45 deg relief. The distance between the two shoulders is the press daylight datum: hold it within +/-0.05 mm and make all four columns in one batch.
  4. Screw-cut M72x4 for 80 mm at each end; fit a nut as gauge.
  5. Protect the chromed body with sleeve during all handling.

#### HP-402 - Column nut M72x4

- **Quantity in plant:** 8 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Hexagon bar 105 A/F
- **Envelope:** 121 x 105 x 58 mm - **mass** 2.49 kg
- **Key dimensions:** Across flats: 105; Height: 58; Thread: M72x4
- **Files:** `models/step/parts/HP-402.step`, `models/stl/HP-402.stl`, `drawings/parts/HP-402.svg`
- **Notes:** Can be bought as DIN 934 M72x4 class 8. Tighten each to 2000 N.m in a cross pattern, or hydraulically pre-tension.
  1. Saw Hexagon bar 105 A/F (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### HP-501 - Platen bottom plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 30 mm
- **Envelope:** 860 x 1140 x 30 mm - **mass** 217.97 kg
- **Key dimensions:** Length: 860; Width: 1140; Thickness: 30
- **Files:** `models/step/parts/HP-501.step`, `models/stl/HP-501.stl`, `drawings/parts/HP-501.svg`, `models/dxf/HP-501.dxf`
- **Notes:** 6 x dia 14 tapping positions for M16 upper-bolster screws.
  1. Profile-cut from Plate 30 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (30 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-502 - Platen top plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 20 mm
- **Envelope:** 860 x 1140 x 20 mm - **mass** 145.10 kg
- **Key dimensions:** Length: 860; Width: 1140; Thickness: 20
- **Files:** `models/step/parts/HP-502.step`, `models/stl/HP-502.stl`, `drawings/parts/HP-502.svg`, `models/dxf/HP-502.dxf`
  1. Profile-cut from Plate 20 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (20 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-503 - Platen web

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 16 mm
- **Envelope:** 1108 x 150 x 16 mm - **mass** 20.87 kg
- **Key dimensions:** Length: 1108; Width: 150; Thickness: 16
- **Files:** `models/step/parts/HP-503.step`, `models/stl/HP-503.stl`, `drawings/parts/HP-503.svg`, `models/dxf/HP-503.dxf`
  1. Profile-cut from Plate 16 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-504 - Platen end web

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 16 mm
- **Envelope:** 860 x 150 x 16 mm - **mass** 16.20 kg
- **Key dimensions:** Length: 860; Width: 150; Thickness: 16
- **Files:** `models/step/parts/HP-504.step`, `models/stl/HP-504.stl`, `drawings/parts/HP-504.svg`, `models/dxf/HP-504.dxf`
  1. Profile-cut from Plate 16 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### HP-505 - Bush housing

- **Quantity in plant:** 4 - **Made in-house** - Lathe turned
- **Material / stock:** S355J2 - Hollow bar OD 130 x ID 95
- **Envelope:** 200 x 130 x 130 mm - **mass** 8.51 kg
- **Key dimensions:** OD: 130; ID: 100 H7 (finish-bored after welding); Length: 200
- **Files:** `models/step/parts/HP-505.step`, `models/stl/HP-505.stl`, `drawings/parts/HP-505.svg`
  1. Saw Hollow bar OD 130 x ID 95 (S355J2) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### HP-506 - Column guide bush

- **Quantity in plant:** 4 - **Made in-house** - Lathe turned
- **Material / stock:** Bronze CuSn12 - Cast bronze tube 105/75
- **Envelope:** 200 x 100 x 100 mm - **mass** 4.88 kg
- **Key dimensions:** OD: 100 r6; ID: 80 H8 (ream after pressing in); Length: 200; Grease grooves: figure-8, 3 wide x 1.5 deep
- **Files:** `models/step/parts/HP-506.step`, `models/stl/HP-506.stl`, `drawings/parts/HP-506.svg`
  1. Saw Cast bronze tube 105/75 (Bronze CuSn12) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### HP-601 - Hydraulic cylinder 250/180 x 300

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Double-acting cylinder, bore 250, rod 180, stroke 300, 250 bar rated, head-flange mount (ISO 6022 MF1 style, 420 x 420 flange, 8 x M20 on PCD 380), rod-end male thread, cushioned
- **Envelope:** 420 x 420 x 737 mm - **mass** 430.00 kg
- **Files:** `models/step/parts/HP-601.step`, `models/stl/HP-601.stl`, `drawings/parts/HP-601.svg`
- **Purchase specification:** Double-acting cylinder, bore 250, rod 180, stroke 300, 250 bar rated, head-flange mount (ISO 6022 MF1 style, 420 x 420 flange, 8 x M20 on PCD 380), rod-end male thread, cushioned
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-602 - Rod flange

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Plate 40 mm
- **Envelope:** 280 x 280 x 40 mm - **mass** 16.15 kg
- **Key dimensions:** OD: 280; Thickness: 40; Bore: 100
- **Files:** `models/step/parts/HP-602.step`, `models/stl/HP-602.stl`, `drawings/parts/HP-602.svg`
- **Notes:** Bore threaded to suit the purchased cylinder rod end (typically M100x3). 6 x M20 into the platen top plate.
  1. Saw Plate 40 mm (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### HP-610 - Hydraulic power unit 4 kW

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Power pack: 4 kW 400 V motor, hi-lo double pump (approx. 30 l/min at 40 bar, 5 l/min at 210 bar), 60 l tank, relief valve set 210 bar, 4/3 solenoid valve with pilot check (load holding), pressure switch, gauge 0-400 bar, return filter, oil cooler optional
- **Envelope:** 500 x 330 x 580 mm - **mass** 95.00 kg
- **Files:** `models/step/parts/HP-610.step`, `models/stl/HP-610.stl`, `drawings/parts/HP-610.svg`
- **Purchase specification:** Power pack: 4 kW 400 V motor, hi-lo double pump (approx. 30 l/min at 40 bar, 5 l/min at 210 bar), 60 l tank, relief valve set 210 bar, 4/3 solenoid valve with pilot check (load holding), pressure switch, gauge 0-400 bar, return filter, oil cooler optional
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-620 - Pressure gauge 0-400 bar

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Glycerine-filled gauge dia 100, 0-400 bar, with gauge isolator
- **Envelope:** 100 x 40 x 100 mm - **mass** 0.60 kg
- **Files:** `models/step/parts/HP-620.step`, `models/stl/HP-620.stl`, `drawings/parts/HP-620.svg`
- **Purchase specification:** Glycerine-filled gauge dia 100, 0-400 bar, with gauge isolator
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-630 - Two-hand control console

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Two-hand control station type IIIC (ISO 13851) on pedestal, with E-stop, mode key switch and pressure/dwell timer display
- **Envelope:** 420 x 160 x 1070 mm - **mass** 14.00 kg
- **Files:** `models/step/parts/HP-630.step`, `models/stl/HP-630.stl`, `drawings/parts/HP-630.svg`
- **Purchase specification:** Two-hand control station type IIIC (ISO 13851) on pedestal, with E-stop, mode key switch and pressure/dwell timer display
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-640 - Safety light curtain, 500 mm, type 4

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Type 4 safety light curtain pair (IEC 61496), 500 mm protective height, 30 mm resolution, with safety relay to stop the down-stroke (ISO 13855 safety distance to be calculated)
- **Envelope:** 40 x 40 x 520 mm - **mass** 1.50 kg
- **Files:** `models/step/parts/HP-640.step`, `models/stl/HP-640.stl`, `drawings/parts/HP-640.svg`
- **Purchase specification:** Type 4 safety light curtain pair (IEC 61496), 500 mm protective height, 30 mm resolution, with safety relay to stop the down-stroke (ISO 13855 safety distance to be calculated)
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-650 - Rear fixed guard

- **Quantity in plant:** 1 - **Made in-house** - Cut to size
- **Material / stock:** S235JR - Weld mesh 25x25x2.5 in 25x25 angle frame
- **Envelope:** 880 x 700 x 2 mm - **mass** 9.67 kg
- **Key dimensions:** Width: 880; Height: 700
- **Files:** `models/step/parts/HP-650.step`, `models/stl/HP-650.stl`, `drawings/parts/HP-650.svg`, `models/dxf/HP-650.dxf`
  1. Cut to size with a shear or 1 mm slitting disc, leaving the allowance noted.
  2. Dress cut wire ends; fold or frame the edges as noted.
  3. Fix with the clamp strips / stitch welds shown on the assembly sheet.

#### HP-701 - Lower bolster with lifter grooves

- **Quantity in plant:** 1 - **Made in-house** - Milled
- **Material / stock:** S355J2 - Plate 30 mm
- **Envelope:** 600 x 900 x 30 mm - **mass** 117.32 kg
- **Key dimensions:** Size: 600 x 900 x 30; Lifter grooves: 2 x 42 wide x 24 deep, full length, at y = +/-300; Fixing: 6 x dia 18 c/bored for M16 cap screws
- **Files:** `models/step/parts/HP-701.step`, `models/stl/HP-701.stl`, `drawings/parts/HP-701.svg`
- **Notes:** Top face ground or fly-cut flat within 0.05 mm - the mould carrier seats on it under full press load.
  1. Saw Plate 30 mm (S355J2) to size + 2 mm.
  2. Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.
  3. Drill (and tap where noted) the holes in the hole table. Deburr.

#### HP-702 - Spring die-lifter bar 40x24x600 with balls

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Spring-loaded ball die lifter for 42 mm groove, 600 long, lift 3 mm, approx. 100 kg per bar; retracts flush under press load
- **Envelope:** 600 x 40 x 27 mm - **mass** 5.00 kg
- **Files:** `models/step/parts/HP-702.step`, `models/stl/HP-702.stl`, `drawings/parts/HP-702.svg`
- **Purchase specification:** Spring-loaded ball die lifter for 42 mm groove, 600 long, lift 3 mm, approx. 100 kg per bar; retracts flush under press load
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### HP-703 - Carrier end stop (flip-down)

- **Quantity in plant:** 1 - **Made in-house** - Milled
- **Material / stock:** S355J2 - Flat bar 45x30
- **Envelope:** 30 x 200 x 45 mm - **mass** 2.12 kg
- **Key dimensions:** Size: 30 x 200 x 45; Pivot hole: dia 12.5, 12 from the bottom edge
- **Files:** `models/step/parts/HP-703.step`, `models/stl/HP-703.stl`, `drawings/parts/HP-703.svg`
- **Notes:** Pivots on an M12 shoulder bolt on the outfeed edge of the lower bolster. Up = positions the carrier under the punches; flipped down = carrier rolls out.
  1. Saw Flat bar 45x30 (S355J2) to size + 2 mm.
  2. Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.
  3. Drill (and tap where noted) the holes in the hole table. Deburr.

#### HP-711 - Upper bolster

- **Quantity in plant:** 1 - **Made in-house** - Milled
- **Material / stock:** S355J2 - Plate 30 mm
- **Envelope:** 540 x 840 x 30 mm - **mass** 106.03 kg
- **Key dimensions:** Length: 540; Width: 840; Thickness: 30
- **Files:** `models/step/parts/HP-711.step`, `models/stl/HP-711.stl`, `drawings/parts/HP-711.svg`
- **Notes:** 6 x dia 18 (c/bored) to the platen, 12 x dia 14 (c/bored from above) for the M12 punch screws. Both faces parallel within 0.05 mm.
  1. Saw Plate 30 mm (S355J2) to size + 2 mm.
  2. Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.
  3. Drill (and tap where noted) the holes in the hole table. Deburr.

#### MX-101 - Mixer frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 842 x 60 x 60 mm - **mass** 5.92 kg
- **Key dimensions:** Cut length: 842.0; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/MX-101.step`, `models/stl/MX-101.stl`, `drawings/parts/MX-101.svg`
  1. Saw SHS 60x60x4 (S235JR) to 842 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-102 - Mixer frame - long rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 780 x 60 x 60 mm - **mass** 5.49 kg
- **Key dimensions:** Cut length: 780; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/MX-102.step`, `models/stl/MX-102.stl`, `drawings/parts/MX-102.svg`
  1. Saw SHS 60x60x4 (S235JR) to 780 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-103 - Mixer frame - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 780 x 60 x 60 mm - **mass** 5.49 kg
- **Key dimensions:** Cut length: 780; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/MX-103.step`, `models/stl/MX-103.stl`, `drawings/parts/MX-103.svg`
  1. Saw SHS 60x60x4 (S235JR) to 780 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-104 - Mixer frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 80 x 150 x 8 mm - **mass** 0.73 kg
- **Key dimensions:** Length: 80; Width: 150; Thickness: 8
- **Files:** `models/step/parts/MX-104.step`, `models/stl/MX-104.stl`, `drawings/parts/MX-104.svg`, `models/dxf/MX-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-201 - Mixer deck plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 900 x 900 x 8 mm - **mass** 44.44 kg
- **Key dimensions:** Length: 900; Width: 900; Thickness: 8
- **Files:** `models/step/parts/MX-201.step`, `models/stl/MX-201.stl`, `drawings/parts/MX-201.svg`, `models/dxf/MX-201.dxf`
- **Notes:** Dia 360 centre opening gives access to the base heater and its wiring. 4 x dia 13 take the drum standoffs; match-drill 8 x dia 14 from the two column base plates on assembly.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-211 - Drum base plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 12 mm
- **Envelope:** 462 x 462 x 12 mm - **mass** 15.79 kg
- **Key dimensions:** OD: 462; Thickness: 12
- **Files:** `models/step/parts/MX-211.step`, `models/stl/MX-211.stl`, `drawings/parts/MX-211.svg`, `models/dxf/MX-211.dxf`
- **Notes:** Top face is the mixing floor: flat within 1 mm so the paddle can run 3 mm clear.
  1. Profile-cut from Plate 12 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-212 - Drum shell

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** S355J2 - Sheet 6 mm
- **Envelope:** 320 x 462 x 462 mm - **mass** 21.12 kg
- **Key dimensions:** OD: 462; Wall: 6; Length: 320; Developed blank: 1433 x 320
- **Files:** `models/step/parts/MX-212.step`, `models/stl/MX-212.stl`, `drawings/parts/MX-212.svg`, `models/dxf/MX-212.dxf`
- **Notes:** Cut the 140 x 70 discharge window at the bottom edge before rolling (flat blank DXF shows the plain blank; window centred on the seam-opposite side).
  1. Cut the flat blank (1433 x 320 mm) from Sheet 6 mm S355J2; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### MX-213 - Drum rim flange

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 8 mm
- **Envelope:** 600 x 600 x 8 mm - **mass** 7.18 kg
- **Key dimensions:** OD: 600; Thickness: 8; Bore: 463
- **Files:** `models/step/parts/MX-213.step`, `models/stl/MX-213.stl`, `drawings/parts/MX-213.svg`, `models/dxf/MX-213.dxf`
  1. Profile-cut from Plate 8 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-214 - Drum standoff

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 82 x 40 x 40 mm - **mass** 0.29 kg
- **Key dimensions:** Cut length: 82; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/MX-214.step`, `models/stl/MX-214.stl`, `drawings/parts/MX-214.svg`
- **Notes:** Thin-wall standoffs limit heat flow into the frame.
  1. Saw SHS 40x40x3 (S235JR) to 82 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-215 - Standoff pad

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 80 x 80 x 8 mm - **mass** 0.39 kg
- **Key dimensions:** Length: 80; Width: 80; Thickness: 8
- **Files:** `models/step/parts/MX-215.step`, `models/stl/MX-215.stl`, `drawings/parts/MX-215.svg`, `models/dxf/MX-215.dxf`
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-221 - Discharge nozzle

- **Quantity in plant:** 1 - **Made in-house** - Plate fabrication
- **Material / stock:** S355J2 - Plate 6 mm
- **Envelope:** 80 x 152 x 82 mm - **mass** 1.67 kg
- **Key dimensions:** Inside: 140 x 70; Length: 80; Plate: 6
- **Files:** `models/step/parts/MX-221.step`, `models/stl/MX-221.stl`, `drawings/parts/MX-221.svg`
- **Notes:** Four 6 mm plates welded into a sleeve; scribe the inner end to the dia 462 shell.
  1. Cut the individual flat plates to the sizes under Key dimensions (plasma or shear).
  2. Tack together square on a flat table; offer up to the mating part and scribe any penetrations before cutting them.
  3. Weld all seams continuously (they must be dust- and sand-tight); grind inside seams smooth so material cannot hang up.

#### MX-222 - Gate flange

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 8 mm
- **Envelope:** 240 x 150 x 8 mm - **mass** 1.65 kg
- **Key dimensions:** Length: 240; Width: 150; Thickness: 8
- **Files:** `models/step/parts/MX-222.step`, `models/stl/MX-222.stl`, `drawings/parts/MX-222.svg`, `models/dxf/MX-222.dxf`
  1. Profile-cut from Plate 8 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-223 - Discharge gate blade

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 6 mm
- **Envelope:** 160 x 240 x 6 mm - **mass** 1.78 kg
- **Key dimensions:** Length: 160; Width: 240; Thickness: 6
- **Files:** `models/step/parts/MX-223.step`, `models/stl/MX-223.stl`, `drawings/parts/MX-223.svg`, `models/dxf/MX-223.dxf`
- **Notes:** Guillotine gate: lift to discharge. Fit a hardwood or PTFE grip through the dia 30 hole - the blade is hot.
  1. Profile-cut from Plate 6 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (6 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-224 - Gate guide spacer

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 20x7
- **Envelope:** 150 x 20 x 7 mm - **mass** 0.16 kg
- **Key dimensions:** Cut length: 150; Section: 20 x 7
- **Files:** `models/step/parts/MX-224.step`, `models/stl/MX-224.stl`, `drawings/parts/MX-224.svg`
  1. Saw Flat bar 20x7 (S235JR) to 150 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-225 - Gate keeper strip

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 35x5
- **Envelope:** 150 x 35 x 5 mm - **mass** 0.21 kg
- **Key dimensions:** Cut length: 150; Section: 35 x 5
- **Files:** `models/step/parts/MX-225.step`, `models/stl/MX-225.stl`, `drawings/parts/MX-225.svg`
- **Notes:** Welded over the spacer; forms the 7 mm slot the 6 mm gate blade slides in.
  1. Saw Flat bar 35x5 (S235JR) to 150 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-231 - Discharge chute

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** AISI 304 - Sheet 3 mm
- **Envelope:** 330 x 186 x 50 mm - **mass** 2.19 kg
- **Key dimensions:** Inside width: 180; Side height: 50; Length: 330; Slope: 25 deg
- **Files:** `models/step/parts/MX-231.step`, `models/stl/MX-231.stl`, `drawings/parts/MX-231.svg`, `models/dxf/MX-231.dxf`
  1. Cut the developed blank from Sheet 3 mm AISI 304 (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### MX-241 - Insulation cladding

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** AISI 304 - Sheet 1 mm
- **Envelope:** 392 x 590 x 590 mm - **mass** 5.59 kg
- **Key dimensions:** OD: 590; Wall: 1; Length: 392; Developed blank: 1850 x 392
- **Files:** `models/step/parts/MX-241.step`, `models/stl/MX-241.stl`, `drawings/parts/MX-241.svg`, `models/dxf/MX-241.dxf`
- **Notes:** Wraps 50 mm of ceramic-fibre blanket (128 kg/m3) round the heater bands. Overlap seam with 6 self-tapping screws so it can be removed to change a heater.
  1. Cut the flat blank (1850 x 392 mm) from Sheet 1 mm AISI 304; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### MX-301 - Bridge column

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 782 x 80 x 80 mm - **mass** 7.46 kg
- **Key dimensions:** Cut length: 782; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/MX-301.step`, `models/stl/MX-301.stl`, `drawings/parts/MX-301.svg`
  1. Saw SHS 80x80x4 (S235JR) to 782 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-302 - Column base plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 160 x 160 x 10 mm - **mass** 1.96 kg
- **Key dimensions:** Length: 160; Width: 160; Thickness: 10
- **Files:** `models/step/parts/MX-302.step`, `models/stl/MX-302.stl`, `drawings/parts/MX-302.svg`, `models/dxf/MX-302.dxf`
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-303 - Mixer bridge beam

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 100x100x5
- **Envelope:** 860 x 100 x 100 mm - **mass** 12.59 kg
- **Key dimensions:** Cut length: 860; Section: 100 x 100 x 5 wall
- **Files:** `models/step/parts/MX-303.step`, `models/stl/MX-303.stl`, `drawings/parts/MX-303.svg`
- **Notes:** Dia 62 through both walls on the centre for the shaft. Match-drill 4 x dia 14 (102 x 102) in the bottom wall for the UCF208 and 4 x dia 11 in the top wall for the gearbox foot. Weld to both column tops with a5 fillets all round. The bridge runs at 30 deg to the line so the discharge chute and the batch screw both stay clear.
  1. Saw SHS 100x100x5 (S235JR) to 860 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Mark out, centre-punch and drill the holes in the hole table (pilot dia 5 first, then to size); deburr both sides.
  4. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-304 - Gearbox mounting plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 12 mm
- **Envelope:** 180 x 180 x 12 mm - **mass** 2.08 kg
- **Key dimensions:** OD: 180; Thickness: 12; Bore: 62
- **Files:** `models/step/parts/MX-304.step`, `models/stl/MX-304.stl`, `drawings/parts/MX-304.svg`, `models/dxf/MX-304.dxf`
- **Notes:** Welded on top of the bridge; lifts the gearmotor so the motor body clears the beam.
  1. Profile-cut from Plate 12 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (12 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-311 - Agitator shaft dia 40

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 40 h9 bright
- **Envelope:** 957 x 40 x 40 mm - **mass** 9.32 kg
- **Key dimensions:** Length: 957; Diameter: 40 h9; Keyway: 12 P9 x 5 deep x 170 at the top end; Cross hole: dia 13, 30 from the bottom end
- **Files:** `models/step/parts/MX-311.step`, `models/stl/MX-311.stl`, `drawings/parts/MX-311.svg`
  1. Saw Round bar dia 40 h9 bright (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### MX-312 - Paddle bottom blade

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** Hardox 450 - Plate 12 mm
- **Envelope:** 436 x 60 x 12 mm - **mass** 2.46 kg
- **Key dimensions:** Length: 436; Width: 60; Thickness: 12
- **Files:** `models/step/parts/MX-312.step`, `models/stl/MX-312.stl`, `drawings/parts/MX-312.svg`, `models/dxf/MX-312.dxf`
  1. Profile-cut from Plate 12 mm Hardox 450 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-313 - Paddle side scraper

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** Hardox 450 - Flat bar 40x10
- **Envelope:** 250 x 40 x 10 mm - **mass** 0.78 kg
- **Key dimensions:** Cut length: 250; Section: 40 x 10
- **Files:** `models/step/parts/MX-313.step`, `models/stl/MX-313.stl`, `drawings/parts/MX-313.svg`
  1. Saw Flat bar 40x10 (Hardox 450) to 250 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-314 - Paddle hub

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 70
- **Envelope:** 60 x 70 x 70 mm - **mass** 1.19 kg
- **Key dimensions:** OD: 70; Bore: 40 H8; Length: 60; Cross hole: dia 13 for M12 bolt
- **Files:** `models/step/parts/MX-314.step`, `models/stl/MX-314.stl`, `drawings/parts/MX-314.svg`
  1. Saw Round bar dia 70 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### MX-321 - Rear lid with charge port

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Sheet 3 mm
- **Envelope:** 600 x 300 x 3 mm - **mass** 2.97 kg
- **Key dimensions:** Diameter: 600; Charge port: 130 x 110; Shaft notch: R35
- **Files:** `models/step/parts/MX-321.step`, `models/stl/MX-321.stl`, `drawings/parts/MX-321.svg`, `models/dxf/MX-321.dxf`
  1. Profile-cut from Sheet 3 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness ( mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-322 - Front lid (hinged, inspection)

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Sheet 3 mm
- **Envelope:** 600 x 300 x 3 mm - **mass** 3.30 kg
- **Key dimensions:** Diameter: 600; Shaft notch: R35
- **Files:** `models/step/parts/MX-322.step`, `models/stl/MX-322.stl`, `drawings/parts/MX-322.svg`, `models/dxf/MX-322.dxf`
- **Notes:** Hinged on the rim flange; fit a limit switch so the agitator stops when the lid is lifted.
  1. Profile-cut from Sheet 3 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness ( mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-323 - Charge collar

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** AISI 304 - Sheet 2 mm
- **Envelope:** 134 x 114 x 62 mm - **mass** 0.48 kg
- **Key dimensions:** Inside: 130 x 110; Height: 62
- **Files:** `models/step/parts/MX-323.step`, `models/stl/MX-323.stl`, `drawings/parts/MX-323.svg`, `models/dxf/MX-323.dxf`
  1. Cut the developed blank from Sheet 2 mm AISI 304 (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### MX-401 - Fume extraction hood - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 1000 x 480 x 2 mm - **mass** 3.53 kg
- **Key dimensions:** Bottom width: 250; Top width: 1000; Slant height: 480.2; Thickness: 1.5; Wall angle to horizontal: 38.7 deg
- **Files:** `models/step/parts/MX-401.step`, `models/stl/MX-401.stl`, `drawings/parts/MX-401.svg`, `models/dxf/MX-401.dxf`
  1. Profile-cut from Sheet 1.5 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-402 - Fume extraction hood - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 1000 x 480 x 2 mm - **mass** 3.53 kg
- **Key dimensions:** Bottom width: 250; Top width: 1000; Slant height: 480.2; Thickness: 1.5; Wall angle to horizontal: 38.7 deg
- **Files:** `models/step/parts/MX-402.step`, `models/stl/MX-402.stl`, `drawings/parts/MX-402.svg`, `models/dxf/MX-402.dxf`
  1. Profile-cut from Sheet 1.5 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-411 - Hood wall bracket

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 50x50x5
- **Envelope:** 990 x 50 x 50 mm - **mass** 3.69 kg
- **Key dimensions:** Cut length: 990; Section: L 50 x 50 x 5
- **Files:** `models/step/parts/MX-411.step`, `models/stl/MX-411.stl`, `drawings/parts/MX-411.svg`
  1. Saw Angle 50x50x5 (S235JR) to 990 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-412 - Hood bracket wall plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 150 x 150 x 8 mm - **mass** 1.39 kg
- **Key dimensions:** Length: 150; Width: 150; Thickness: 8
- **Files:** `models/step/parts/MX-412.step`, `models/stl/MX-412.stl`, `drawings/parts/MX-412.svg`, `models/dxf/MX-412.dxf`
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### MX-420 - Spiral duct dia 200, vertical

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Galvanised spiral duct dia 200 with 250x250-to-dia-200 square/round adapter and one 90 deg bend
- **Envelope:** 200 x 200 x 150 mm - **mass** 3.00 kg
- **Files:** `models/step/parts/MX-420.step`, `models/stl/MX-420.stl`, `drawings/parts/MX-420.svg`
- **Purchase specification:** Galvanised spiral duct dia 200 with 250x250-to-dia-200 square/round adapter and one 90 deg bend
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### MX-421 - Inline extraction fan dia 200

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Inline duct fan dia 200, approx. 800 m3/h, metal casing, motor out of the air stream or rated 60 C, with weather cowl through the back wall
- **Envelope:** 300 x 260 x 260 mm - **mass** 6.00 kg
- **Files:** `models/step/parts/MX-421.step`, `models/stl/MX-421.stl`, `drawings/parts/MX-421.svg`
- **Purchase specification:** Inline duct fan dia 200, approx. 800 m3/h, metal casing, motor out of the air stream or rated 60 C, with weather cowl through the back wall
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### MX-511 - Guard frame upright

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 25x25x2
- **Envelope:** 700 x 25 x 25 mm - **mass** 1.01 kg
- **Key dimensions:** Cut length: 700; Section: 25 x 25 x 2 wall
- **Files:** `models/step/parts/MX-511.step`, `models/stl/MX-511.stl`, `drawings/parts/MX-511.svg`
  1. Saw SHS 25x25x2 (S235JR) to 700 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-512 - Guard frame rail

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 25x25x2
- **Envelope:** 850 x 25 x 25 mm - **mass** 1.23 kg
- **Key dimensions:** Cut length: 850; Section: 25 x 25 x 2 wall
- **Files:** `models/step/parts/MX-512.step`, `models/stl/MX-512.stl`, `drawings/parts/MX-512.svg`
  1. Saw SHS 25x25x2 (S235JR) to 850 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-513 - Guard mesh infill

- **Quantity in plant:** 1 - **Made in-house** - Cut to size
- **Material / stock:** S235JR - Weld mesh 25x25x2.5
- **Envelope:** 850 x 650 x 2 mm - **mass** 8.67 kg
- **Key dimensions:** Width: 850; Height: 650; Mesh: 25 x 25 x 2.5
- **Files:** `models/step/parts/MX-513.step`, `models/stl/MX-513.stl`, `drawings/parts/MX-513.svg`, `models/dxf/MX-513.dxf`
  1. Cut to size with a shear or 1 mm slitting disc, leaving the allowance noted.
  2. Dress cut wire ends; fold or frame the edges as noted.
  3. Fix with the clamp strips / stitch welds shown on the assembly sheet.

#### MX-601 - Band heater dia 462 x 70, 1.7 kW

- **Quantity in plant:** 3 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Mica or ceramic band heater, ID 462, width 70, 1.7 kW 230 V, two-piece clamp, max 350 C sheath
- **Envelope:** 486 x 486 x 70 mm - **mass** 2.50 kg
- **Files:** `models/step/parts/MX-601.step`, `models/stl/MX-601.stl`, `drawings/parts/MX-601.svg`
- **Purchase specification:** Mica or ceramic band heater, ID 462, width 70, 1.7 kW 230 V, two-piece clamp, max 350 C sheath
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### MX-602 - Base plate heater dia 340, 3 kW

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Cast-in aluminium or mica disc heater OD 340, 3 kW 400 V, clamped under the drum base
- **Envelope:** 340 x 340 x 20 mm - **mass** 6.00 kg
- **Files:** `models/step/parts/MX-602.step`, `models/stl/MX-602.stl`, `drawings/parts/MX-602.svg`
- **Purchase specification:** Cast-in aluminium or mica disc heater OD 340, 3 kW 400 V, clamped under the drum base
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### MX-701 - Mixer heater control panel

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Wall/post-mounted panel 400x500x200 IP54: 2 x PID temperature controller (drum wall, melt), 4 x SSR 25 A with heat sinks, main contactor, agitator VFD 2.2 kW, lid interlock relay, E-stop, batch timer
- **Envelope:** 400 x 208 x 500 mm - **mass** 18.00 kg
- **Files:** `models/step/parts/MX-701.step`, `models/stl/MX-701.stl`, `drawings/parts/MX-701.svg`
- **Purchase specification:** Wall/post-mounted panel 400x500x200 IP54: 2 x PID temperature controller (drum wall, melt), 4 x SSR 25 A with heat sinks, main contactor, agitator VFD 2.2 kW, lid interlock relay, E-stop, batch timer
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### MX-702 - Panel post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 1500 x 40 x 40 mm - **mass** 5.23 kg
- **Key dimensions:** Cut length: 1500; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/MX-702.step`, `models/stl/MX-702.stl`, `drawings/parts/MX-702.svg`
  1. Saw SHS 40x40x3 (S235JR) to 1500 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### MX-703 - Panel post foot

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 130 x 60 x 8 mm - **mass** 0.47 kg
- **Key dimensions:** Length: 130; Width: 60; Thickness: 8
- **Files:** `models/step/parts/MX-703.step`, `models/stl/MX-703.stl`, `drawings/parts/MX-703.svg`, `models/dxf/MX-703.dxf`
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### RC-101 - Roller table frame - leg

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 802 x 40 x 40 mm - **mass** 2.80 kg
- **Key dimensions:** Cut length: 802; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/RC-101.step`, `models/stl/RC-101.stl`, `drawings/parts/RC-101.svg`
  1. Saw SHS 40x40x3 (S235JR) to 802 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-102 - Roller table frame - long rail

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 470 x 40 x 40 mm - **mass** 1.64 kg
- **Key dimensions:** Cut length: 470; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/RC-102.step`, `models/stl/RC-102.stl`, `drawings/parts/RC-102.svg`
  1. Saw SHS 40x40x3 (S235JR) to 470 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-103 - Roller table frame - cross rail

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 920 x 40 x 40 mm - **mass** 3.21 kg
- **Key dimensions:** Cut length: 920; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/RC-103.step`, `models/stl/RC-103.stl`, `drawings/parts/RC-103.svg`
  1. Saw SHS 40x40x3 (S235JR) to 920 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-104 - Roller table frame - foot plate

- **Quantity in plant:** 8 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 60 x 130 x 8 mm - **mass** 0.47 kg
- **Key dimensions:** Length: 60; Width: 130; Thickness: 8
- **Files:** `models/step/parts/RC-104.step`, `models/stl/RC-104.stl`, `drawings/parts/RC-104.svg`, `models/dxf/RC-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### RC-111 - Roller rail 550

- **Quantity in plant:** 8 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 40x80x5
- **Envelope:** 550 x 40 x 80 mm - **mass** 2.48 kg
- **Key dimensions:** Cut length: 550; Section: L 40 x 80 x 5
- **Files:** `models/step/parts/RC-111.step`, `models/stl/RC-111.stl`, `drawings/parts/RC-111.svg`
- **Notes:** Drill dia 12.5 axle holes 50 mm above the heel: 5 at 110 pitch (first at 55) for the top level; the return level uses 3 of them. The 80 leg stands 5 mm proud of the roller tops and guides the carrier.
  1. Saw Angle 40x80x5 (S235JR) to 550 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-121 - Return rail, press section

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 80x5
- **Envelope:** 1090 x 80 x 5 mm - **mass** 3.42 kg
- **Key dimensions:** Cut length: 1090; Section: 80 x 5
- **Files:** `models/step/parts/RC-121.step`, `models/stl/RC-121.stl`, `drawings/parts/RC-121.svg`
- **Notes:** Flat on edge, welded to the two bearers in the press base. 5 x dia 12.5 axle holes at 220 pitch, first at 105, 50 above the bottom edge.
  1. Saw Flat bar 80x5 (S235JR) to 1090 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-201 - Dough scale shelf - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2.5
- **Envelope:** 682 x 30 x 30 mm - **mass** 1.47 kg
- **Key dimensions:** Cut length: 682; Section: 30 x 30 x 2.5 wall
- **Files:** `models/step/parts/RC-201.step`, `models/stl/RC-201.stl`, `drawings/parts/RC-201.svg`
  1. Saw SHS 30x30x2.5 (S235JR) to 682 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-202 - Dough scale shelf - long rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2.5
- **Envelope:** 180 x 30 x 30 mm - **mass** 0.39 kg
- **Key dimensions:** Cut length: 180; Section: 30 x 30 x 2.5 wall
- **Files:** `models/step/parts/RC-202.step`, `models/stl/RC-202.stl`, `drawings/parts/RC-202.svg`
  1. Saw SHS 30x30x2.5 (S235JR) to 180 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-203 - Dough scale shelf - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2.5
- **Envelope:** 360 x 30 x 30 mm - **mass** 0.78 kg
- **Key dimensions:** Cut length: 360; Section: 30 x 30 x 2.5 wall
- **Files:** `models/step/parts/RC-203.step`, `models/stl/RC-203.stl`, `drawings/parts/RC-203.svg`
  1. Saw SHS 30x30x2.5 (S235JR) to 360 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### RC-204 - Dough scale shelf - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 50 x 120 x 8 mm - **mass** 0.36 kg
- **Key dimensions:** Length: 50; Width: 120; Thickness: 8
- **Files:** `models/step/parts/RC-204.step`, `models/stl/RC-204.stl`, `drawings/parts/RC-204.svg`, `models/dxf/RC-204.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### RC-251 - Dough tray

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** AISI 304 - Sheet 2 mm
- **Envelope:** 240 x 380 x 60 mm - **mass** 2.57 kg
- **Key dimensions:** Inside: 236 x 376 x 58; Sheet: 2
- **Files:** `models/step/parts/RC-251.step`, `models/stl/RC-251.stl`, `drawings/parts/RC-251.svg`, `models/dxf/RC-251.dxf`
- **Notes:** Cut the 356 x 496 blank with 58 mm corner notches, fold four sides up, TIG the corners. Tare the scale with the tray on it.
  1. Cut the developed blank from Sheet 2 mm AISI 304 (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### RC-255 - Scale shelf top

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 3 mm
- **Envelope:** 240 x 420 x 3 mm - **mass** 2.37 kg
- **Key dimensions:** Length: 240; Width: 420; Thickness: 3
- **Files:** `models/step/parts/RC-255.step`, `models/stl/RC-255.stl`, `drawings/parts/RC-255.svg`, `models/dxf/RC-255.dxf`
  1. Profile-cut from Plate 3 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### RC-301 - Carrier hook tool

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Steel pull hook dia 12 x 700 with T-handle, for moving hot mould carriers and inserts
- **Envelope:** 700 x 12 x 66 mm - **mass** 0.80 kg
- **Files:** `models/step/parts/RC-301.step`, `models/stl/RC-301.stl`, `drawings/parts/RC-301.svg`
- **Purchase specification:** Steel pull hook dia 12 x 700 with T-handle, for moving hot mould carriers and inserts
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### SC-101 - Rafter

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - RHS 200x100x5
- **Envelope:** 7000 x 100 x 200 mm - **mass** 159.35 kg
- **Key dimensions:** Cut length: 7000; Section: 200 x 100 x 5; Slope: 10 deg
- **Files:** `models/step/parts/SC-101.step`, `models/stl/SC-101.stl`, `drawings/parts/SC-101.svg`
- **Notes:** Shop-weld the 7 purlin cleats on top at 1154 mm pitch (first at 40 mm from the low end) and the two post-cap seating plates underneath.
  1. Saw RHS 200x100x5 (S355J2) to 7000 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-102 - Post base plate

- **Quantity in plant:** 8 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 16 mm
- **Envelope:** 350 x 350 x 16 mm - **mass** 15.20 kg
- **Key dimensions:** Length: 350; Width: 350; Thickness: 16
- **Files:** `models/step/parts/SC-102.step`, `models/stl/SC-102.stl`, `drawings/parts/SC-102.svg`, `models/dxf/SC-102.dxf`
  1. Profile-cut from Plate 16 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (16 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SC-103 - Post cap plate

- **Quantity in plant:** 8 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 12 mm
- **Envelope:** 180 x 300 x 12 mm - **mass** 4.99 kg
- **Key dimensions:** Length: 180; Width: 300; Thickness: 12
- **Files:** `models/step/parts/SC-103.step`, `models/stl/SC-103.stl`, `drawings/parts/SC-103.svg`, `models/dxf/SC-103.dxf`
- **Notes:** Welded on the post top at 10 deg; 4 x M16 into the rafter.
  1. Profile-cut from Plate 12 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (12 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SC-104 - Knee brace, rear

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x3
- **Envelope:** 995 x 60 x 60 mm - **mass** 5.34 kg
- **Key dimensions:** Cut length: 995; Section: 60 x 60 x 3 wall
- **Files:** `models/step/parts/SC-104.step`, `models/stl/SC-104.stl`, `drawings/parts/SC-104.svg`
- **Notes:** Both ends mitred to suit post and rafter; weld all round.
  1. Saw SHS 60x60x3 (S235JR) to 995 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-105 - Knee brace, front

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x3
- **Envelope:** 818 x 60 x 60 mm - **mass** 4.39 kg
- **Key dimensions:** Cut length: 818; Section: 60 x 60 x 3 wall
- **Files:** `models/step/parts/SC-105.step`, `models/stl/SC-105.stl`, `drawings/parts/SC-105.svg`
- **Notes:** Both ends mitred to suit post and rafter; weld all round.
  1. Saw SHS 60x60x3 (S235JR) to 818 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-111 - Rear post

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - SHS 150x150x5
- **Envelope:** 3225 x 150 x 150 mm - **mass** 73.42 kg
- **Key dimensions:** Cut length: 3225; Section: 150 x 150 x 5 wall
- **Files:** `models/step/parts/SC-111.step`, `models/stl/SC-111.stl`, `drawings/parts/SC-111.svg`
- **Notes:** Top end mitred 10 deg.
  1. Saw SHS 150x150x5 (S355J2) to 3225 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-112 - Front post

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - SHS 150x150x5
- **Envelope:** 4195 x 150 x 150 mm - **mass** 95.50 kg
- **Key dimensions:** Cut length: 4195; Section: 150 x 150 x 5 wall
- **Files:** `models/step/parts/SC-112.step`, `models/stl/SC-112.stl`, `drawings/parts/SC-112.svg`
- **Notes:** Top end mitred 10 deg.
  1. Saw SHS 150x150x5 (S355J2) to 4195 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-201 - Purlin

- **Quantity in plant:** 21 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - RHS 120x60x3, hot-dip galvanised
- **Envelope:** 4590 x 60 x 120 mm - **mass** 37.62 kg
- **Key dimensions:** Cut length: 4590; Section: 120 x 60 x 3; End holes: 2 x dia 14 each end, 60 from the end
- **Files:** `models/step/parts/SC-201.step`, `models/stl/SC-201.stl`, `drawings/parts/SC-201.svg`
  1. Saw RHS 120x60x3, hot-dip galvanised (S355J2) to 4590 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-203 - Purlin cleat

- **Quantity in plant:** 28 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - Angle 100x75x8
- **Envelope:** 120 x 100 x 75 mm - **mass** 1.26 kg
- **Key dimensions:** Cut length: 120; Section: L 100 x 75 x 8
- **Files:** `models/step/parts/SC-203.step`, `models/stl/SC-203.stl`, `drawings/parts/SC-203.svg`
- **Notes:** Welded on the rafter top; each purlin end is fixed with 2 x M12.
  1. Saw Angle 100x75x8 (S355J2) to 120 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-301 - Bracing rod dia 16, rear

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - Round bar dia 16
- **Envelope:** 5201 x 16 x 16 mm - **mass** 8.21 kg
- **Key dimensions:** Cut length: 5201; Diameter: 16
- **Files:** `models/step/parts/SC-301.step`, `models/stl/SC-301.stl`, `drawings/parts/SC-301.svg`
- **Notes:** Thread M16 x 150 one end for the turnbuckle; 10 mm gusset lugs on the posts.
  1. Saw Round bar dia 16 (S355J2) to 5201 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-302 - Bracing rod dia 16, front

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S355J2 - Round bar dia 16
- **Envelope:** 5771 x 16 x 16 mm - **mass** 9.11 kg
- **Key dimensions:** Cut length: 5771; Diameter: 16
- **Files:** `models/step/parts/SC-302.step`, `models/stl/SC-302.stl`, `drawings/parts/SC-302.svg`
- **Notes:** Thread M16 x 150 one end for the turnbuckle; 10 mm gusset lugs on the posts.
  1. Saw Round bar dia 16 (S355J2) to 5771 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SC-401 - PV module 550 W

- **Quantity in plant:** 36 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Monocrystalline 550 Wp module, 144 half-cells, approx. 2278 x 1134 x 35 mm, 28 kg, Vmp ~41.7 V, Imp ~13.2 A
- **Envelope:** 2278 x 1134 x 35 mm - **mass** 28.00 kg
- **Files:** `models/step/parts/SC-401.step`, `models/stl/SC-401.stl`, `drawings/parts/SC-401.svg`
- **Purchase specification:** Monocrystalline 550 Wp module, 144 half-cells, approx. 2278 x 1134 x 35 mm, 28 kg, Vmp ~41.7 V, Imp ~13.2 A
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### SC-501 - PV combiner box

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - DC combiner: 3 strings of 12 modules (approx. 500 V, 13 A each), string fuses 20 A gPV, type 2 DC surge arrester, 1000 V DC isolator
- **Envelope:** 400 x 200 x 500 mm - **mass** 8.00 kg
- **Files:** `models/step/parts/SC-501.step`, `models/stl/SC-501.stl`, `drawings/parts/SC-501.svg`
- **Purchase specification:** DC combiner: 3 strings of 12 modules (approx. 500 V, 13 A each), string fuses 20 A gPV, type 2 DC surge arrester, 1000 V DC isolator
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### SF-101 - Sand hopper stand - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 1332 x 80 x 80 mm - **mass** 12.71 kg
- **Key dimensions:** Cut length: 1332; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/SF-101.step`, `models/stl/SF-101.stl`, `drawings/parts/SF-101.svg`
  1. Saw SHS 80x80x4 (S235JR) to 1332 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-102 - Sand hopper stand - long rail

- **Quantity in plant:** 6 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 1120 x 80 x 80 mm - **mass** 10.69 kg
- **Key dimensions:** Cut length: 1120; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/SF-102.step`, `models/stl/SF-102.stl`, `drawings/parts/SF-102.svg`
  1. Saw SHS 80x80x4 (S235JR) to 1120 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-103 - Sand hopper stand - cross rail

- **Quantity in plant:** 5 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 1120 x 80 x 80 mm - **mass** 10.69 kg
- **Key dimensions:** Cut length: 1120; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/SF-103.step`, `models/stl/SF-103.stl`, `drawings/parts/SF-103.svg`
  1. Saw SHS 80x80x4 (S235JR) to 1120 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-104 - Sand hopper stand - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 100 x 170 x 8 mm - **mass** 1.04 kg
- **Key dimensions:** Length: 100; Width: 170; Thickness: 8
- **Files:** `models/step/parts/SF-104.step`, `models/stl/SF-104.stl`, `drawings/parts/SF-104.svg`, `models/dxf/SF-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-201 - Sand receiving hopper - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Sheet 4 mm
- **Envelope:** 1100 x 819 x 4 mm - **mass** 17.36 kg
- **Key dimensions:** Bottom width: 250; Top width: 1100; Slant height: 818.9; Thickness: 4; Wall angle to horizontal: 58.7 deg
- **Files:** `models/step/parts/SF-201.step`, `models/stl/SF-201.stl`, `drawings/parts/SF-201.svg`, `models/dxf/SF-201.dxf`
  1. Profile-cut from Sheet 4 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-202 - Sand receiving hopper - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Sheet 4 mm
- **Envelope:** 1100 x 819 x 4 mm - **mass** 17.36 kg
- **Key dimensions:** Bottom width: 250; Top width: 1100; Slant height: 818.9; Thickness: 4; Wall angle to horizontal: 58.7 deg
- **Files:** `models/step/parts/SF-202.step`, `models/stl/SF-202.stl`, `drawings/parts/SF-202.svg`, `models/dxf/SF-202.dxf`
  1. Profile-cut from Sheet 4 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-203 - Hopper top band

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 4 mm
- **Envelope:** 1104 x 150 x 4 mm - **mass** 5.20 kg
- **Key dimensions:** Length: 1104; Width: 150; Thickness: 4
- **Files:** `models/step/parts/SF-203.step`, `models/stl/SF-203.stl`, `drawings/parts/SF-203.svg`, `models/dxf/SF-203.dxf`
  1. Profile-cut from Plate 4 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-204 - Hopper support rim angle

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 50x50x5
- **Envelope:** 1158 x 50 x 50 mm - **mass** 4.32 kg
- **Key dimensions:** Cut length: 1158; Section: L 50 x 50 x 5
- **Files:** `models/step/parts/SF-204.step`, `models/stl/SF-204.stl`, `drawings/parts/SF-204.svg`
- **Notes:** Welded round the hopper at the band joint; the horizontal leg sits on the stand top rails (2 x M12 per side).
  1. Saw Angle 50x50x5 (S235JR) to 1158 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-205 - Grizzly bar

- **Quantity in plant:** 11 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Round bar dia 12
- **Envelope:** 1100 x 12 x 12 mm - **mass** 0.98 kg
- **Key dimensions:** Cut length: 1100; Diameter: 12
- **Files:** `models/step/parts/SF-205.step`, `models/stl/SF-205.stl`, `drawings/parts/SF-205.svg`
  1. Saw Round bar dia 12 (S235JR) to 1100 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-206 - Grizzly end flat

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 30x5
- **Envelope:** 1100 x 30 x 5 mm - **mass** 1.30 kg
- **Key dimensions:** Cut length: 1100; Section: 30 x 5
- **Files:** `models/step/parts/SF-206.step`, `models/stl/SF-206.stl`, `drawings/parts/SF-206.svg`
  1. Saw Flat bar 30x5 (S235JR) to 1100 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-251 - Flood-feed boot

- **Quantity in plant:** 1 - **Made in-house** - Plate fabrication
- **Material / stock:** S235JR - Plate 4 mm
- **Envelope:** 258 x 258 x 360 mm - **mass** 12.49 kg
- **Key dimensions:** Inside: 250 x 250 x 356; Plate: 4; Tube penetrations: dia 117 at 45 deg, both side walls, on the boot centre line
- **Files:** `models/step/parts/SF-251.step`, `models/stl/SF-251.stl`, `drawings/parts/SF-251.svg`
- **Notes:** Fabricate from 5 flat plates (4 walls 250/258 x 360, base 258 x 258). Offer the casing tube through at 45 deg, scribe and cut the two elliptical penetrations, then seal-weld round the tube. Bolt the open top to the hopper outlet with a 30 x 5 flat flange.
  1. Cut the individual flat plates to the sizes under Key dimensions (plasma or shear).
  2. Tack together square on a flat table; offer up to the mating part and scribe any penetrations before cutting them.
  3. Weld all seams continuously (they must be dust- and sand-tight); grind inside seams smooth so material cannot hang up.

#### SF-301 - Elevating screw (45 deg) - casing tube

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD114.3 x 3.6
- **Envelope:** 3484 x 114 x 114 mm - **mass** 33.57 kg
- **Key dimensions:** Cut length: 3484; OD: 114.3; Wall: 3.6; Inlet cut-out (top): 140 x 90 at x=250; Outlet cut-out (bottom): 100 x 80 at x=3374
- **Files:** `models/step/parts/SF-301.step`, `models/stl/SF-301.stl`, `drawings/parts/SF-301.svg`
- **Notes:** Saw to length, mark and plasma/grinder-cut the inlet (top) and outlet (bottom) windows. Deburr inside.
  1. Saw Tube OD114.3 x 3.6 (S235JR) to 3484 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-302 - Elevating screw (45 deg) - end flange

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 170 x 170 x 8 mm - **mass** 1.30 kg
- **Key dimensions:** OD: 170; Thickness: 8; Bore: 45
- **Files:** `models/step/parts/SF-302.step`, `models/stl/SF-302.stl`, `drawings/parts/SF-302.svg`, `models/dxf/SF-302.dxf`
- **Notes:** Bolt pattern 70 x 70 suits UCF205. Weld square to the tube end (fillet a3 all round).
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-303 - Elevating screw (45 deg) - screw centre pipe

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD33.7 x 4
- **Envelope:** 3464 x 34 x 34 mm - **mass** 10.15 kg
- **Key dimensions:** Cut length: 3464; OD: 33.7; Wall: 4.0
- **Files:** `models/step/parts/SF-303.step`, `models/stl/SF-303.stl`, `drawings/parts/SF-303.svg`
- **Notes:** Drill 2 x dia 8 cross holes 25 mm from each end (at 90 deg to each other) for the stub-shaft pins after fitting the stubs.
  1. Saw Tube OD33.7 x 4 (S235JR) to 3464 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-304 - Elevating screw (45 deg) - tail stub shaft

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 135 x 26 x 26 mm - **mass** 0.53 kg
- **Key dimensions:** Plug dia (into pipe): 25.7 h9 x 60; Journal dia: 25 h7 x 75; Overall: 135
- **Files:** `models/step/parts/SF-304.step`, `models/stl/SF-304.stl`, `drawings/parts/SF-304.svg`
  1. Saw Round bar dia 30 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### SF-305 - Elevating screw (45 deg) - drive stub shaft

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 250 x 26 x 26 mm - **mass** 0.95 kg
- **Key dimensions:** Plug dia (into pipe): 25.7 h9 x 60; Journal dia: 25 h7 x 190; Keyway: 8 x 4 deep x 100 long; Overall: 250
- **Files:** `models/step/parts/SF-305.step`, `models/stl/SF-305.stl`, `drawings/parts/SF-305.svg`
  1. Saw Round bar dia 30 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### SF-307 - Elevating screw (45 deg) - outlet spout

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 110 x 90 x 120 mm - **mass** 1.10 kg
- **Key dimensions:** Inside: 104 x 84; Height: 120; Sheet: 3
- **Files:** `models/step/parts/SF-307.step`, `models/stl/SF-307.stl`, `drawings/parts/SF-307.svg`, `models/dxf/SF-307.dxf`
- **Notes:** Fold from one strip (developed length 388) and seam-weld; scribe to the tube and weld all round.
  1. Cut the developed blank from Sheet 3 mm S235JR (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### SF-401 - Overhead transfer screw - casing tube

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD114.3 x 3.6
- **Envelope:** 3060 x 114 x 114 mm - **mass** 29.41 kg
- **Key dimensions:** Cut length: 3060; OD: 114.3; Wall: 3.6; Inlet cut-out (top): 140 x 90 at x=250; Outlet cut-out (bottom): 100 x 80 at x=2950
- **Files:** `models/step/parts/SF-401.step`, `models/stl/SF-401.stl`, `drawings/parts/SF-401.svg`
- **Notes:** Saw to length, mark and plasma/grinder-cut the inlet (top) and outlet (bottom) windows. Deburr inside.
  1. Saw Tube OD114.3 x 3.6 (S235JR) to 3060 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-402 - Overhead transfer screw - end flange

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 170 x 170 x 8 mm - **mass** 1.30 kg
- **Key dimensions:** OD: 170; Thickness: 8; Bore: 45
- **Files:** `models/step/parts/SF-402.step`, `models/stl/SF-402.stl`, `drawings/parts/SF-402.svg`, `models/dxf/SF-402.dxf`
- **Notes:** Bolt pattern 70 x 70 suits UCF205. Weld square to the tube end (fillet a3 all round).
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-403 - Overhead transfer screw - screw centre pipe

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD33.7 x 4
- **Envelope:** 3040 x 34 x 34 mm - **mass** 8.91 kg
- **Key dimensions:** Cut length: 3040; OD: 33.7; Wall: 4.0
- **Files:** `models/step/parts/SF-403.step`, `models/stl/SF-403.stl`, `drawings/parts/SF-403.svg`
- **Notes:** Drill 2 x dia 8 cross holes 25 mm from each end (at 90 deg to each other) for the stub-shaft pins after fitting the stubs.
  1. Saw Tube OD33.7 x 4 (S235JR) to 3040 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-404 - Overhead transfer screw - tail stub shaft

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 135 x 26 x 26 mm - **mass** 0.53 kg
- **Key dimensions:** Plug dia (into pipe): 25.7 h9 x 60; Journal dia: 25 h7 x 75; Overall: 135
- **Files:** `models/step/parts/SF-404.step`, `models/stl/SF-404.stl`, `drawings/parts/SF-404.svg`
  1. Saw Round bar dia 30 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### SF-405 - Overhead transfer screw - drive stub shaft

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 250 x 26 x 26 mm - **mass** 0.95 kg
- **Key dimensions:** Plug dia (into pipe): 25.7 h9 x 60; Journal dia: 25 h7 x 190; Keyway: 8 x 4 deep x 100 long; Overall: 250
- **Files:** `models/step/parts/SF-405.step`, `models/stl/SF-405.stl`, `drawings/parts/SF-405.svg`
  1. Saw Round bar dia 30 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### SF-406 - Overhead transfer screw - inlet stub

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 150 x 100 x 90 mm - **mass** 1.03 kg
- **Key dimensions:** Inside: 144 x 94; Height: 90; Sheet: 3
- **Files:** `models/step/parts/SF-406.step`, `models/stl/SF-406.stl`, `drawings/parts/SF-406.svg`, `models/dxf/SF-406.dxf`
- **Notes:** Fold from one strip (developed length 488) and seam-weld; scribe the bottom to the tube and weld all round.
  1. Cut the developed blank from Sheet 3 mm S235JR (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### SF-407 - Overhead transfer screw - outlet spout

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 110 x 90 x 400 mm - **mass** 3.65 kg
- **Key dimensions:** Inside: 104 x 84; Height: 400; Sheet: 3
- **Files:** `models/step/parts/SF-407.step`, `models/stl/SF-407.stl`, `drawings/parts/SF-407.svg`, `models/dxf/SF-407.dxf`
- **Notes:** Fold from one strip (developed length 388) and seam-weld; scribe to the tube and weld all round.
  1. Cut the developed blank from Sheet 3 mm S235JR (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### SF-501 - Elevating screw support post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 2052 x 80 x 80 mm - **mass** 19.59 kg
- **Key dimensions:** Cut length: 2052; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/SF-501.step`, `models/stl/SF-501.stl`, `drawings/parts/SF-501.svg`
  1. Saw SHS 80x80x4 (S235JR) to 2052 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SF-502 - Post base plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 250 x 250 x 10 mm - **mass** 4.83 kg
- **Key dimensions:** Length: 250; Width: 250; Thickness: 10
- **Files:** `models/step/parts/SF-502.step`, `models/stl/SF-502.stl`, `drawings/parts/SF-502.svg`, `models/dxf/SF-502.dxf`
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-503 - Post saddle plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 160 x 160 x 10 mm - **mass** 1.99 kg
- **Key dimensions:** Length: 160; Width: 160; Thickness: 10
- **Files:** `models/step/parts/SF-503.step`, `models/stl/SF-503.stl`, `drawings/parts/SF-503.svg`, `models/dxf/SF-503.dxf`
- **Notes:** Welded on the post top; the casing tube is held down with an M12 U-bolt (DN100) over a 45 deg steel wedge packer about 65 mm high, made to suit on site.
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SF-511 - Transfer screw support post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 2243 x 80 x 80 mm - **mass** 21.41 kg
- **Key dimensions:** Cut length: 2243; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/SF-511.step`, `models/stl/SF-511.stl`, `drawings/parts/SF-511.svg`
  1. Saw SHS 80x80x4 (S235JR) to 2243 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SH-101 - Shredder frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 792 x 60 x 60 mm - **mass** 5.57 kg
- **Key dimensions:** Cut length: 792; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/SH-101.step`, `models/stl/SH-101.stl`, `drawings/parts/SH-101.svg`
  1. Saw SHS 60x60x4 (S235JR) to 792 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SH-102 - Shredder frame - long rail

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 680 x 60 x 60 mm - **mass** 4.78 kg
- **Key dimensions:** Cut length: 680; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/SH-102.step`, `models/stl/SH-102.stl`, `drawings/parts/SH-102.svg`
  1. Saw SHS 60x60x4 (S235JR) to 680 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SH-103 - Shredder frame - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 60x60x4
- **Envelope:** 830 x 60 x 60 mm - **mass** 5.84 kg
- **Key dimensions:** Cut length: 830; Section: 60 x 60 x 4 wall
- **Files:** `models/step/parts/SH-103.step`, `models/stl/SH-103.stl`, `drawings/parts/SH-103.svg`
  1. Saw SHS 60x60x4 (S235JR) to 830 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SH-104 - Shredder frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 80 x 150 x 8 mm - **mass** 0.73 kg
- **Key dimensions:** Length: 80; Width: 150; Thickness: 8
- **Files:** `models/step/parts/SH-104.step`, `models/stl/SH-104.stl`, `drawings/parts/SH-104.svg`, `models/dxf/SH-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-201 - Shredder deck plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 800 x 950 x 10 mm - **mass** 50.13 kg
- **Key dimensions:** Length: 800; Width: 950; Thickness: 10
- **Files:** `models/step/parts/SH-201.step`, `models/stl/SH-201.stl`, `drawings/parts/SH-201.svg`, `models/dxf/SH-201.dxf`
- **Notes:** Stitch-weld to the frame top (50 every 150). The dia 260 hole clears the gearmotor; the 222 x 304 window is the flake discharge.
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-211 - Chamber end plate (bearing plate)

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 15 mm
- **Envelope:** 244 x 250 x 15 mm - **mass** 6.88 kg
- **Key dimensions:** Length: 244; Width: 250; Thickness: 15
- **Files:** `models/step/parts/SH-211.step`, `models/stl/SH-211.stl`, `drawings/parts/SH-211.svg`, `models/dxf/SH-211.dxf`
- **Notes:** Bore dia 50 and the 4 x dia 14 (92 x 92, UCF207) must be positioned within 0.2 mm - drill both plates clamped together.
  1. Profile-cut from Plate 15 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (15 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-212 - Chamber side plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 12 mm
- **Envelope:** 302 x 250 x 12 mm - **mass** 7.11 kg
- **Key dimensions:** Length: 302; Width: 250; Thickness: 12
- **Files:** `models/step/parts/SH-212.step`, `models/stl/SH-212.stl`, `drawings/parts/SH-212.svg`, `models/dxf/SH-212.dxf`
  1. Profile-cut from Plate 12 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-213 - Chamber flange (top / bottom)

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 344 x 432 x 10 mm - **mass** 6.31 kg
- **Key dimensions:** Length: 344; Width: 432; Thickness: 10
- **Files:** `models/step/parts/SH-213.step`, `models/stl/SH-213.stl`, `drawings/parts/SH-213.svg`, `models/dxf/SH-213.dxf`
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-221 - Rotor shaft (hex 36 A/F)

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Hexagon bar 36 A/F
- **Envelope:** 642 x 42 x 36 mm - **mass** 5.16 kg
- **Key dimensions:** Overall length: 642; Hex section: 36 A/F x 300 (left as drawn bar); Drive journal: dia 35 k6 x 276; Front journal: dia 35 k6 x 66; Keyway: 10 P9 x 5 deep x 170 (for 10x8 key)
- **Files:** `models/step/parts/SH-221.step`, `models/stl/SH-221.stl`, `drawings/parts/SH-221.svg`
  1. Saw hexagon bar 36 A/F (C45, bright drawn) to 646 mm.
  2. Lathe, 3-jaw on the hex with soft jaws: face and centre-drill both ends to 642 mm overall.
  3. Between centres: turn the drive end to dia 35 k6 for 276 mm and the front end to dia 35 k6 for 66 mm. Leave R1 fillets at the hex shoulders; do not touch the hex section.
  4. Mill the 10 P9 x 5 deep keyway, 170 long, starting 12 mm from the drive end.
  5. Deburr, check both journals run true to each other within 0.05 mm TIR.

#### SH-231 - Rotary knife, type A (hex at 0 deg)

- **Quantity in plant:** 5 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** Hardox 450 - Plate 10 mm
- **Envelope:** 168 x 162 x 10 mm - **mass** 1.34 kg
- **Key dimensions:** Tip circle: 180; Root circle: 124; Thickness: 10; Hex bore: 36.2 A/F; Hex rotation: 0 deg; Teeth: 3
- **Files:** `models/step/parts/SH-231.step`, `models/stl/SH-231.stl`, `drawings/parts/SH-231.svg`, `models/dxf/SH-231.dxf`
- **Notes:** Laser or waterjet cut from Hardox 450 (do NOT plasma cut - the heat softens the edge). Surface-grind both faces only if the plate is not flat within 0.2 mm. Grind a 5 deg relief behind each hook tip. The three types differ only in the angle of the hex bore, which staggers the teeth into a helix.
  1. Laser or waterjet cut from 10 mm Hardox 450 using the DXF (never plasma - the heat-affected edge loses hardness).
  2. Deburr. Check the hex bore with the 36 A/F shaft bar: sliding fit, no more than 0.3 mm play.
  3. Stack all 15 knives and 15 spacers on the shaft and measure the stack: 300.0 +/-0.3 mm. Surface-grind individual knives if needed.
  4. Grind a 5 deg clearance behind each of the three hook tips with a flap disc; keep the tips cool (dip in water) so they stay hard.
  5. Assembly order along the shaft: A, B, C, A, B, C ... so the teeth form a helix and only one or two teeth cut at a time.

#### SH-232 - Rotary knife, type B (hex at 20 deg)

- **Quantity in plant:** 5 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** Hardox 450 - Plate 10 mm
- **Envelope:** 168 x 162 x 10 mm - **mass** 1.34 kg
- **Key dimensions:** Tip circle: 180; Root circle: 124; Thickness: 10; Hex bore: 36.2 A/F; Hex rotation: 20 deg; Teeth: 3
- **Files:** `models/step/parts/SH-232.step`, `models/stl/SH-232.stl`, `drawings/parts/SH-232.svg`, `models/dxf/SH-232.dxf`
- **Notes:** Laser or waterjet cut from Hardox 450 (do NOT plasma cut - the heat softens the edge). Surface-grind both faces only if the plate is not flat within 0.2 mm. Grind a 5 deg relief behind each hook tip. The three types differ only in the angle of the hex bore, which staggers the teeth into a helix.
  1. Laser or waterjet cut from 10 mm Hardox 450 using the DXF (never plasma - the heat-affected edge loses hardness).
  2. Deburr. Check the hex bore with the 36 A/F shaft bar: sliding fit, no more than 0.3 mm play.
  3. Stack all 15 knives and 15 spacers on the shaft and measure the stack: 300.0 +/-0.3 mm. Surface-grind individual knives if needed.
  4. Grind a 5 deg clearance behind each of the three hook tips with a flap disc; keep the tips cool (dip in water) so they stay hard.
  5. Assembly order along the shaft: A, B, C, A, B, C ... so the teeth form a helix and only one or two teeth cut at a time.

#### SH-233 - Rotary knife, type C (hex at 40 deg)

- **Quantity in plant:** 5 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** Hardox 450 - Plate 10 mm
- **Envelope:** 168 x 162 x 10 mm - **mass** 1.34 kg
- **Key dimensions:** Tip circle: 180; Root circle: 124; Thickness: 10; Hex bore: 36.2 A/F; Hex rotation: 40 deg; Teeth: 3
- **Files:** `models/step/parts/SH-233.step`, `models/stl/SH-233.stl`, `drawings/parts/SH-233.svg`, `models/dxf/SH-233.dxf`
- **Notes:** Laser or waterjet cut from Hardox 450 (do NOT plasma cut - the heat softens the edge). Surface-grind both faces only if the plate is not flat within 0.2 mm. Grind a 5 deg relief behind each hook tip. The three types differ only in the angle of the hex bore, which staggers the teeth into a helix.
  1. Laser or waterjet cut from 10 mm Hardox 450 using the DXF (never plasma - the heat-affected edge loses hardness).
  2. Deburr. Check the hex bore with the 36 A/F shaft bar: sliding fit, no more than 0.3 mm play.
  3. Stack all 15 knives and 15 spacers on the shaft and measure the stack: 300.0 +/-0.3 mm. Surface-grind individual knives if needed.
  4. Grind a 5 deg clearance behind each of the three hook tips with a flap disc; keep the tips cool (dip in water) so they stay hard.
  5. Assembly order along the shaft: A, B, C, A, B, C ... so the teeth form a helix and only one or two teeth cut at a time.

#### SH-234 - Rotor spacer

- **Quantity in plant:** 15 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 10 mm
- **Envelope:** 64 x 64 x 10 mm - **mass** 0.16 kg
- **Key dimensions:** OD: 64; Thickness: 10; Hex bore: 36.2 A/F
- **Files:** `models/step/parts/SH-234.step`, `models/stl/SH-234.stl`, `drawings/parts/SH-234.svg`, `models/dxf/SH-234.dxf`
- **Notes:** Must be the same thickness as the knives within 0.05 mm; cut both from the same plate.
  1. Profile-cut from Plate 10 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-241 - Fixed comb (counter knife)

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** Hardox 450 - Plate 10 mm
- **Envelope:** 76 x 300 x 10 mm - **mass** 0.93 kg
- **Key dimensions:** Length: 76; Width: 300; Thickness: 10
- **Files:** `models/step/parts/SH-241.step`, `models/stl/SH-241.stl`, `drawings/parts/SH-241.svg`, `models/dxf/SH-241.dxf`
- **Notes:** Fingers are 8 mm wide and sit in the gaps between the rotary knives with 1 mm side clearance. 3 x dia 11 holes on the back strip are match-drilled from the support angle on assembly; shim so the finger tips clear the spacers by 2 mm.
  1. Profile-cut from Plate 10 mm Hardox 450 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-242 - Comb support angle

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 40x40x5
- **Envelope:** 302 x 40 x 40 mm - **mass** 0.89 kg
- **Key dimensions:** Cut length: 302; Section: L 40 x 40 x 5
- **Files:** `models/step/parts/SH-242.step`, `models/stl/SH-242.stl`, `drawings/parts/SH-242.svg`
- **Notes:** Weld inside the chamber, top face 10 mm below shaft centre. Drill and tap 3 x M10 at 100 pitch through the horizontal leg, 20 from the heel.
  1. Saw Angle 40x40x5 (S235JR) to 302 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### SH-251 - Screen, dia 8 perforation

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, roll, weld seam
- **Material / stock:** S355J2 - Sheet 4 mm
- **Envelope:** 300 x 202 x 87 mm - **mass** 2.68 kg
- **Key dimensions:** Inside radius: 98; Length: 300; Flat blank: 284 x 300; Perforation: dia 8 holes, 12 mm staggered pitch
- **Files:** `models/step/parts/SH-251.step`, `models/stl/SH-251.stl`, `drawings/parts/SH-251.svg`, `models/dxf/SH-251.dxf`
- **Notes:** Laser the perforated blank flat (DXF), then roll to R98 inside with the burr side outward. Sits in the comb support angles; held by 2 x M8 each side.
  1. Cut the flat blank (284 x 300 mm) from Sheet 4 mm S355J2; DXF supplied.
  2. Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.
  3. Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.
  4. Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.
  5. Pass through the rolls once more to correct weld distortion.

#### SH-2601 - Shredder feed hopper - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 700 x 427 x 3 mm - **mass** 4.62 kg
- **Key dimensions:** Bottom width: 220; Top width: 700; Slant height: 426.9; Thickness: 3; Wall angle to horizontal: 69.6 deg
- **Files:** `models/step/parts/SH-2601.step`, `models/stl/SH-2601.stl`, `drawings/parts/SH-2601.svg`, `models/dxf/SH-2601.dxf`
  1. Profile-cut from Sheet 3 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-2602 - Shredder feed hopper - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 600 x 466 x 3 mm - **mass** 4.95 kg
- **Key dimensions:** Bottom width: 302; Top width: 600; Slant height: 466.5; Thickness: 3; Wall angle to horizontal: 59.0 deg
- **Files:** `models/step/parts/SH-2602.step`, `models/stl/SH-2602.stl`, `drawings/parts/SH-2602.svg`, `models/dxf/SH-2602.dxf`
  1. Profile-cut from Sheet 3 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-263 - Hopper flange

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 6 mm
- **Envelope:** 344 x 432 x 6 mm - **mass** 3.83 kg
- **Key dimensions:** Length: 344; Width: 432; Thickness: 6
- **Files:** `models/step/parts/SH-263.step`, `models/stl/SH-263.stl`, `drawings/parts/SH-263.svg`, `models/dxf/SH-263.dxf`
  1. Profile-cut from Plate 6 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (6 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-271 - Discharge skirt

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 226 x 308 x 300 mm - **mass** 4.99 kg
- **Key dimensions:** Inside: 222 x 304; Height: 300; Sheet: 2
- **Files:** `models/step/parts/SH-271.step`, `models/stl/SH-271.stl`, `drawings/parts/SH-271.svg`, `models/dxf/SH-271.dxf`
- **Notes:** Fold from one strip 1060 x 300 with a 20 mm top flange on each side; spot/stitch-weld the seam. Screw to the underside of the deck.
  1. Cut the developed blank from Sheet 2 mm DC01 galv. (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### SH-281 - Gearmotor torque arm

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 80 x 180 x 10 mm - **mass** 1.10 kg
- **Key dimensions:** Length: 80; Width: 180; Thickness: 10
- **Files:** `models/step/parts/SH-281.step`, `models/stl/SH-281.stl`, `drawings/parts/SH-281.svg`, `models/dxf/SH-281.dxf`
- **Notes:** Bolts to the gearbox torque-arm lug; the dia 17 end takes an M16 bolt with rubber bushes anchored to the deck.
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### SH-291 - Control post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x3
- **Envelope:** 500 x 40 x 40 mm - **mass** 1.74 kg
- **Key dimensions:** Cut length: 500; Section: 40 x 40 x 3 wall
- **Files:** `models/step/parts/SH-291.step`, `models/stl/SH-291.stl`, `drawings/parts/SH-291.svg`
  1. Saw SHS 40x40x3 (S235JR) to 500 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### ST-101 - Sorting table frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x2.5
- **Envelope:** 822 x 40 x 40 mm - **mass** 2.42 kg
- **Key dimensions:** Cut length: 822; Section: 40 x 40 x 2.5 wall
- **Files:** `models/step/parts/ST-101.step`, `models/stl/ST-101.stl`, `drawings/parts/ST-101.svg`
  1. Saw SHS 40x40x2.5 (S235JR) to 822 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### ST-102 - Sorting table frame - long rail

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x2.5
- **Envelope:** 820 x 40 x 40 mm - **mass** 2.41 kg
- **Key dimensions:** Cut length: 820; Section: 40 x 40 x 2.5 wall
- **Files:** `models/step/parts/ST-102.step`, `models/stl/ST-102.stl`, `drawings/parts/ST-102.svg`
  1. Saw SHS 40x40x2.5 (S235JR) to 820 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### ST-103 - Sorting table frame - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x2.5
- **Envelope:** 520 x 40 x 40 mm - **mass** 1.53 kg
- **Key dimensions:** Cut length: 520; Section: 40 x 40 x 2.5 wall
- **Files:** `models/step/parts/ST-103.step`, `models/stl/ST-103.stl`, `drawings/parts/ST-103.svg`
  1. Saw SHS 40x40x2.5 (S235JR) to 520 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### ST-104 - Sorting table frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 60 x 130 x 8 mm - **mass** 0.47 kg
- **Key dimensions:** Length: 60; Width: 130; Thickness: 8
- **Files:** `models/step/parts/ST-104.step`, `models/stl/ST-104.stl`, `drawings/parts/ST-104.svg`, `models/dxf/ST-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### ST-201 - Sorting table top

- **Quantity in plant:** 1 - **Made in-house** - Cut to size (saw/router)
- **Material / stock:** HDPE - HDPE board 20 mm
- **Envelope:** 940 x 640 x 20 mm - **mass** 11.43 kg
- **Key dimensions:** Length: 940; Width: 640; Thickness: 20
- **Files:** `models/step/parts/ST-201.step`, `models/stl/ST-201.stl`, `drawings/parts/ST-201.svg`, `models/dxf/ST-201.dxf`
- **Notes:** Fix to the top rails with 8 x M6x50 countersunk screws into rivet nuts. Break all edges R3.
  1. Cut from HDPE board 20 mm with a fine-tooth circular saw or router to the sizes given.
  2. Drill fixing holes on assembly (match-drill from the frame).
  3. Round or flame-polish the exposed edges.

#### ST-301 - Reject bin 80 L, red

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - 80 L rigid PP bin, RED, labelled "PVC / PET / unknown - REJECT"
- **Envelope:** 400 x 400 x 600 mm - **mass** 3.50 kg
- **Files:** `models/step/parts/ST-301.step`, `models/stl/ST-301.stl`, `drawings/parts/ST-301.svg`
- **Purchase specification:** 80 L rigid PP bin, RED, labelled "PVC / PET / unknown - REJECT"
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### ST-302 - HDPE bin 80 L, green

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - 80 L rigid PP bin, GREEN, labelled "HDPE only"
- **Envelope:** 400 x 400 x 600 mm - **mass** 3.50 kg
- **Files:** `models/step/parts/ST-302.step`, `models/stl/ST-302.stl`, `drawings/parts/ST-302.svg`
- **Purchase specification:** 80 L rigid PP bin, GREEN, labelled "HDPE only"
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### TL-001 - Roof tile, double-roman, plastic-sand

- **Quantity in plant:** 37 - **Made in-house** - Compression moulded
- **Material / stock:** Plastic-sand composite - 70 % dry sand + 30 % HDPE by weight
- **Envelope:** 330 x 420 x 52 mm - **mass** 2.19 kg
- **Key dimensions:** Length: 420.0; Cover width: 330.0; Wall thickness: 8.0; Roll height: 40.0; Hanging nibs: 2 x 30 x 20 x 12; Calculated mass: 2.19 kg at 1.72 g/cm3; Profile, centre line (x across the width): x 0-30: side rim falling 14 to 0 (half cosine); 30-80 flat pan; 80-180 roll, 32 high (full cosine); 180-235 flat pan; 235-330 second roll, 32 high, cut off at x=330 (the overlap edge); Wall: 8 mm measured normal to the centre line, constant; Nib positions: under the pans at x = 55 and 207, 15-35 mm from the head end
- **Files:** `models/step/parts/TL-001.step`, `models/stl/TL-001.stl`, `drawings/parts/TL-001.svg`
- **Notes:** The product. Compression-moulded upside down: weather face in the aluminium cavity insert, underside and nibs formed by the punch.
  1. Charge: weigh 2.25 kg of hot mix (190-200 C) per cavity on the dough scale; shape it roughly into a 350 x 250 slab with the steel paddle. Work fast - the mix skins over in under a minute.
  2. Place one charge in the middle of each cavity insert on the charge table. Brush insert and punch thinly with mould release every 5-10 cycles.
  3. Roll the carrier into the press against the end stop. Two-hand start: fast approach, then press at 180-210 bar (about 3.5 MPa on the tile) until the punch lands close on the insert.
  4. Hold under pressure for 60-90 s (to be validated) so the skin freezes, then open the press.
  5. Roll the carrier out and lift each insert with its tile to the cooling rack. Air-cool about 20 min until the tile is below 60 C and has shrunk free of the cavity.
  6. Tip the tile out, trim the flash at the trim station, check for cracks, voids and short shots, weigh (2.1-2.3 kg). Rejects and flash go to the regrind tote.
  7. Stack flat on the pallet, at most 10 high per stack, and leave 24 h before loading or testing.

#### TL-101 - Cavity insert (lower mould half)

- **Quantity in plant:** 10 - **Made in-house** - Sand cast + CNC finish
- **Material / stock:** Al A356-T6 - Sand casting, or 5083 tooling plate 80 mm
- **Envelope:** 470 x 380 x 75 mm - **mass** 18.73 kg
- **Key dimensions:** Block: 470 x 380 x 75; Pocket plan: 421 x 331 (tile + 0.5 mm per side); Min. floor under roll crowns: 15; Shut-off depth above tile: 20; Lightening pockets (underside): 2 x 380 x 40 x 33; Finger grooves: 2 x 120 x 14 x 12
- **Files:** `models/step/parts/TL-101.step`, `models/stl/TL-101.stl`, `drawings/parts/TL-101.svg`
- **Notes:** 10 off: two are in the press while eight cool in the rack. Machine the cavity directly from the STEP surface. Hard-anodise 50 micron (or electroless nickel) for abrasion resistance; polish the cavity to Ra 0.8.
  1. Pattern: CNC-rout or 3D-print the insert shape from the STL (models/stl/TL-101.stl) scaled 1.013 for aluminium shrinkage, with 3 mm machining allowance on the cavity, top and bottom faces and 2 deg draft on the outside walls.
  2. Sand-cast in A356 (AlSi7Mg0.3), degassed and grain-refined; heat treat to T6. Reject castings with visible porosity in the cavity. Alternative without a foundry: machine from 80 mm 5083 or MIC-6 tooling plate - same CNC program, no heat treatment.
  3. Mill the underside flat, then flip onto that face and mill the block to 470 x 380 x 75. Machine the two underside lightening pockets and the two finger grooves.
  4. 3-axis CNC the cavity from the STEP model: rough with a dia 16 end mill leaving 0.5 mm, finish the profiled floor with a dia 12 ball-nose at 0.3 mm step-over along the tile length. The pocket walls are vertical: finish with a dia 10 end mill, corner radius 5.
  5. Polish the cavity floor along the tile length to Ra 0.8 or better (wet paper 240-600) - the floor is the weather face of the tile.
  6. Hard-anodise 50 micron (or electroless nickel 25 micron). Stamp the insert number 1-10 on the front edge so defects can be traced to a cavity.
  7. Inspect: pocket 421 x 331 +0.2/0, depth to the pan area 28.0 +/-0.1, underside flat within 0.1 mm.

#### TL-102 - Punch (upper mould half)

- **Quantity in plant:** 2 - **Made in-house** - 3-axis CNC surface machined
- **Material / stock:** S355J2 - Plate 100 mm
- **Envelope:** 470 x 380 x 90 mm - **mass** 84.86 kg
- **Key dimensions:** Base: 470 x 380 x 35; Boss plan: 420.2 x 330.2 (0.4 mm shear gap per side to the pocket); Kiss-off lands: 2 x 470 x 20 x 3 high; Nib pockets: 2 x 30.6 x 20.6 x 12.5 deep, 5 deg draft
- **Files:** `models/step/parts/TL-102.step`, `models/stl/TL-102.stl`, `drawings/parts/TL-102.svg`
- **Notes:** 2 off, bolted under the upper bolster. The two 3 mm lands close on the insert top face and fix the tile thickness; flash escapes at the ends. Drill and tap 6 x M12 x 25 deep in the back face (pattern 400 x 150) for the bolster screws.
  1. Saw a 480 x 390 blank from 100 mm S355J2 plate (or P20 if the budget allows). Mill both faces parallel to 98 mm, square the edges to 470 x 380.
  2. Back face: drill and tap 6 x M12 x 25 deep (400 x 150 pattern) for the bolster screws; these also hold the block for the next operations.
  3. Bolt to a fixture plate, back face down. Rough-mill around the boss to leave the 35 mm base and the two 3 mm kiss-off lands (470 x 20) along the long edges.
  4. 3-axis CNC the boss from the STEP model: rough with dia 16, finish the profiled face with a dia 12 ball-nose at 0.3 mm step-over along the tile length. Finish the vertical boss walls to 420.2 x 330.2 (-0.1/0) with 0.5 mm edge break.
  5. Machine the two nib pockets 30.6 x 20.6 x 12.5 deep with 5 deg draft on all four walls and R2 corners; polish them - nibs that stick will tear off.
  6. Polish the moulding face to Ra 1.6. Optional: gas-nitride for wear resistance.
  7. Trial-fit in an insert with 0.4 mm feeler gauges all round; the two lands must touch the insert top face together (blue check).

#### TL-111 - Carrier base plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S355J2 - Plate 10 mm
- **Envelope:** 540 x 840 x 10 mm - **mass** 35.55 kg
- **Key dimensions:** Length: 540; Width: 840; Thickness: 10
- **Files:** `models/step/parts/TL-111.step`, `models/stl/TL-111.stl`, `drawings/parts/TL-111.svg`, `models/dxf/TL-111.dxf`
- **Notes:** 2 x dia 22 pull holes for the hook tool.
  1. Profile-cut from Plate 10 mm S355J2 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### TL-112 - Carrier long rim bar

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 20x15
- **Envelope:** 822 x 20 x 15 mm - **mass** 1.94 kg
- **Key dimensions:** Cut length: 822; Section: 20 x 15
- **Files:** `models/step/parts/TL-112.step`, `models/stl/TL-112.stl`, `drawings/parts/TL-112.svg`
  1. Saw Flat bar 20x15 (S235JR) to 822 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TL-113 - Carrier cross rim bar

- **Quantity in plant:** 6 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 20x15
- **Envelope:** 471 x 20 x 15 mm - **mass** 1.11 kg
- **Key dimensions:** Cut length: 471; Section: 20 x 15
- **Files:** `models/step/parts/TL-113.step`, `models/stl/TL-113.stl`, `drawings/parts/TL-113.svg`
  1. Saw Flat bar 20x15 (S235JR) to 471 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-101 - Trim table frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x2.5
- **Envelope:** 838 x 40 x 40 mm - **mass** 2.47 kg
- **Key dimensions:** Cut length: 838; Section: 40 x 40 x 2.5 wall
- **Files:** `models/step/parts/TR-101.step`, `models/stl/TR-101.stl`, `drawings/parts/TR-101.svg`
  1. Saw SHS 40x40x2.5 (S235JR) to 838 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-102 - Trim table frame - long rail

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x2.5
- **Envelope:** 770 x 40 x 40 mm - **mass** 2.27 kg
- **Key dimensions:** Cut length: 770; Section: 40 x 40 x 2.5 wall
- **Files:** `models/step/parts/TR-102.step`, `models/stl/TR-102.stl`, `drawings/parts/TR-102.svg`
  1. Saw SHS 40x40x2.5 (S235JR) to 770 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-103 - Trim table frame - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 40x40x2.5
- **Envelope:** 620 x 40 x 40 mm - **mass** 1.83 kg
- **Key dimensions:** Cut length: 620; Section: 40 x 40 x 2.5 wall
- **Files:** `models/step/parts/TR-103.step`, `models/stl/TR-103.stl`, `drawings/parts/TR-103.svg`
  1. Saw SHS 40x40x2.5 (S235JR) to 620 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-104 - Trim table frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 60 x 130 x 8 mm - **mass** 0.47 kg
- **Key dimensions:** Length: 60; Width: 130; Thickness: 8
- **Files:** `models/step/parts/TR-104.step`, `models/stl/TR-104.stl`, `drawings/parts/TR-104.svg`, `models/dxf/TR-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### TR-201 - Trim table top

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 4 mm
- **Envelope:** 890 x 740 x 4 mm - **mass** 19.81 kg
- **Key dimensions:** Length: 890; Width: 740; Thickness: 4
- **Files:** `models/step/parts/TR-201.step`, `models/stl/TR-201.stl`, `drawings/parts/TR-201.svg`, `models/dxf/TR-201.dxf`
- **Notes:** Dia 40 hole for the trim spindle, 220 x 120 slot for offcuts. Powder-coat white so cracks and voids show up against it.
  1. Profile-cut from Plate 4 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (4 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### TR-2101 - Offcut funnel - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 260 x 181 x 2 mm - **mass** 0.41 kg
- **Key dimensions:** Bottom width: 120; Top width: 260; Slant height: 181.1; Thickness: 1.5; Wall angle to horizontal: 83.7 deg
- **Files:** `models/step/parts/TR-2101.step`, `models/stl/TR-2101.stl`, `drawings/parts/TR-2101.svg`, `models/dxf/TR-2101.dxf`
  1. Profile-cut from Sheet 1.5 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### TR-2102 - Offcut funnel - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 160 x 193 x 2 mm - **mass** 0.32 kg
- **Key dimensions:** Bottom width: 120; Top width: 160; Slant height: 193.1; Thickness: 1.5; Wall angle to horizontal: 68.7 deg
- **Files:** `models/step/parts/TR-2102.step`, `models/stl/TR-2102.stl`, `drawings/parts/TR-2102.svg`, `models/dxf/TR-2102.dxf`
  1. Profile-cut from Sheet 1.5 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### TR-301 - Trim spindle 0.75 kW with carbide burr

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Router / die-grinder spindle 0.75 kW, 10 000-20 000 rpm variable, under-table mount, with dia 12 x 30 cylindrical carbide burr and guide bearing; foot switch
- **Envelope:** 80 x 80 x 295 mm - **mass** 4.00 kg
- **Files:** `models/step/parts/TR-301.step`, `models/stl/TR-301.stl`, `drawings/parts/TR-301.svg`
- **Purchase specification:** Router / die-grinder spindle 0.75 kW, 10 000-20 000 rpm variable, under-table mount, with dia 12 x 30 cylindrical carbide burr and guide bearing; foot switch
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### TR-311 - Guard post

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 25x25x2
- **Envelope:** 380 x 25 x 25 mm - **mass** 0.55 kg
- **Key dimensions:** Cut length: 380; Section: 25 x 25 x 2 wall
- **Files:** `models/step/parts/TR-311.step`, `models/stl/TR-311.stl`, `drawings/parts/TR-311.svg`
  1. Saw SHS 25x25x2 (S235JR) to 380 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-312 - Guard top rail, long

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 25x25x2
- **Envelope:** 550 x 25 x 25 mm - **mass** 0.79 kg
- **Key dimensions:** Cut length: 550; Section: 25 x 25 x 2 wall
- **Files:** `models/step/parts/TR-312.step`, `models/stl/TR-312.stl`, `drawings/parts/TR-312.svg`
  1. Saw SHS 25x25x2 (S235JR) to 550 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-313 - Guard top rail, short

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 25x25x2
- **Envelope:** 400 x 25 x 25 mm - **mass** 0.58 kg
- **Key dimensions:** Cut length: 400; Section: 25 x 25 x 2 wall
- **Files:** `models/step/parts/TR-313.step`, `models/stl/TR-313.stl`, `drawings/parts/TR-313.svg`
  1. Saw SHS 25x25x2 (S235JR) to 400 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TR-321 - Guard panel, top

- **Quantity in plant:** 1 - **Made in-house** - Cut to size (saw/router)
- **Material / stock:** Polycarbonate - Polycarbonate sheet 4 mm
- **Envelope:** 600 x 450 x 4 mm - **mass** 1.30 kg
- **Key dimensions:** Length: 600; Width: 450; Thickness: 4
- **Files:** `models/step/parts/TR-321.step`, `models/stl/TR-321.stl`, `drawings/parts/TR-321.svg`, `models/dxf/TR-321.dxf`
  1. Cut from Polycarbonate sheet 4 mm with a fine-tooth circular saw or router to the sizes given.
  2. Drill fixing holes on assembly (match-drill from the frame).
  3. Round or flame-polish the exposed edges.

#### TR-322 - Guard panel, back

- **Quantity in plant:** 1 - **Made in-house** - Cut to size (saw/router)
- **Material / stock:** Polycarbonate - Polycarbonate sheet 4 mm
- **Envelope:** 600 x 380 x 4 mm - **mass** 1.09 kg
- **Key dimensions:** Length: 600; Width: 380; Thickness: 4
- **Files:** `models/step/parts/TR-322.step`, `models/stl/TR-322.stl`, `drawings/parts/TR-322.svg`, `models/dxf/TR-322.dxf`
  1. Cut from Polycarbonate sheet 4 mm with a fine-tooth circular saw or router to the sizes given.
  2. Drill fixing holes on assembly (match-drill from the frame).
  3. Round or flame-polish the exposed edges.

#### TR-323 - Guard panel, side

- **Quantity in plant:** 2 - **Made in-house** - Cut to size (saw/router)
- **Material / stock:** Polycarbonate - Polycarbonate sheet 4 mm
- **Envelope:** 450 x 380 x 4 mm - **mass** 0.82 kg
- **Key dimensions:** Length: 450; Width: 380; Thickness: 4
- **Files:** `models/step/parts/TR-323.step`, `models/stl/TR-323.stl`, `drawings/parts/TR-323.svg`, `models/dxf/TR-323.dxf`
  1. Cut from Polycarbonate sheet 4 mm with a fine-tooth circular saw or router to the sizes given.
  2. Drill fixing holes on assembly (match-drill from the frame).
  3. Round or flame-polish the exposed edges.

#### TR-324 - Guard panel, front upper

- **Quantity in plant:** 1 - **Made in-house** - Cut to size (saw/router)
- **Material / stock:** Polycarbonate - Polycarbonate sheet 4 mm
- **Envelope:** 600 x 200 x 4 mm - **mass** 0.58 kg
- **Key dimensions:** Length: 600; Width: 200; Thickness: 4
- **Files:** `models/step/parts/TR-324.step`, `models/stl/TR-324.stl`, `drawings/parts/TR-324.svg`, `models/dxf/TR-324.dxf`
  1. Cut from Polycarbonate sheet 4 mm with a fine-tooth circular saw or router to the sizes given.
  2. Drill fixing holes on assembly (match-drill from the frame).
  3. Round or flame-polish the exposed edges.

#### TR-401 - Trim fence

- **Quantity in plant:** 1 - **Made in-house** - Cut to size (saw/router)
- **Material / stock:** HDPE - HDPE board 20 mm
- **Envelope:** 300 x 40 x 20 mm - **mass** 0.23 kg
- **Key dimensions:** Size: 300 x 40 x 20
- **Files:** `models/step/parts/TR-401.step`, `models/stl/TR-401.stl`, `drawings/parts/TR-401.svg`, `models/dxf/TR-401.dxf`
- **Notes:** Screwed to the table 6 mm behind the burr; the tile edge slides along it.
  1. Cut from HDPE board 20 mm with a fine-tooth circular saw or router to the sizes given.
  2. Drill fixing holes on assembly (match-drill from the frame).
  3. Round or flame-polish the exposed edges.

#### TR-901 - Control post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2
- **Envelope:** 300 x 30 x 30 mm - **mass** 0.53 kg
- **Key dimensions:** Cut length: 300; Section: 30 x 30 x 2 wall
- **Files:** `models/step/parts/TR-901.step`, `models/stl/TR-901.stl`, `drawings/parts/TR-901.svg`
  1. Saw SHS 30x30x2 (S235JR) to 300 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TT-101 - Base runner

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - RHS 100x50x4
- **Envelope:** 800 x 50 x 100 mm - **mass** 7.13 kg
- **Key dimensions:** Cut length: 800; Section: 100 x 50 x 4 (upright)
- **Files:** `models/step/parts/TT-101.step`, `models/stl/TT-101.stl`, `drawings/parts/TT-101.svg`
  1. Saw RHS 100x50x4 (S235JR) to 800 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TT-102 - Base plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 800 x 500 x 10 mm - **mass** 31.40 kg
- **Key dimensions:** Length: 800; Width: 500; Thickness: 10
- **Files:** `models/step/parts/TT-102.step`, `models/stl/TT-102.stl`, `drawings/parts/TT-102.svg`, `models/dxf/TT-102.dxf`
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### TT-103 - Upright

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 1250 x 80 x 80 mm - **mass** 11.93 kg
- **Key dimensions:** Cut length: 1250; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/TT-103.step`, `models/stl/TT-103.stl`, `drawings/parts/TT-103.svg`
  1. Saw SHS 80x80x4 (S235JR) to 1250 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TT-104 - Top beam

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 80x80x4
- **Envelope:** 680 x 80 x 80 mm - **mass** 6.47 kg
- **Key dimensions:** Cut length: 680; Section: 80 x 80 x 4 wall
- **Files:** `models/step/parts/TT-104.step`, `models/stl/TT-104.stl`, `drawings/parts/TT-104.svg`
  1. Saw SHS 80x80x4 (S235JR) to 680 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Mark out, centre-punch and drill the holes in the hole table (pilot dia 5 first, then to size); deburr both sides.
  4. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TT-105 - Support beam

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - RHS 150x100x5
- **Envelope:** 400 x 100 x 150 mm - **mass** 7.54 kg
- **Key dimensions:** Cut length: 400; Section: 150 x 100 x 5
- **Files:** `models/step/parts/TT-105.step`, `models/stl/TT-105.stl`, `drawings/parts/TT-105.svg`
  1. Saw RHS 150x100x5 (S235JR) to 400 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TT-106 - Support saddle

- **Quantity in plant:** 4 - **Made in-house** - Milled
- **Material / stock:** S235JR - Flat bar 40x20
- **Envelope:** 40 x 60 x 20 mm - **mass** 0.34 kg
- **Key dimensions:** Size: 40 x 60 x 20; Seat: R15.2 groove across the 40 mm width
- **Files:** `models/step/parts/TT-106.step`, `models/stl/TT-106.stl`, `drawings/parts/TT-106.svg`
  1. Saw Flat bar 40x20 (S235JR) to size + 2 mm.
  2. Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.
  3. Drill (and tap where noted) the holes in the hole table. Deburr.

#### TT-201 - Support / loading bar dia 30

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 360 x 30 x 30 mm - **mass** 2.00 kg
- **Key dimensions:** Cut length: 360; Diameter: 30
- **Files:** `models/step/parts/TT-201.step`, `models/stl/TT-201.stl`, `drawings/parts/TT-201.svg`
- **Notes:** Bright bar; 2 supports + 1 loading nose. Free to rotate in the saddles.
  1. Saw Round bar dia 30 (C45) to 360 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### TT-202 - Loading nose holder

- **Quantity in plant:** 1 - **Made in-house** - Milled
- **Material / stock:** S235JR - Flat bar 60x40
- **Envelope:** 60 x 60 x 40 mm - **mass** 0.96 kg
- **Key dimensions:** Size: 60 x 60 x 40; Seat: R15.2 groove; Top: M16 tapped for the ram rod
- **Files:** `models/step/parts/TT-202.step`, `models/stl/TT-202.stl`, `drawings/parts/TT-202.svg`
  1. Saw Flat bar 60x40 (S235JR) to size + 2 mm.
  2. Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.
  3. Drill (and tap where noted) the holes in the hole table. Deburr.

#### TT-301 - Hydraulic ram 5 t with hand pump and gauge

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Single-acting 5 t ram, stroke >= 100 mm, with hand pump, hose and calibrated gauge (or a 20 kN load cell + indicator for direct reading)
- **Envelope:** 70 x 70 x 960 mm - **mass** 9.00 kg
- **Files:** `models/step/parts/TT-301.step`, `models/stl/TT-301.stl`, `drawings/parts/TT-301.svg`
- **Purchase specification:** Single-acting 5 t ram, stroke >= 100 mm, with hand pump, hose and calibrated gauge (or a 20 kN load cell + indicator for direct reading)
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### VS-101 - Screen frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 692 x 50 x 50 mm - **mass** 3.06 kg
- **Key dimensions:** Cut length: 692; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/VS-101.step`, `models/stl/VS-101.stl`, `drawings/parts/VS-101.svg`
  1. Saw SHS 50x50x3 (S235JR) to 692 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-102 - Screen frame - long rail

- **Quantity in plant:** 3 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 500 x 50 x 50 mm - **mass** 2.21 kg
- **Key dimensions:** Cut length: 500; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/VS-102.step`, `models/stl/VS-102.stl`, `drawings/parts/VS-102.svg`
  1. Saw SHS 50x50x3 (S235JR) to 500 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-103 - Screen frame - cross rail

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 900 x 50 x 50 mm - **mass** 3.98 kg
- **Key dimensions:** Cut length: 900; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/VS-103.step`, `models/stl/VS-103.stl`, `drawings/parts/VS-103.svg`
  1. Saw SHS 50x50x3 (S235JR) to 900 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-104 - Screen frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 70 x 140 x 8 mm - **mass** 0.60 kg
- **Key dimensions:** Length: 70; Width: 140; Thickness: 8
- **Files:** `models/step/parts/VS-104.step`, `models/stl/VS-104.stl`, `drawings/parts/VS-104.svg`, `models/dxf/VS-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-201 - Spring seat

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 6 mm
- **Envelope:** 80 x 80 x 6 mm - **mass** 0.30 kg
- **Key dimensions:** Length: 80; Width: 80; Thickness: 6
- **Files:** `models/step/parts/VS-201.step`, `models/stl/VS-201.stl`, `drawings/parts/VS-201.svg`, `models/dxf/VS-201.dxf`
- **Notes:** Weld on the frame top rail; the M8 stud centres the spring.
  1. Profile-cut from Plate 6 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (6 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-202 - Compression spring dia 50 x 90

- **Quantity in plant:** 4 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Compression spring OD 50, wire 6, free length 90, rate approx. 15 N/mm, ground ends
- **Envelope:** 50 x 50 x 90 mm - **mass** 0.30 kg
- **Files:** `models/step/parts/VS-202.step`, `models/stl/VS-202.stl`, `drawings/parts/VS-202.svg`
- **Purchase specification:** Compression spring OD 50, wire 6, free length 90, rate approx. 15 N/mm, ground ends
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### VS-301 - Screen box side plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 4 mm
- **Envelope:** 840 x 150 x 4 mm - **mass** 3.96 kg
- **Key dimensions:** Length: 840; Width: 150; Thickness: 4
- **Files:** `models/step/parts/VS-301.step`, `models/stl/VS-301.stl`, `drawings/parts/VS-301.svg`, `models/dxf/VS-301.dxf`
  1. Profile-cut from Plate 4 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-302 - Screen box back plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 4 mm
- **Envelope:** 432 x 150 x 4 mm - **mass** 2.03 kg
- **Key dimensions:** Length: 432; Width: 150; Thickness: 4
- **Files:** `models/step/parts/VS-302.step`, `models/stl/VS-302.stl`, `drawings/parts/VS-302.svg`, `models/dxf/VS-302.dxf`
  1. Profile-cut from Plate 4 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-303 - Screen box cross tube

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD33.7 x 3
- **Envelope:** 432 x 34 x 34 mm - **mass** 0.98 kg
- **Key dimensions:** Cut length: 432; OD: 33.7; Wall: 3
- **Files:** `models/step/parts/VS-303.step`, `models/stl/VS-303.stl`, `drawings/parts/VS-303.svg`
  1. Saw Tube OD33.7 x 3 (S235JR) to 432 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-304 - Deck support flat

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 25x5
- **Envelope:** 836 x 25 x 5 mm - **mass** 0.82 kg
- **Key dimensions:** Cut length: 836; Section: 25 x 5
- **Files:** `models/step/parts/VS-304.step`, `models/stl/VS-304.stl`, `drawings/parts/VS-304.svg`
  1. Saw Flat bar 25x5 (S235JR) to 836 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-305 - Screen mesh panel 2 mm aperture

- **Quantity in plant:** 1 - **Made in-house** - Cut to size
- **Material / stock:** Woven wire 304 - Woven wire cloth, 2.0 mm aperture, 0.9 mm wire
- **Envelope:** 430 x 836 x 2 mm - **mass** 5.68 kg
- **Key dimensions:** Length: 836; Width: 430; Aperture: 2.0; Wire: 0.9
- **Files:** `models/step/parts/VS-305.step`, `models/stl/VS-305.stl`, `drawings/parts/VS-305.svg`, `models/dxf/VS-305.dxf`
- **Notes:** Cut with a 4 mm allowance, fold the long edges 10 mm over for clamping. Keep a spare; this is a wear part.
  1. Cut to size with a shear or 1 mm slitting disc, leaving the allowance noted.
  2. Dress cut wire ends; fold or frame the edges as noted.
  3. Fix with the clamp strips / stitch welds shown on the assembly sheet.

#### VS-306 - Mesh clamp strip

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Flat bar 25x4
- **Envelope:** 836 x 25 x 4 mm - **mass** 0.66 kg
- **Key dimensions:** Cut length: 836; Section: 25 x 4
- **Files:** `models/step/parts/VS-306.step`, `models/stl/VS-306.stl`, `drawings/parts/VS-306.svg`
- **Notes:** 6 x dia 7 holes at 150 pitch; M6 screws into the deck support flats.
  1. Saw Flat bar 25x4 (S235JR) to 836 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-307 - Vibrator bridge plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 440 x 200 x 8 mm - **mass** 5.50 kg
- **Key dimensions:** Length: 440; Width: 200; Thickness: 8
- **Files:** `models/step/parts/VS-307.step`, `models/stl/VS-307.stl`, `drawings/parts/VS-307.svg`, `models/dxf/VS-307.dxf`
- **Notes:** Welded across the top of the side plates at the discharge end; hole pattern to suit the vibrator feet (check the purchased unit).
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-308 - Vibrator motor 0.12 kW

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - External electric vibrator motor 0.12 kW, 2-pole (3000 rpm), centrifugal force adjustable to approx. 1.5 kN
- **Envelope:** 200 x 150 x 130 mm - **mass** 6.00 kg
- **Files:** `models/step/parts/VS-308.step`, `models/stl/VS-308.stl`, `drawings/parts/VS-308.svg`
- **Purchase specification:** External electric vibrator motor 0.12 kW, 2-pole (3000 rpm), centrifugal force adjustable to approx. 1.5 kN
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### VS-309 - Spring lug

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 60x60x6
- **Envelope:** 80 x 60 x 60 mm - **mass** 0.43 kg
- **Key dimensions:** Cut length: 80; Section: L 60 x 60 x 6
- **Files:** `models/step/parts/VS-309.step`, `models/stl/VS-309.stl`, `drawings/parts/VS-309.svg`
  1. Saw Angle 60x60x6 (S235JR) to 80 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-3101 - Undersize pan - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 430 x 378 x 2 mm - **mass** 1.72 kg
- **Key dimensions:** Bottom width: 150; Top width: 430; Slant height: 378.5; Thickness: 2; Wall angle to horizontal: 43.4 deg
- **Files:** `models/step/parts/VS-3101.step`, `models/stl/VS-3101.stl`, `drawings/parts/VS-3101.svg`, `models/dxf/VS-3101.dxf`
  1. Profile-cut from Sheet 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-3102 - Undersize pan - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 700 x 295 x 2 mm - **mass** 1.97 kg
- **Key dimensions:** Bottom width: 150; Top width: 700; Slant height: 295.3; Thickness: 2; Wall angle to horizontal: 61.7 deg
- **Files:** `models/step/parts/VS-3102.step`, `models/stl/VS-3102.stl`, `drawings/parts/VS-3102.svg`, `models/dxf/VS-3102.dxf`
  1. Profile-cut from Sheet 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-321 - Oversize chute

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 434 x 135 x 60 mm - **mass** 1.17 kg
- **Key dimensions:** Width: 434; Length: 135; Side height: 60
- **Files:** `models/step/parts/VS-321.step`, `models/stl/VS-321.stl`, `drawings/parts/VS-321.svg`, `models/dxf/VS-321.dxf`
  1. Cut the developed blank from Sheet 2 mm DC01 galv. (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### VS-401 - Screen dust hood - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 440 x 253 x 2 mm - **mass** 0.88 kg
- **Key dimensions:** Bottom width: 150; Top width: 440; Slant height: 253.0; Thickness: 1.5; Wall angle to horizontal: 60.4 deg
- **Files:** `models/step/parts/VS-401.step`, `models/stl/VS-401.stl`, `drawings/parts/VS-401.svg`, `models/dxf/VS-401.dxf`
  1. Profile-cut from Sheet 1.5 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-402 - Screen dust hood - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 1.5 mm
- **Envelope:** 400 x 263 x 2 mm - **mass** 0.85 kg
- **Key dimensions:** Bottom width: 150; Top width: 400; Slant height: 263.5; Thickness: 1.5; Wall angle to horizontal: 56.6 deg
- **Files:** `models/step/parts/VS-402.step`, `models/stl/VS-402.stl`, `drawings/parts/VS-402.svg`, `models/dxf/VS-402.dxf`
  1. Profile-cut from Sheet 1.5 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### VS-411 - Dust hood post

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2
- **Envelope:** 320 x 30 x 30 mm - **mass** 0.56 kg
- **Key dimensions:** Cut length: 320; Section: 30 x 30 x 2 wall
- **Files:** `models/step/parts/VS-411.step`, `models/stl/VS-411.stl`, `drawings/parts/VS-411.svg`
  1. Saw SHS 30x30x2 (S235JR) to 320 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-412 - Dust hood bearer

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Angle 30x30x3
- **Envelope:** 600 x 30 x 30 mm - **mass** 0.81 kg
- **Key dimensions:** Cut length: 600; Section: L 30 x 30 x 3
- **Files:** `models/step/parts/VS-412.step`, `models/stl/VS-412.stl`, `drawings/parts/VS-412.svg`
  1. Saw Angle 30x30x3 (S235JR) to 600 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### VS-501 - Stones bucket 20 L

- **Quantity in plant:** 1 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Steel bucket 20 L for stones and oversize
- **Envelope:** 300 x 300 x 300 mm - **mass** 1.50 kg
- **Files:** `models/step/parts/VS-501.step`, `models/stl/VS-501.stl`, `drawings/parts/VS-501.svg`
- **Purchase specification:** Steel bucket 20 L for stones and oversize
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### WB-101 - Weigh batcher frame - leg

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 1492 x 50 x 50 mm - **mass** 6.61 kg
- **Key dimensions:** Cut length: 1492; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/WB-101.step`, `models/stl/WB-101.stl`, `drawings/parts/WB-101.svg`
  1. Saw SHS 50x50x3 (S235JR) to 1492 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-102 - Weigh batcher frame - long rail

- **Quantity in plant:** 5 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 900 x 50 x 50 mm - **mass** 3.98 kg
- **Key dimensions:** Cut length: 900; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/WB-102.step`, `models/stl/WB-102.stl`, `drawings/parts/WB-102.svg`
  1. Saw SHS 50x50x3 (S235JR) to 900 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-103 - Weigh batcher frame - cross rail

- **Quantity in plant:** 5 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 500 x 50 x 50 mm - **mass** 2.21 kg
- **Key dimensions:** Cut length: 500; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/WB-103.step`, `models/stl/WB-103.stl`, `drawings/parts/WB-103.svg`
  1. Saw SHS 50x50x3 (S235JR) to 500 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-104 - Weigh batcher frame - foot plate

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 70 x 140 x 8 mm - **mass** 0.60 kg
- **Key dimensions:** Length: 70; Width: 140; Thickness: 8
- **Files:** `models/step/parts/WB-104.step`, `models/stl/WB-104.stl`, `drawings/parts/WB-104.svg`, `models/dxf/WB-104.dxf`
- **Notes:** Anchor to container floor with M12 coach bolts / through-bolts.
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-201 - Collecting hopper - front/back panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 900 x 403 x 2 mm - **mass** 3.32 kg
- **Key dimensions:** Bottom width: 150; Top width: 900; Slant height: 403.1; Thickness: 2; Wall angle to horizontal: 60.3 deg
- **Files:** `models/step/parts/WB-201.step`, `models/stl/WB-201.stl`, `drawings/parts/WB-201.svg`, `models/dxf/WB-201.dxf`
  1. Profile-cut from Sheet 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-202 - Collecting hopper - side panel

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** DC01 galv. - Sheet 2 mm
- **Envelope:** 500 x 513 x 2 mm - **mass** 2.42 kg
- **Key dimensions:** Bottom width: 100; Top width: 500; Slant height: 513.0; Thickness: 2; Wall angle to horizontal: 43.0 deg
- **Files:** `models/step/parts/WB-202.step`, `models/stl/WB-202.stl`, `drawings/parts/WB-202.svg`, `models/dxf/WB-202.dxf`
  1. Profile-cut from Sheet 2 mm DC01 galv. using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-251 - Screw inlet chute

- **Quantity in plant:** 1 - **Made in-house** - Plate fabrication
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 156 x 106 x 210 mm - **mass** 1.90 kg
- **Key dimensions:** Inside: 150 x 100; Height: 210 max, scribed to the 45 deg tube
- **Files:** `models/step/parts/WB-251.step`, `models/stl/WB-251.stl`, `drawings/parts/WB-251.svg`
- **Notes:** Make as a 4-sided sleeve 210 high, offer up to the casing tube at 45 deg, scribe, cut and seal-weld to the tube round the inlet window.
  1. Cut the individual flat plates to the sizes under Key dimensions (plasma or shear).
  2. Tack together square on a flat table; offer up to the mating part and scribe any penetrations before cutting them.
  3. Weld all seams continuously (they must be dust- and sand-tight); grind inside seams smooth so material cannot hang up.

#### WB-301 - Weigh hopper - front/back panel

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Sheet 2 mm
- **Envelope:** 380 x 313 x 2 mm - **mass** 1.19 kg
- **Key dimensions:** Bottom width: 100; Top width: 380; Slant height: 313.0; Thickness: 2; Wall angle to horizontal: 63.4 deg
- **Files:** `models/step/parts/WB-301.step`, `models/stl/WB-301.stl`, `drawings/parts/WB-301.svg`, `models/dxf/WB-301.dxf`
  1. Profile-cut from Sheet 2 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-302 - Weigh hopper - side panel

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Sheet 2 mm
- **Envelope:** 380 x 313 x 2 mm - **mass** 1.19 kg
- **Key dimensions:** Bottom width: 100; Top width: 380; Slant height: 313.0; Thickness: 2; Wall angle to horizontal: 63.4 deg
- **Files:** `models/step/parts/WB-302.step`, `models/stl/WB-302.stl`, `drawings/parts/WB-302.svg`, `models/dxf/WB-302.dxf`
  1. Profile-cut from Sheet 2 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-303 - Weigh hopper band

- **Quantity in plant:** 8 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Plate 2 mm
- **Envelope:** 382 x 120 x 2 mm - **mass** 0.72 kg
- **Key dimensions:** Length: 382; Width: 120; Thickness: 2
- **Files:** `models/step/parts/WB-303.step`, `models/stl/WB-303.stl`, `drawings/parts/WB-303.svg`, `models/dxf/WB-303.dxf`
  1. Profile-cut from Plate 2 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-304 - Weigh hopper support plate

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 6 mm
- **Envelope:** 430 x 494 x 6 mm - **mass** 2.91 kg
- **Key dimensions:** Length: 430; Width: 494; Thickness: 6
- **Files:** `models/step/parts/WB-304.step`, `models/stl/WB-304.stl`, `drawings/parts/WB-304.svg`, `models/dxf/WB-304.dxf`
- **Notes:** Welded round the hopper at the band joint. The rear tongue bolts to the free end of the load cell; nothing else may touch the hopper.
  1. Profile-cut from Plate 6 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (6 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-321 - Slide gate body

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Plate 8 mm
- **Envelope:** 160 x 160 x 8 mm - **mass** 0.99 kg
- **Key dimensions:** Length: 160; Width: 160; Thickness: 8
- **Files:** `models/step/parts/WB-321.step`, `models/stl/WB-321.stl`, `drawings/parts/WB-321.svg`, `models/dxf/WB-321.dxf`
  1. Profile-cut from Plate 8 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Compensate the kerf on the waste side.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-322 - Slide gate guide

- **Quantity in plant:** 4 - **Made in-house** - Saw to length
- **Material / stock:** AISI 304 - Angle 20x20x3
- **Envelope:** 200 x 20 x 20 mm - **mass** 0.18 kg
- **Key dimensions:** Cut length: 200; Section: L 20 x 20 x 3
- **Files:** `models/step/parts/WB-322.step`, `models/stl/WB-322.stl`, `drawings/parts/WB-322.svg`
  1. Saw Angle 20x20x3 (AISI 304) to 200 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-323 - Slide gate blade

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** AISI 304 - Plate 3 mm
- **Envelope:** 104 x 250 x 3 mm - **mass** 0.60 kg
- **Key dimensions:** Length: 104; Width: 250; Thickness: 3
- **Files:** `models/step/parts/WB-323.step`, `models/stl/WB-323.stl`, `drawings/parts/WB-323.svg`, `models/dxf/WB-323.dxf`
- **Notes:** Slides in the two guide angles. Pull toward the operator to open; the dia 28 hole is the finger grip.
  1. Profile-cut from Plate 3 mm AISI 304 using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (3 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-401 - Single-point load cell 100 kg

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Aluminium single-point (platform) load cell, 100 kg, C3, rated for platforms up to 600 x 600 mm, IP65, with 3 m cable
- **Envelope:** 40 x 150 x 40 mm - **mass** 0.90 kg
- **Files:** `models/step/parts/WB-401.step`, `models/stl/WB-401.stl`, `drawings/parts/WB-401.svg`
- **Purchase specification:** Aluminium single-point (platform) load cell, 100 kg, C3, rated for platforms up to 600 x 600 mm, IP65, with 3 m cable
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### WB-402 - Load cell spacer

- **Quantity in plant:** 4 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 10 mm
- **Envelope:** 40 x 50 x 10 mm - **mass** 0.15 kg
- **Key dimensions:** Length: 40; Width: 50; Thickness: 10
- **Files:** `models/step/parts/WB-402.step`, `models/stl/WB-402.stl`, `drawings/parts/WB-402.svg`, `models/dxf/WB-402.dxf`
  1. Profile-cut from Plate 10 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (10 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-501 - Weighing indicator

- **Quantity in plant:** 2 - **Purchased** - Purchased item
- **Material / stock:** Purchased - Weighing indicator with large LED display, set-point output (2 relays), 230 V; 1 per hopper. Display in kg and % of batch target
- **Envelope:** 200 x 80 x 130 mm - **mass** 1.20 kg
- **Files:** `models/step/parts/WB-501.step`, `models/stl/WB-501.stl`, `drawings/parts/WB-501.svg`
- **Purchase specification:** Weighing indicator with large LED display, set-point output (2 relays), 230 V; 1 per hopper. Display in kg and % of batch target
  1. Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).
  2. On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.
  3. Fit as shown on the assembly sheet.

#### WB-502 - Display post

- **Quantity in plant:** 2 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2
- **Envelope:** 320 x 30 x 30 mm - **mass** 0.56 kg
- **Key dimensions:** Cut length: 320; Section: 30 x 30 x 2 wall
- **Files:** `models/step/parts/WB-502.step`, `models/stl/WB-502.stl`, `drawings/parts/WB-502.svg`
  1. Saw SHS 30x30x2 (S235JR) to 320 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-503 - Display cross bar

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 30x30x2
- **Envelope:** 790 x 30 x 30 mm - **mass** 1.39 kg
- **Key dimensions:** Cut length: 790; Section: 30 x 30 x 2 wall
- **Files:** `models/step/parts/WB-503.step`, `models/stl/WB-503.stl`, `drawings/parts/WB-503.svg`
  1. Saw SHS 30x30x2 (S235JR) to 790 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-601 - Batch incline screw (45 deg) - casing tube

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD114.3 x 3.6
- **Envelope:** 2023 x 114 x 114 mm - **mass** 19.21 kg
- **Key dimensions:** Cut length: 2023; OD: 114.3; Wall: 3.6; Inlet cut-out (top): 140 x 90 at x=150; Outlet cut-out (bottom): 100 x 80 at x=1913
- **Files:** `models/step/parts/WB-601.step`, `models/stl/WB-601.stl`, `drawings/parts/WB-601.svg`
- **Notes:** Saw to length, mark and plasma/grinder-cut the inlet (top) and outlet (bottom) windows. Deburr inside.
  1. Saw Tube OD114.3 x 3.6 (S235JR) to 2023 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-602 - Batch incline screw (45 deg) - end flange

- **Quantity in plant:** 2 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 170 x 170 x 8 mm - **mass** 1.30 kg
- **Key dimensions:** OD: 170; Thickness: 8; Bore: 45
- **Files:** `models/step/parts/WB-602.step`, `models/stl/WB-602.stl`, `drawings/parts/WB-602.svg`, `models/dxf/WB-602.dxf`
- **Notes:** Bolt pattern 70 x 70 suits UCF205. Weld square to the tube end (fillet a3 all round).
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-603 - Batch incline screw (45 deg) - screw centre pipe

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - Tube OD33.7 x 4
- **Envelope:** 2003 x 34 x 34 mm - **mass** 5.87 kg
- **Key dimensions:** Cut length: 2003; OD: 33.7; Wall: 4.0
- **Files:** `models/step/parts/WB-603.step`, `models/stl/WB-603.stl`, `drawings/parts/WB-603.svg`
- **Notes:** Drill 2 x dia 8 cross holes 25 mm from each end (at 90 deg to each other) for the stub-shaft pins after fitting the stubs.
  1. Saw Tube OD33.7 x 4 (S235JR) to 2003 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-604 - Batch incline screw (45 deg) - tail stub shaft

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 135 x 26 x 26 mm - **mass** 0.53 kg
- **Key dimensions:** Plug dia (into pipe): 25.7 h9 x 60; Journal dia: 25 h7 x 75; Overall: 135
- **Files:** `models/step/parts/WB-604.step`, `models/stl/WB-604.stl`, `drawings/parts/WB-604.svg`
  1. Saw Round bar dia 30 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### WB-605 - Batch incline screw (45 deg) - drive stub shaft

- **Quantity in plant:** 1 - **Made in-house** - Lathe turned
- **Material / stock:** C45 - Round bar dia 30
- **Envelope:** 250 x 26 x 26 mm - **mass** 0.95 kg
- **Key dimensions:** Plug dia (into pipe): 25.7 h9 x 60; Journal dia: 25 h7 x 190; Keyway: 8 x 4 deep x 100 long; Overall: 250
- **Files:** `models/step/parts/WB-605.step`, `models/stl/WB-605.stl`, `drawings/parts/WB-605.svg`
  1. Saw Round bar dia 30 (C45) to the finished length + 4 mm.
  2. Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.
  3. Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.
  4. Inspect; oil and wrap bearing seats and bores for storage.

#### WB-607 - Batch incline screw (45 deg) - outlet spout

- **Quantity in plant:** 1 - **Made in-house** - Cut blank, fold
- **Material / stock:** S235JR - Sheet 3 mm
- **Envelope:** 110 x 90 x 120 mm - **mass** 1.10 kg
- **Key dimensions:** Inside: 104 x 84; Height: 120; Sheet: 3
- **Files:** `models/step/parts/WB-607.step`, `models/stl/WB-607.stl`, `drawings/parts/WB-607.svg`, `models/dxf/WB-607.dxf`
- **Notes:** Fold from one strip (developed length 388) and seam-weld; scribe to the tube and weld all round.
  1. Cut the developed blank from Sheet 3 mm S235JR (DXF supplied).
  2. Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.
  3. Tack and weld the seam / corners, dress the welds, break sharp edges.

#### WB-701 - Incline screw support post

- **Quantity in plant:** 1 - **Made in-house** - Saw to length
- **Material / stock:** S235JR - SHS 50x50x3
- **Envelope:** 879 x 50 x 50 mm - **mass** 3.89 kg
- **Key dimensions:** Cut length: 879; Section: 50 x 50 x 3 wall
- **Files:** `models/step/parts/WB-701.step`, `models/stl/WB-701.stl`, `drawings/parts/WB-701.svg`
  1. Saw SHS 50x50x3 (S235JR) to 879 mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.
  2. Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.
  3. Write the part number on the part with a paint marker and put it with its weldment kit.

#### WB-702 - Support post base plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 160 x 160 x 8 mm - **mass** 1.57 kg
- **Key dimensions:** Length: 160; Width: 160; Thickness: 8
- **Files:** `models/step/parts/WB-702.step`, `models/stl/WB-702.stl`, `drawings/parts/WB-702.svg`, `models/dxf/WB-702.dxf`
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).

#### WB-703 - Support post saddle plate

- **Quantity in plant:** 1 - **Made in-house** - Laser / plasma profile cut
- **Material / stock:** S235JR - Plate 8 mm
- **Envelope:** 140 x 140 x 8 mm - **mass** 1.22 kg
- **Key dimensions:** Length: 140; Width: 140; Thickness: 8
- **Files:** `models/step/parts/WB-703.step`, `models/stl/WB-703.stl`, `drawings/parts/WB-703.svg`, `models/dxf/WB-703.dxf`
  1. Profile-cut from Plate 8 mm S235JR using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.
  2. Holes smaller than the plate thickness (8 mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.
  3. Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.
  4. Check the overall size and hole positions against the drawing (+/-0.5 mm general).
