from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor


def MissionFive(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Five")
    #reaching roots
    robot.turn(10)
    straight_acceleration=(100000)
    robot.straight(735)
    robot.turn(-5)
    motor_acceleration=(300000000)
    left_attachment_motor.run_time(2500, 900,wait=False)
    right_attachment_motor.run_time(2500, 900)
    robot.straight(-40)
    left_attachment_motor.run_time(-2500, 1500,wait=False)
    right_attachment_motor.run_time(-2500, 1500)
    robot.turn(5)
    #robot.straight(50)
    left_attachment_motor.run_time(2500, 900,wait=False)
    right_attachment_motor.run_time(2500, 900)
    #robot.straight(30)
    robot.straight(-20)
    left_attachment_motor.run_time(2500, 250,wait=False)
    right_attachment_motor.run_time(2500, 250)
    robot.straight(-735)
    #motor_acceleration=(100000000)
    #left_attachment_motor.run_time(-500, 1000)
    #left_attachment_motor.run_time(500, 1000)
    #robot.turn(9)
    #robot.straight(-700)
    #robot.turn(50)
