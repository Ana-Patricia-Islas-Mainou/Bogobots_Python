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

class Bogobot(Node):
	def __init__(self):
		super().__init__(NODE_NAME)
		self.ctr = 0
		
		self.create_timer(1.0,self.callback)
		self.robot = HUMANOID_ROBOT(ROBOT_NAME)
		
	def callback(self):
		self.get_logger().info("Hola mundo " + str(self.ctr))
		self.ctr += 1
		
	def stop(self):
		print("Ending comunication with DXL and colsing ports")
		
def main(arg=None):
	rclpy.init(args=arg)
	nodeh = Bogobot()
	try: rclpy.spin(nodeh)
	except Exception as error: 
		nodeh.stop()
		print(error)
	except KeyboardInterrupt: 
		nodeh.stop()
		print("Node terminated by user")
	
if __name__ == "__main__":
	main()
