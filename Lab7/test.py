#!/usr/bin/env python3
from ev3dev.ev3 import *

sound = Sound()
sound.set_volume(100)
sound.beep()

motorA = MediumMotor('outA')
motorB = LargeMotor('outB')
motorC = LargeMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0

motorA.run_direct(duty_cycle_sp=100)
motorB.run_direct(duty_cycle_sp=100)
motorC.run_direct(duty_cycle_sp=100)
