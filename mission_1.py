from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from distance_sensor import AndySensor
def MissionOne(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor ):
    print("Mission One ")
    