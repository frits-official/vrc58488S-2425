# Drivetrain: Left pod 1, 2; Right pod 3, 5
# Intake: 19, 20
# Lady brown: 16
# IMU: 15

from vex import *
from constant import *

brain = Brain()

class controller:
    master = Controller(PRIMARY)
    partner = Controller(PARTNER)

class drivetrain:
    leftMotorGroup = MotorGroup(Motor(Ports.PORT1), 
                                Motor(Ports.PORT2))
    rightMotorGroup = MotorGroup(Motor(Ports.PORT3), 
                                Motor(Ports.PORT5))
    
    drivetrain = DriveTrain(leftMotorGroup, rightMotorGroup,
                            DRIVETRAIN.WHEEL_DIAMETER, 
                            DRIVETRAIN.TRACK_WIDTH,
                            DRIVETRAIN.WHEEL_BASE,
                            DistanceUnits.IN,
                            DRIVETRAIN.GEAR_RATIO)