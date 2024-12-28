from vex import *
import math

class _DRIVETRAIN:
    WHEEL_C = 4 * math.pi
    GEAR_RATIO = 1.4
    DRIVE_DEADBAND = 2

    DRIVE_PID = [0.5, 0, 0]
    TURN_PID = [0.05, 0, 0]
    SLEW_RATE = 0.1
DRIVETRAIN = _DRIVETRAIN()