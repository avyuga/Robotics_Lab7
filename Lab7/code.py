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
q0 = [90, 45, 45]
q = [5 * q0[0], 5 * q0[1], 5/3 * q0[2]]

# значение коэффициентов в градусных мерах
k_p = [10, 20, 10]
k_i = [10, 5, 4]
k_d = [0, 5, 0]


motorA = MediumMotor('outA')
motorB = LargeMotor('outB')
motorC = LargeMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0

timeStart = time.time()
last_t = time.time()
sum = 0
last_e = 0
inaccuracy = 2  # погрешность в градусах

name = str(q[0]) + "_" + str(q[1]) + "_" + str(q[2]) + ".txt"
file = open(name, 'w')

motors_set = [motorA, motorB, motorC]

for i in range(3):
    while abs(motors_set[i].position + inaccuracy) < q[i]:
        e = q[i] - motors_set[i].position
        dt = time.time() - last_t
        U = k_p[i] * e + k_d[i] * (e - last_e) / dt + k_i[i] * sum * dt

        motors_set[i].run_direct(duty_cycle_sp=saturate(U, -100, 100))
        file.write(str(motorA.position) + '\t' + str(motorB.position) + '\t' + str(motorC.position) + '\n')

        sum += e
        last_e = e
        last_t = time.time()
    sum = 0
    last_e = 0
    last_t = time.time()

file.close()
