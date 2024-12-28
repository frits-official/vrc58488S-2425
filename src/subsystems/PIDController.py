from vex import *
from subsystems import drivetrain
from devices import DrivetrainDevices
from constant import *
from utils import map_range

def calculateTick(distance): # inches
    return ((distance / DRIVETRAIN.WHEEL_C) * DRIVETRAIN.GEAR_RATIO) * 360

def drivePID(distance): # inches
    global error # how far the robot is from the target
    global integral # area under the error vs time graph
    integral = 0
    global derivative # slope of the error vs time graph
    global prevError # the error for the previous iteration of the PID loop
    prevError = 0
    global motorPower # how much power to apply to the motors, ranging from -1 (backwards at full power) to 1 (forwards at full power)
    global prevMotorPower # the motor power for the previous iteration of the PID loop
    prevMotorPower = 0
    driveDistance = calculateTick(distance)
    drivetrain.resetEncoder()

    while True:
        currentDistance = drivetrain.position()
        error = driveDistance - currentDistance

        if abs(error) < 200:
            integral += error # updated the integral term if |error| < 200

        derivative = error - prevError # calculate the derivative term

        motorPower = (DRIVETRAIN.DRIVE_PID[0] * error) + (DRIVETRAIN.DRIVE_PID[1] * integral) + (DRIVETRAIN.DRIVE_PID[2] * derivative)

        if motorPower > 1: motorPower = 1
        if motorPower < -1: motorPower = -1

        # slew rate limiter
        if motorPower > (prevMotorPower + DRIVETRAIN.SLEW_RATE): motorPower = prevMotorPower + DRIVETRAIN.SLEW_RATE
        if motorPower < (prevMotorPower - DRIVETRAIN.SLEW_RATE): motorPower = prevMotorPower - DRIVETRAIN.SLEW_RATE

        # cap motor range
        motorPower = map_range(motorPower, 0, 1, 0, 100)
        
        drivetrain.setPower(motorPower, motorPower)

        # Exit the PID if the robot is within 10 degrees of the target, and not going too fast
        if error > -10 and error < 10 and error - prevError > -10 and error - prevError < 10:
            break

        prevMotorPower = motorPower
        prevError = error

        wait(20, MSEC)
        
    drivetrain.setPower(0, 0)

def turnPID(rotation): # degree
    global error # how far the robot is from the target
    global integral # area under the error vs time graph
    integral = 0
    global derivative # slope of the error vs time graph
    global prevError # the error for the previous iteration of the PID loop
    prevError = 0
    global motorPower # how much power to apply to the motors, ranging from -1 (backwards at full power) to 1 (forwards at full power)
    global prevMotorPower # the motor power for the previous iteration of the PID loop
    prevMotorPower = 0
    global startDistance
    startDistance = 0

    while True:
        # Calculate the current distance of the robot and store it as a number (float)
        currentDistance = startDistance - DrivetrainDevices.imu.rotation(DEGREES)
        error = rotation - currentDistance

        if abs(error) < 10:
            integral += error # updated the integral term if |error| < 10

        derivative = error - prevError

        motorPower = (DRIVETRAIN.TURN_PID[0] * error) + (DRIVETRAIN.TURN_PID[1] * integral) + (DRIVETRAIN.TURN_PID[2] * derivative)

        if motorPower > 1: motorPower = 1
        if motorPower < -1: motorPower = -1

        # slew rate limiter
        if motorPower > (prevMotorPower + DRIVETRAIN.SLEW_RATE): motorPower = prevMotorPower + DRIVETRAIN.SLEW_RATE
        if motorPower < (prevMotorPower - DRIVETRAIN.SLEW_RATE): motorPower = prevMotorPower - DRIVETRAIN.SLEW_RATE

        # cap motor range
        motorPower = map_range(motorPower, 0, 1, 0, 100)

        drivetrain.setPower(motorPower, -motorPower)

        # Exit the PID if the robot is within 10 degrees of the target, and not going too fast
        if error > -1 and error < 1 and error - prevError > -0.3 and error - prevError < 0.3:
            break

        prevMotorPower = motorPower
        prevError = error

        wait(20, MSEC)
        
    drivetrain.setPower(0, 0)