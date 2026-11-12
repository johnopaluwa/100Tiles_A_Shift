"""Plant layout constants. Plant origin = inside back-left floor corner of the container.
X along the container length (process direction), Y from the back wall toward the open front, Z up from the floor."""
import math
G = -170.0                 # ground level relative to container floor
CT_L, CT_W, CT_H = 12032.0, 2352.0, 2690.0     # container internal dimensions (40 ft high-cube)
S45 = math.sqrt(0.5)

ST = (500, 80)
SH = (1450, 80)
DR = (2300, 150)
DR_AXIS_Y = DR[1] + 350
DR_INLET_X = DR[0] + 170
VS = (3870, 180)
DC = (4500, 60)
MX = (6450, 80)
MX_C = (MX[0] + 450, MX[1] + 450)
MX_PORT = (MX_C[0] - 60, MX_C[1] - 140)          # charge port centre in the rear lid
MX_PORT_TOP = 1345.0                             # top of the charge collar
RCI = (7400, 150)
HP = (8250, 70)
HP_C = (HP[0] + 500, HP[1] + 580)
RCO = (9300, 150)
CR = (9900, 80)
TR = (10520, 80)
EL = (11400, 60)
TRANSFER_Z = 885.0          # top of rollers / lower bolster: mould carrier transfer height

# sand feed
SCREW2_Z = 2150.0
SCREW2_X = DR_INLET_X
HOPPER_CY = 3200.0
SPOUT = S45 * (57.15 + 120 - 12)               # offset of the 45 deg screw spout mouth from its axis point
