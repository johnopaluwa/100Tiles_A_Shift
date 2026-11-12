# Solar plastic-sand roof tile microfactory - engineering package

3D model, drawings and build instructions for the process shown in the concept video
`100Tiles_A_Shift.mp4`: waste HDPE + sand in, 100 roof tiles a shift out, from one 40 ft
container under a solar canopy.

**Start here: open `index.html`** (double-click). It contains the interactive 3D model,
a page per machine, a sheet per part with its drawing, files and how-to-make route, and
links to everything below.

> **Status: concept design.** The video itself ends with "a concept layout, not a finished
> machine drawing". The dimensions, forces, temperatures, structure and electrics in this
> package are first-pass engineering. Have them checked by qualified mechanical, structural
> and electrical engineers, and run the validation programme (recipe, temperatures, press
> force, cooling time, ventilation) before building or operating anything.

## What is in the package

| Folder / file | Contents |
|---|---|
| `index.html` | The hub: overview, 3D viewer, machines, all parts, how to build, file index |
| `models/step/assemblies/PLANT_complete.step` | Whole plant as one STEP assembly (FreeCAD, Fusion 360, SolidWorks, Onshape ...) |
| `models/step/assemblies/` | One STEP per machine and per weldment |
| `models/step/parts/` | One STEP solid per part number - master geometry for manufacture |
| `models/dxf/` | 1:1 flat profiles for laser / plasma / waterjet (plates, sheet, developed blanks) |
| `models/stl/` | Mesh per part |
| `models/glb/plant.glb` | Whole plant for Blender / 3D Viewer / web |
| `drawings/*_drawing_set.pdf` | A3 drawing set per machine: ballooned assembly + parts list, views, weldments, part sheets |
| `drawings/ALL_drawings.pdf` | Every sheet in one file |
| `drawings/PLANT_general_arrangement.pdf` | Plant layout sheets |
| `drawings/parts/*.svg` | Individual part and weldment sheets |
| `docs/Manufacturing_Guide.md` | Design basis, build sequence, every machine, every part with its route |
| `docs/BOM_all_parts.csv` | Bill of materials (opens in Excel) |
| `docs/Cut_list_sections.csv` | Saw cut list grouped by stock section |
| `docs/BOM_hardware.csv` | Fasteners and consumables |
| `images/` | Rendered views |
| `cad_source/` | Parametric Python + CadQuery source that generates all of the above |

## Machines

| Code | Machine |
|---|---|
| CT | Container shell conversion (40 ft high-cube) |
| ST | Station 1a - sorting table |
| SH | Station 1b - low-speed shredder, 4 kW |
| SF | Station 2a - sand receiving hopper and two feed screws |
| DR | Station 2b - rotary sand dryer, 4.5 kW |
| VS | Station 2c - vibrating screen |
| DC | Station 2d - dust collector |
| WB | Station 3 - weigh batcher with incline screw |
| MX | Station 4 - heated batch mixer, 8 kW |
| RC | Roller tables, return line, dough scale |
| HP | Station 5 - two-cavity hydraulic press, 1000 kN |
| TL | Mould tooling and the tile itself |
| CR | Station 6 - cooling rack |
| TR | Station 7 - guarded trim, check and stack station |
| FG | Finished goods pallet |
| EL | Inverter, battery, distribution, generator |
| SC | Solar canopy, 36 x 550 W |
| TT | Tile test rig |

Part numbers start with the machine code (`HP-401` = press column). `CM-...` parts are common
bought-out items used on several machines (bearings, gearmotors, screw flights, rollers).

## Conventions

- All dimensions in millimetres.
- Plant origin = inside back-left floor corner of the container; X along the line, Y toward
  the open front, Z up. Machine datums are on the plant general arrangement sheets.
- Purchased items are modelled as simple envelopes with a purchase specification. Check the real
  unit's connecting dimensions before drilling mating parts.

## Rebuilding after a change

```
pip install cadquery matplotlib pillow trimesh numpy
python cad_source/build.py            # everything (about 25 minutes)
python cad_source/build.py parts asm  # only the model files
python cad_source/build.py draw HP    # only the drawings of one machine
```

Layout positions are in `cad_source/mf/layout.py`; each machine is a function in
`m_prep.py`, `m_mix.py`, `m_press.py` or `m_site.py`.
