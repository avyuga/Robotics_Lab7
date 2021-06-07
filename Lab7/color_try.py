#!/usr/bin/env python3
from ev3dev.ev3 import *
import time


Sound.beep()
color_sensor = ColorSensor()
color_sensor.mode = 'RGB-RAW'
file = open("color_try.txt", 'w')
time_start = time.time()
time_zero = time_start
while True:
    if time.time() - time_zero > 0.1:
        red = "Red: " + str(color_sensor.value(0)) + "\t"
        green = "Green: " + str(color_sensor.value(1)) + "\t"
        blue = "Blue: " + str(color_sensor.value(2)) + "\t"
        file.write(str(time.time() - time_start) + '\t' + red + green + blue + "\n")
        time_zero = time.time()
    if time.time() - time_start > 10: break
file.close()