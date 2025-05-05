from HUMANOID.ZMP_Models.ZMP_cartModel import *
from HUMANOID.Humanoid_Movement import *

class HUMANOID_WALKING_AlGORIRTHMS(HUMANOID_MOVEMENT):

    def __init__(self, ROBOT_NAME):
        super().__init__(ROBOT_NAME)

    def walk_cartModel_IK(self, Xzmp,  yzmp, radio, giro, tf, step, s, basePos):
        for i in range(0,s):
            t = 0
            dt = 0.1
            stop = t + tf
            #print("------------- inicio ciclo -----------")
            while (t < stop):
                pts = cartModel(Xzmp,yzmp,radio,giro,t,dt,tf,stop,i,step)
                print(pts)
                #print(pts)
                self.moveLegsByPose(pts,basePos)
                # moveRobot_byPose(portHandler,packetHandler,groupSyncWritePos,groupSyncWriteVel,IDs,walk_TaskS)
                t = t + dt