ROBOT_NAME = "BOGOBOT 4"

if ROBOT_NAME == "BOGOBOT 3.1":
    from BOGO_3_1.BOGO_3_1_positions import *

if ROBOT_NAME == "BOGOBOT 3.2":
    from BOGO_3_2.BOGO_3_2_positions import *

if ROBOT_NAME == "BOGOBOT 4":
    from BOGO_4.BOGO_4_positions import *

from Humanoid_Robot import *

#dxl11 = DXL_P2(11)
#dxl13 = DXL_P2(13)
robot = HUMANOID_ROBOT(ROBOT_NAME)

Wz = 0.0 # angular.z
Vx = 1.0 # linear.x
Vy = 0.0 # linear.y

startCom()
robot.setMotorsTorque(1)
robot.moveRobotByQVals(sitPos_QVals)
robot.standFormSitting()
robot.moveRobotByQVals(sitPos_QVals)

#robot.getMotorsPosition()
#print(robot.q0)

#robot.moveRobotByQVals(standPos_QVals)
#robot.oneTimeAlgorithm(poses_pararse_boca_abajo)
#robot.standFormSitting()
#robot.moveWith_cmd_vel(Wz, Vx, Vy)
#robot.stopRobot()
time.sleep(5)
robot.setMotorsTorque(0)
time.sleep(1)
stopCom()

#robot.motors[1].setTorque(1)
# robot.motors[0].setTorque(1)
# robot.motors[1].setTorque(1)
# robot.motors[0].setTorque(0)
#robot.motors[1].setTorque(0)
