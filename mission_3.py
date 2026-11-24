from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionThree(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Three")
    #exploding seeds/

    robot.straight(390)
    left_attachment_motor.run_time(850,1000) 
    robot.straight(-390)
   

    #right_attachment_motor.run_time (1000,750,Stop.HOLD, False) 
    #left_attachment_motor.run_time (-700,700) 
    #robot.straight(400)
    #robot.turn(55)
    #robot.straight(90)
    #right_attachment_motor.run_time (150,1000) 
  # robot.turn(30)
    #robot.straight(-700)
