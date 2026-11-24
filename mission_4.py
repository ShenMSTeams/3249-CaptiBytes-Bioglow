from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionFour(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Four")
   #Feona@!!!!!!!!!
    robot.straight(385)
    left_attachment_motor.run_time(-1000,500)
    left_attachment_motor.run_time(1000,1500)
    robot.straight(-50)
    left_attachment_motor.run_time(-1000,500)
    left_attachment_motor.run_time(1000,1500)
    robot.straight(150)
    robot.straight(-400)
