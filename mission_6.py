from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def MissionSix(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Six")



    robot.straight(592)
    robot.turn(-90)
    #push in skylight
    robot.straight(500)
    robot.turn(90)
    left_attachment_motor.run_time(50,100)
    robot.straight(90)
    left_attachment_motor.run_time(100,2000)
    left_attachment_motor.run_time(-100,2100)

    robot.straight(-200)
    #to blue base
    robot.turn(90)
    robot.straight(664)
    robot.turn(35)
    robot.straight(400)
    robot.turn(45)
    robot.straight(200)
