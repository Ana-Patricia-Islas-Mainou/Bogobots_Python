from DXL_PROTOCOL2.DXL_Protocol2_Robot import *
from HUMANOID.Humanoid_Kinematics import *

class HUMANOID_MOVEMENT(ROBOT_P2):

    def __init__(self, ROBOT_NAME):
        super().__init__(ROBOT_NAME)

    def moveRobotByPose(self,pts): # no esta terminado REVISAR IK BRAZOS
        qIK = IK_robot (pts,1,1) # new desiered position
        qf = self.qValsToBits(qIK,self.offsets)
        print(qf)
    
    def moveLegsByPose(self,pts, basePos):
        qIK = IK_robot (pts,1,0)
        legOffsets = self.offsets[6:18]
        qf = basePos[0:6] + self.qValsToBits(qIK,legOffsets)
        qf.append(pts[-2])
        qf.append(+ pts[-1])
        self.moveRobotByQVals(qf)

    def moveRobotByJacobian(self):
        pass

    def qValsToBits(self,qRad, offset):
        qBits = []
        for i in range(0, len(qRad)):
            qBits.append(rad2bits(qRad[i], offset[i]))
        return qBits