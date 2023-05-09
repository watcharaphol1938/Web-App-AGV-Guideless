from setup.structure import AutonomousMobileRobot, session
from components.processline import processline1, processline2, processline3, processline4

autonomousmobilrrobot1 = AutonomousMobileRobot(1, "I", processline1.processline_id)
autonomousmobilrrobot2 = AutonomousMobileRobot(2, "J", processline3.processline_id)
autonomousmobilrrobot3 = AutonomousMobileRobot(3, "K", processline2.processline_id)
autonomousmobilrrobot4 = AutonomousMobileRobot(4, "L", processline4.processline_id)
session.add(autonomousmobilrrobot1)
session.add(autonomousmobilrrobot2)
session.add(autonomousmobilrrobot3)
session.add(autonomousmobilrrobot4)