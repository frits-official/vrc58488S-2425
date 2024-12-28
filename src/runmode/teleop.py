from vex import *
from devices import brain
from subsystems import drivetrain, intake, mogo

def control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    
    Thread(callback=drivetrain.control)
    Thread(callback=intake.control)
    Thread(callback=mogo.control)

    while True:
        wait(20, MSEC)