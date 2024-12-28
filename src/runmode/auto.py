from vex import *
from devices import *

def control():
    brain.screen.clear_screen()
    brain.screen.print("autonomous")

    DrivetrainDevices.leftMotor.set_position(0)
    DrivetrainDevices.rightMotor.set_position(0)