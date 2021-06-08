#!/usr/bin/env python3
from ev3dev.ev3 import *
import time


def saturate(x, left, right):
    if x > right: x = right
    if x < left: x = left
    return x


sound = Sound()
sound.set_volume(100)
sound.beep()

# первая координата - motorA
# вторая координата - motorB
# третья координата - motorC
q0 = [-90, -12, 80]
# калибровка координат
q0 = [saturate(q0[0], -180, 180), saturate(q0[1], -70, 135), saturate(q0[2], -120, 100)]
q = [5 * q0[0], -5 * q0[1], -5/3 * q0[2]]

# значение коэффициентов в градусных мерах
k_p = [0.3, 0.3, 0.1]
k_i = [0.25/60, 0.25/60, 0]
k_d = [1/60, 1/60, 0]


motorA = LargeMotor('outA')
motorB = LargeMotor('outB')
motorC = MediumMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0

timeStart = time.time()
last_t = time.time()
sum = 0
last_e = 0
inaccuracy = 5  # погрешность в градусах
U_max = 6.97

name = "code_color.txt"
file = open(name, 'w')

motors_set = [motorA, motorB, motorC]

for i in range(3):
    while abs(q[i] - motors_set[i].position) > inaccuracy:
        e = q[i] - motors_set[i].position
        dt = time.time() - last_t
        U = k_p[i] * e + k_d[i] * (e - last_e) / dt + k_i[i] * sum * dt
        U = U/U_max*100
        motors_set[i].run_direct(duty_cycle_sp=saturate(U, -100, 100))
        file.write(str(time.time() - timeStart) + '\t' + str(motorA.position/5) + '\t' +
                   str(motorB.position/5) + '\t' + str(motorC.position/5*3) + '\n')
        sum += e
        last_e = e
        last_t = time.time()
    sum = 0
    last_e = 0
    last_t = time.time()
    motors_set[i].run_direct(duty_cycle_sp=0)


color_sensor = ColorSensor('in4')
red_component = blue_component = green_component = 0
counter = 0
time_start_color = time.time()
while time.time() - time_start_color < 0.5:
    counter += 1
    red_component += color_sensor.value(0)
    green_component += color_sensor.value(1)
    blue_component += color_sensor.value(2)
red_ideal = red_component/counter
green_ideal = green_component/counter
blue_ideal = blue_component/counter

time_zero = time.time()

motorA_starters = motorA.position

while (motorA.position - motorA_starters) < 180*5:
    if time.time() - time_zero > 0.1:
        red = str(color_sensor.value(0)/red_ideal*255) + "\t"
        green = str(color_sensor.value(1)/green_ideal*255) + "\t"
        blue = str(color_sensor.value(2)/blue_ideal*255) + "\t"
        time_zero = time.time()
        file.write(str(time.time() - timeStart) + '\t' + str(motorA.position/5) +
                   '\t' + str(motorB.position/5) + '\t' + str(motorC.position/5*3) + '\t'
                   + red + green + blue + "\n")
        
    motorA.run_direct(duty_cycle_sp=10)
motorA.run_direct(duty_cycle_sp=0)
file.close()
