from HUMANOID.Humanoid_Walking_Algorithms import *

class HUMANOID_ROBOT(HUMANOID_WALKING_AlGORIRTHMS):
    def __init__(self, ROBOT_NAME):
        if ROBOT_NAME == "BOGOBOT 3.1":
            from BOGO_3_1.BOGO_3_1_positions import standPos_Pose, standPos_QVals, sitPos_QVals

        if ROBOT_NAME == "BOGOBOT 3.2":
            from BOGO_3_2.BOGO_3_2_positions import offsets, standPos_Pose, standPos_QVals, sitPos_QVals
        super().__init__(ROBOT_NAME)

        self.offsets = offsets
        self.standPos_Pose = standPos_Pose
        self.standPos_QVals = standPos_QVals
        self.sitPos_QVals = sitPos_QVals
            
    def standFormSitting(self):
        self.setMotorsTorque(1)
        self.moveLegsByPose(self.standPos_Pose, self.standPos_QVals)

    def stopRobot(self):
        #self.moveRobotByQVals(self.sitPos_QVals) # revisar pose
        self.setMotorsTorque(0)

    def configPose(self):
        self.setMotorsTorque(1)
        self.moveRobotByQVals(self.offsets)

    def oneTimeAlgorithm(self, algorithm):
        self.setMotorsTorque(1)
        nSteps = len(algorithm)
        for step in range(0,nSteps):
            self.moveRobotByQVals(algorithm[step])
        self.moveLegsByPose(self.standPos_Pose, self.standPos_QVals)

    def moveWith_cmd_vel(self, Wz, Vx, Vy):
        tf = 0.4
        radio = 3.5

        x_zmp = min(8.5,max(Vx*tf*100,-8.5)); # Mover la cadera hacia adelante
        y_zmp = 8.8; #8.8; # Máximo 10.2 # Mover la cadera hacia los lados
        giro = min(pi/18,max(pi/18,Wz*tf*100)); # Si se pisa ponerle pi/18

        step = [1,2,2,3]  
        s = 4

        # apagar torca de los hombros
        self.motors[0].setTorque(0) # ID 1
        self.motors[1].setTorque(0) # ID 2
        self.motors[2].setTorque(0) # ID 3
        self.motors[3].setTorque(0) # ID 4

        self.walk_cartModel_IK(x_zmp, y_zmp, radio, giro, tf, step, s, self.standPos_QVals)

