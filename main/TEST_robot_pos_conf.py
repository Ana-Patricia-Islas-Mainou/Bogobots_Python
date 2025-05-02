# BOGOBOT 3.2 CONFIGURE PAGE

from DXL_PROTOCOL2.DXL_Protocol2_Functions import *

# MOTOR DECLARATION
DXL1 = DXL_P2(1)
DXL11 = DXL_P2(11)
DXL13 = DXL_P2(13)
# SPECS
#motorConfig = [DXL1, DXL11, DXL13]
motorConfig = [DXL1]
numberOfMotors = len(motorConfig)

offsets = [2048,2048,2048, 10, 20]
