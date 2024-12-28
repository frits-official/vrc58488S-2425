from vex import *
from devices import *

def check_motor():
    uninstalledPort = []
    for port in motorPorts:
        if not Motor(port).installed():
            uninstalledPort.append(port + 1)
    return uninstalledPort

def control():
    while True:
        brain.screen.clear_screen()
        brain.screen.print("Button A to recheck")
        brain.screen.new_line()
        
        motorCheck = check_motor()
        if len(motorCheck) > 0:
            for port in motorCheck:
                brain.screen.print("motor " + str(port) + " not connected")
                brain.screen.new_line()
            while not controller.master.buttonA.pressing():
                controller.master.rumble("...---...")
                wait(100, MSEC)
        else: 
            break

    DrivetrainDevices.leftMotor.set_max_torque(100, PERCENT)
    DrivetrainDevices.rightMotor.set_max_torque(100, PERCENT)
    DrivetrainDevices.leftMotor.stop()
    DrivetrainDevices.rightMotor.stop()

    intakeMotor.set_max_torque(100, PERCENT)
    intakeMotor.stop()