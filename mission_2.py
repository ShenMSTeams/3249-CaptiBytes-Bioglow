from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from distance_sensor import AndySensor

def MissionTwo(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Two")
   #drone survey
   #make sure to hit tab
   #download mission main.

    robot.straight(700)
    robot.straight(-300)
    robot.turn(-90)
    robot.straight(300)
    robot.turn(90)
    robot.straight(1250)
    robot.turn (90)
    robot.straight(20)