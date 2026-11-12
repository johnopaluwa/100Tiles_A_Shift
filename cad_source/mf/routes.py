"""Manufacturing routes: a step list for every part, from process templates plus part-specific overrides."""
from .core import PARTS
from .drawing import find_holes

CUSTOM = {
    'TL-001': [
        'Charge: weigh 2.25 kg of hot mix (190-200 C) per cavity on the dough scale; shape it roughly into a 350 x 250 slab with the steel paddle. Work fast - the mix skins over in under a minute.',
        'Place one charge in the middle of each cavity insert on the charge table. Brush insert and punch thinly with mould release every 5-10 cycles.',
        'Roll the carrier into the press against the end stop. Two-hand start: fast approach, then press at 180-210 bar (about 3.5 MPa on the tile) until the punch lands close on the insert.',
        'Hold under pressure for 60-90 s (to be validated) so the skin freezes, then open the press.',
        'Roll the carrier out and lift each insert with its tile to the cooling rack. Air-cool about 20 min until the tile is below 60 C and has shrunk free of the cavity.',
        'Tip the tile out, trim the flash at the trim station, check for cracks, voids and short shots, weigh (2.1-2.3 kg). Rejects and flash go to the regrind tote.',
        'Stack flat on the pallet, at most 10 high per stack, and leave 24 h before loading or testing.'],
    'TL-101': [
        'Pattern: CNC-rout or 3D-print the insert shape from the STL (models/stl/TL-101.stl) scaled 1.013 for aluminium shrinkage, with 3 mm machining allowance on the cavity, top and bottom faces and 2 deg draft on the outside walls.',
        'Sand-cast in A356 (AlSi7Mg0.3), degassed and grain-refined; heat treat to T6. Reject castings with visible porosity in the cavity. '
        'Alternative without a foundry: machine from 80 mm 5083 or MIC-6 tooling plate - same CNC program, no heat treatment.',
        'Mill the underside flat, then flip onto that face and mill the block to 470 x 380 x 75. Machine the two underside lightening pockets and the two finger grooves.',
        '3-axis CNC the cavity from the STEP model: rough with a dia 16 end mill leaving 0.5 mm, finish the profiled floor with a dia 12 ball-nose at 0.3 mm step-over along the tile length. The pocket walls are vertical: finish with a dia 10 end mill, corner radius 5.',
        'Polish the cavity floor along the tile length to Ra 0.8 or better (wet paper 240-600) - the floor is the weather face of the tile.',
        'Hard-anodise 50 micron (or electroless nickel 25 micron). Stamp the insert number 1-10 on the front edge so defects can be traced to a cavity.',
        'Inspect: pocket 421 x 331 +0.2/0, depth to the pan area 28.0 +/-0.1, underside flat within 0.1 mm.'],
    'TL-102': [
        'Saw a 480 x 390 blank from 100 mm S355J2 plate (or P20 if the budget allows). Mill both faces parallel to 98 mm, square the edges to 470 x 380.',
        'Back face: drill and tap 6 x M12 x 25 deep (400 x 150 pattern) for the bolster screws; these also hold the block for the next operations.',
        'Bolt to a fixture plate, back face down. Rough-mill around the boss to leave the 35 mm base and the two 3 mm kiss-off lands (470 x 20) along the long edges.',
        '3-axis CNC the boss from the STEP model: rough with dia 16, finish the profiled face with a dia 12 ball-nose at 0.3 mm step-over along the tile length. Finish the vertical boss walls to 420.2 x 330.2 (-0.1/0) with 0.5 mm edge break.',
        'Machine the two nib pockets 30.6 x 20.6 x 12.5 deep with 5 deg draft on all four walls and R2 corners; polish them - nibs that stick will tear off.',
        'Polish the moulding face to Ra 1.6. Optional: gas-nitride for wear resistance.',
        'Trial-fit in an insert with 0.4 mm feeler gauges all round; the two lands must touch the insert top face together (blue check).'],
    'CM-F98-80': [
        'Laser-cut the annular blank from 4 mm S355 using the DXF. One blank = one pitch (80 mm) of right-hand flight. Cut one extra per screw as a spare.',
        'Clamp one cut end of the blank in the vice or tack it to the bench. Grip the other end with a lever or chain block and pull the ring axially until the ends are 80 mm apart; '
        'dress out kinks over a dia 34 bar. A pair of 80 mm pitch forming dies in a 20 t press gives a better result if many are needed.',
        'Slide the flight onto the centre pipe, butt it to the previous segment, check the 98 mm OD in the casing tube itself, tack at four points on the inner edge.',
        'When all segments are on: weld the butt joints between segments (grind flush) and stitch-weld the inner edge to the pipe 25 mm every 75 mm, both sides alternately to keep the pipe straight.',
        'Straighten the finished screw between centres to within 1.5 mm TIR; it must turn freely in the casing with about 4.5 mm radial clearance.'],
}
KNIFE = ['Laser or waterjet cut from 10 mm Hardox 450 using the DXF (never plasma - the heat-affected edge loses hardness).',
         'Deburr. Check the hex bore with the 36 A/F shaft bar: sliding fit, no more than 0.3 mm play.',
         'Stack all 15 knives and 15 spacers on the shaft and measure the stack: 300.0 +/-0.3 mm. Surface-grind individual knives if needed.',
         'Grind a 5 deg clearance behind each of the three hook tips with a flap disc; keep the tips cool (dip in water) so they stay hard.',
         'Assembly order along the shaft: A, B, C, A, B, C ... so the teeth form a helix and only one or two teeth cut at a time.']
for _k in ('SH-231', 'SH-232', 'SH-233'):
    CUSTOM[_k] = KNIFE


def template(p, has_holes):
    d = p.dims
    L = d.get('Cut length')
    hole = 'Mark out, centre-punch and drill the holes in the hole table (pilot dia 5 first, then to size); deburr both sides.'
    if p.proc == 'SAW':
        s = [f'Saw {p.stock} ({p.mat}) to {L:g} mm (+/-1 mm), ends square within 1 mm. Use a band saw or cold saw, not an abrasive disc, for hollow sections.',
             'Deburr inside and outside. For welded members, grind mill scale and any galvanising off 25 mm back from the joints.']
        if has_holes:
            s.append(hole)
        s.append('Write the part number on the part with a paint marker and put it with its weldment kit.')
        return s
    if p.proc == 'LASER':
        t = d.get('Thickness', '')
        return [f'Profile-cut from {p.stock} {p.mat} using the DXF file (1:1, millimetres). Laser or waterjet preferred; plasma is acceptable on mild steel if the holes are drilled afterwards.',
                (f'Holes smaller than the plate thickness ({t} mm) cannot be cut cleanly: let the cutter centre-mark them, then drill.' if has_holes
                 else 'Compensate the kerf on the waste side.'),
                'Remove dross, break all edges 0.5 mm, press flat if bowed more than 1 mm in 500 mm.',
                'Check the overall size and hole positions against the drawing (+/-0.5 mm general).']
    if p.proc == 'ROLL':
        return [f'Cut the flat blank ({d.get("Developed blank", d.get("Flat blank", "see DXF"))} mm) from {p.stock} {p.mat}; DXF supplied.',
                'Pre-bend the first and last 50 mm in a press brake (or over a former) so the seam closes round instead of flat.',
                'Roll on a three-roll bender to the stated diameter; check with a plywood or sheet template.',
                'Tack the seam every 100 mm, check roundness (max 2 mm out), weld the seam with full penetration and grind it flush inside.',
                'Pass through the rolls once more to correct weld distortion.']
    if p.proc == 'BEND':
        return [f'Cut the developed blank from {p.stock} {p.mat} (DXF supplied).',
                'Scribe the bend lines. Fold on a press brake or box-and-pan folder; inside bend radius about one sheet thickness.',
                'Tack and weld the seam / corners, dress the welds, break sharp edges.']
    if p.proc == 'TURN':
        return [f'Saw {p.stock} ({p.mat}) to the finished length + 4 mm.',
                'Lathe: face and centre-drill both ends to length. Turn the diameters given under Key dimensions; take the toleranced seats (h7, k6, H7, H8) with a light finishing cut and measure with a micrometer.',
                'Mill keyways and drill cross holes as listed. Break all edges 0.5 x 45 deg.',
                'Inspect; oil and wrap bearing seats and bores for storage.']
    if p.proc == 'MILL':
        return [f'Saw {p.stock} ({p.mat}) to size + 2 mm.',
                'Mill square to the dimensions given; machine grooves, seats and slots as listed under Key dimensions.',
                'Drill (and tap where noted) the holes in the hole table. Deburr.']
    if p.proc == 'WELD':
        return ['Cut the individual flat plates to the sizes under Key dimensions (plasma or shear).',
                'Tack together square on a flat table; offer up to the mating part and scribe any penetrations before cutting them.',
                'Weld all seams continuously (they must be dust- and sand-tight); grind inside seams smooth so material cannot hang up.']
    if p.proc == 'MESH':
        return ['Cut to size with a shear or 1 mm slitting disc, leaving the allowance noted.', 'Dress cut wire ends; fold or frame the edges as noted.',
                'Fix with the clamp strips / stitch welds shown on the assembly sheet.']
    if p.proc == 'BOARD':
        return [f'Cut from {p.stock} with a fine-tooth circular saw or router to the sizes given.', 'Drill fixing holes on assembly (match-drill from the frame).',
                'Round or flame-polish the exposed edges.']
    if p.proc == 'BUY':
        return ['Buy to the purchase specification on this sheet (equivalent makes accepted - check the connecting dimensions against the model before ordering).',
                'On receipt: check the nameplate data, shaft / bore / flange sizes and that it turns freely or powers up.',
                'Fit as shown on the assembly sheet.']
    return ['See notes.']


def assign():
    for pn, p in PARTS.items():
        if p.route:
            p.route_final = p.route
        elif CUSTOM.get(pn):
            p.route_final = CUSTOM[pn]
        else:
            has = False
            if p.kind != 'buy' and p.proc in ('SAW', 'LASER'):
                try:
                    h = find_holes(p.shape())
                    has = any(not (p.proc == 'SAW' and ax == 'X') for (dia, ax) in h)
                except Exception:
                    has = False
            p.route_final = template(p, has)
