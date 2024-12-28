from vex import *
from devices import intakeMotor, controller

def control():
    while True:
        if controller.master.buttonB.pressing():
            intakeMotor.spin(FORWARD, 100, PERCENT)
        elif controller.master.buttonX.pressing():
            intakeMotor.spin(REVERSE, 100, PERCENT)
        elif controller.master.buttonA.pressing():
            intakeMotor.stop()
        wait(20, MSEC)