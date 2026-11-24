from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from distance_sensor import AndySensor
def MissionOne(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor ):
    print("Mission One")
    #blue base
    robot.straight(675)
    robot.turn(60)
    left_attachment_motor.run_time(1000,700)
    left_attachment_motor.run_time(-1000,700)
    robot.straight(-50)
    robot.turn(-66)
    
    left_attachment_motor.run_time(50,100)
    left_attachment_motor.run_time(500,500)
    robot.straight(-90)
    robot.straight(90)
    left_attachment_motor.run(-1000,500)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #robot.turn(-23)
    #robot.straight(50)
    #left_attachment_motor.run_time(-1000,500)
    #robot.straight(-91)
    #robot.turn(-12)
    #motor_speed=(90)
    #left_attachment_motor.run_time(125,500)
    #robot.turn(10)
    #motor_speed=(200)
    #left_attachment_motor.run_time(-700,1000)
    #robot.turn(-60)
    #robot.straight(50)
    #left_attachment_motor.run_time(500,500)
    #robot.straight(-150)
    #robot.straight(100)
    #robot.turn(-45)
    #robot.straight(400)
    #left_attachment_motor.run_time(500,500)
    #robot.turn(100)
    #straight_speed=(50)
    #robot.straight(170)
    #robot.straight(-50)
    #robot.turn(-50)
    #robot.straight(-350)
