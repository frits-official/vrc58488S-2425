from vex import *
from devices import DrivetrainDevices, controller
from constant import *

def threshold(val):
   if abs(val) <= DRIVETRAIN.DRIVE_DEADBAND: return 0
   else: return val

def arcade_drive(straight, turn):
  straight = threshold(straight)
  turn = threshold(turn)

  left = straight + turn * 0.7 # the 0.7 makes the turns less intense
  right = straight - turn * 0.7

  DrivetrainDevices["leftMotor"].spin(FORWARD, left, PERCENT)
  DrivetrainDevices["rightMotor"].spin(FORWARD, right, PERCENT)

def cheesy_drive():  
  straight = threshold(controller["master"].axis3.position())
  turn = threshold(controller["master"].axis1.position())

  if abs(straight) <= turn:
    arcade_drive(0, turn)
    return

  left = straight + abs(straight) * turn
  right = straight - abs(straight) * turn

  mag = max(abs(left), abs(right))
  if mag > 1.0:
    left /= mag;
    right /= mag;

  DrivetrainDevices["leftMotor"].spin(FORWARD, left, PERCENT)
  DrivetrainDevices["rightMotor"].spin(FORWARD, right, PERCENT)

def control():
  while True:
    cheesy_drive()
    wait(20, MSEC)
