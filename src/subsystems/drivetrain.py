from vex import *
from devices import DrivetrainDevices, controller
from constant import *
from utils import map_range

def threshold(val):
   if abs(val) <= DRIVETRAIN.DRIVE_DEADBAND: return 0
   else: return val

def setPower(left, right):
  DrivetrainDevices.leftMotor.spin(FORWARD, left, PERCENT)
  DrivetrainDevices.rightMotor.spin(FORWARD, right, PERCENT)

def arcade_drive(straight, turn):
  straight = threshold(straight)
  turn = threshold(turn)

  left = straight + turn * 0.7 # the 0.7 makes the turns less intense
  right = straight - turn * 0.7

  setPower(left, right)

def cheesy_drive():  
  straight = threshold(controller.master.axis3.position())
  turn = threshold(controller.master.axis1.position())

  if abs(straight) <= turn:
    arcade_drive(0, turn)
    return

  left = straight + abs(straight) * turn
  right = straight - abs(straight) * turn

  mag = max(abs(left), abs(right))
  if mag > 100:
    left = map_range(left, 0, mag, 0, 100)
    right = map_range(right, 0, mag, 0, 100)

  setPower(left, right)

def control():
  while True:
    cheesy_drive()
    wait(20, MSEC)

def position():
  return (DrivetrainDevices.leftMotor.position(DEGREES) + DrivetrainDevices.rightMotor.position(DEGREES)) / 2

def resetEncoder():
  DrivetrainDevices.leftMotor.set_position(0)
  DrivetrainDevices.rightMotor.set_position(0)