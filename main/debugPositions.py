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

startCom()
robot.setMotorsTorque(1)
#robot.moveRobotByQVals(offsets)
while True:
    opt = input("u -> up, e -> exit, t -> torque, g -> get, a -> algorithm, o -> offsets ").lower().strip()
    if opt == "o":
        robot.moveRobotByQVals(offsets)
    if opt == "u":
        robot.standFormSitting()
        #robot.standFormSitting()
    if opt == "e":
        robot.moveRobotByQVals(sitPos_QVals)
        break
    if opt == "t":
        id = int(input("ID: ").strip()) -1
        torque = int(input("Torque valor: ").strip())
        robot.motors[id].setTorque(torque)
    if opt == "g":
        robot.getMotorsPosition()
        print(robot.q0)
    
    if opt == "w":
        robot.moveWith_cmd_vel(0,0.5,0)

    if opt == "a":
        for i in range(0,1):
            #robot.mo(portero1_QVals)
            robot.moveRobotByQVals(porteroBien_QVals)
            #robot.moveRobotByQVals(portero3_QVals)
        """ 
        robot.moveRobotByQVals(portero1_QVals)
        robot.moveRobotByQVals(porteroTapa1_QVals)
        #robot.moveRobotByQVals(porteroTapa2_QVals)
        robot.moveRobotByQVals(porteroTapa3_QVals)
        for i in range(0,5):
            robot.moveRobotByQVals(porteroTapa4_QVals)
            robot.moveRobotByQVals(porteroTapa5_QVals) """

robot.setMotorsTorque(0)
stopCom()