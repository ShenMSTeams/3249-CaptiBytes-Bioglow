from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from distance_sensor import AndySensor

def MissionTwo(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Two")
   
   def MissionTwo(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Two")
   
   #drone survey
   #make sure to hit tab
   #download mission main.
   #Straight to  push up LIDAR
    robot.straight(743)
    # Turn and Push 
    robot.turn(-70)
    # Turn Back
    robot.turn(70)
    #go Backwards
    robot.straight(-743)
