from pybricks.tools import wait
from distance_sensor import AndySensor

def MissionZero(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Zero")
    #flip the rock
    robot.straight(560)
    robot.turn(-540)
    robot.straight(560)
  
    
