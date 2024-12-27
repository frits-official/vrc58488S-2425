from vex import *
from runmode import pre_auton, auto, teleop

pre_auton.control()

comp = Competition(driver=teleop.control, autonomous=auto.control)