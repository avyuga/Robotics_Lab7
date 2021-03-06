#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
from math import *


def straight_transfer_formulas(theta1, theta2, theta3):
    theta3 = theta2 - theta3
    theta1 = theta1*pi/180
    theta2 = theta2*pi/180
    theta3 = theta3*pi/180
    a = [0, 0.007, 0.128, 0.128]  # массив значений a_i
    alpha = [0, pi / 2, 0, 0]
    d = [0, 0.18, 0, 0]  # массив значений d_i
    x = (a[2] * cos(theta2) + a[3] * cos(theta3)) * cos(theta1)
    y = (a[2] * cos(theta2) + a[3] * cos(theta3)) * sin(theta1)
    z = d[1] + a[2] * sin(theta2) + a[3] * sin(theta3)
    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)
    # print("x = ", x)
    # print("y = ", y)
    # print("z = ", z)
    return(x, ",", y, ",", z)


# DEPRECATED
# КНОПКА НЕ НУЖНА
# TRY
#

Sound.beep()
color_sensor = ColorSensor('in4')
button = TouchSensor('in3')

time_start = time.time()
color_sensor.mode = 'RGB-RAW'
file = open("color.txt", 'w')

motorA = LargeMotor('outA')
motorB = LargeMotor('outB')
motorC = MediumMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0


while time.time() - time_start < 60:
    if button.value():
        red = "Red: " + str(color_sensor.value(0)) + "\t"
        green = "Green: " + str(color_sensor.value(1)) + "\t"
        blue = "Blue: " + str(color_sensor.value(2)) + "\t"
        file.write(str(time.time()-time_start) + '\t' + str(straight_transfer_formulas(motorA.position, motorB.position, motorC.position)) + '\t' + str(motorA.position) + '\t' + str(motorB.position) + '\t'+ str(motorC.position)
            + '\t' + red + green + blue + "\n")

file.close()
