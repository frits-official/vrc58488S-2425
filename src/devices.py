# Drivetrain: Left pod 1, 2; Right pod 3, 5
# Intake: 19, 20
# Lady brown: 16
# IMU: 15

from vex import *
from constant import *

brain = Brain()

motorPorts = [Ports.PORT1, Ports.PORT2, Ports.PORT3, Ports.PORT5, Ports.PORT19, Ports.PORT20, Ports.PORT16]

controller = {
    "master": Controller(PRIMARY),
    "partner": Controller(PARTNER)
}

DrivetrainDevices = {
    "leftMotor": MotorGroup(Motor(Ports.PORT1, GearSetting.RATIO_18_1, False), 
                                Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)),
    "rightMotor": MotorGroup(Motor(Ports.PORT3, GearSetting.RATIO_18_1, True), 
                                Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)),
    "imu": Gyro(Ports.PORT15)
}
Drivetrain = DriveTrain(DrivetrainDevices["leftMotor"], DrivetrainDevices["rightMotor"],
                            DRIVETRAIN.WHEEL_DIAMETER, 
                            DRIVETRAIN.TRACK_WIDTH,
                            DRIVETRAIN.WHEEL_BASE,
                            DistanceUnits.IN,
                            DRIVETRAIN.GEAR_RATIO)

intakeMotor = MotorGroup(Motor(Ports.PORT19, GearSetting.RATIO_18_1, True), 
                        Motor(Ports.PORT20, GearSetting.RATIO_18_1, True))

mogoPiston = {
    "piston1": DigitalOut(brain.three_wire_port.a),
    "piston2": DigitalOut(brain.three_wire_port.b)
}
    