from vex import *
from devices import mogoPiston, controller

def set(val):
        mogoPiston["piston1"].set(val)
        mogoPiston["piston2"].set(val)

def control():
    while True:
        if controller["master"].buttonDown.pressing():
            set(True)
        elif controller["master"].buttonUp.pressing():
            set(False)
        wait(20, MSEC)