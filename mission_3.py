from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionThree(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Three")
    right_attachment_motor.run_time (150,2220) 
    left_attachment_motor.run_time(150,2250)
    robot.straight(80)
    robot.turn(45)
    robot.straight(190)
    left_attachment_motor.run_time(-150,2250)
    robot.straight(-200)