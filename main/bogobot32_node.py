#!/usr/bin/env python3

ROBOT_NAME = "BOGOBOT 3.2"

if ROBOT_NAME == "BOGOBOT 3.1":
    from BOGO_3_1.BOGO_3_1_positions import *
    NODE_NAME = "BOGO_3_1"

if ROBOT_NAME == "BOGOBOT 3.2":
    from BOGO_3_2.BOGO_3_2_positions import *
    NODE_NAME = "BOGO_3_2"

import rclpy 
from rclpy.node import Node

from Humanoid_Robot import *

class Bogobot(Node, HUMANOID_ROBOT):
	def __init__(self):
		super().__init__(NODE_NAME)
		self.ctr = 0
		self.robot = HUMANOID_ROBOT(ROBOT_NAME)
		self.create_timer(1.0,self.callback)
		self.robot = HUMANOID_ROBOT(ROBOT_NAME)
		self.robot.setMotorsTorque(1)
       		
	def callback(self):
		self.robot.moveRobotByQVals(portero1_QVals)
		self.robot.moveRobotByQVals(portero2_QVals)
		
	def stop(self):
		self.robot.moveRobotByQVals(sitPos_QVals)
		self.robot.setMotorsTorque(0)
		print("Ending comunication with DXL and colsing ports")
		
def main(arg=None):
	rclpy.init(args=arg)
	startCom()
	nodeh = Bogobot()
	try: rclpy.spin(nodeh)
	except Exception as error: 
		nodeh.stop()
		print(error)
	except KeyboardInterrupt: 
		nodeh.stop()
		print("Node terminated by user")
	stopCom()
if __name__ == "__main__":
	main()
