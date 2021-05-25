#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

color_sensor = ColorSensor('in4')
# button = TouchSensor('in4')

color_sensor.mode = 'COL-COLOR'
file = open("color.txt", 'w')
colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')

motorA = LargeMotor('outA')
motorB = LargeMotor('outB')
motorC = MediumMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0

time_zero = time.time()

while motorA.position < 180*5:
    if time.time() - time_zero > 0.1:
        if color_sensor.value() == 4 or color_sensor.value() == 5 or color_sensor.value() == 1:
            file.write(str(time.time()) + '\t' + colors[color_sensor.value()] + '\t' + str(motorA.position) +
                       '\t' + str(motorB.position) + '\t' + str(motorC.position) + "\n")
            time_zero = time.time()
        else:
            file.write(str(time.time()) + '\t' + colors[color_sensor.value()] + '\n')
    motorA.run_direct(duty_cycle_sp=-10)
motorA.run_direct(duty_cycle_sp=0)
file.close()
