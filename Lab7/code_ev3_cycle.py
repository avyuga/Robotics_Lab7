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

Q = [[90, -2, 78], [-27, 34, 57], [20, -10, 20], [0, 45, 10], [-90, 90, 0]]

k_p = [0.2, 0.2, 0.05]
k_i = [0.25 / 60, 0.25 / 60, 0]
k_d = [1 / 60, 1 / 60, 0]

inaccuracy = 5
U_max = 7.04

motorA = LargeMotor('outA')
motorB = LargeMotor('outB')
motorC = MediumMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0

motors_set = [motorA, motorB, motorC]
e = [0, 0, 0]
U = [0, 0, 0]

for i in range(5):
    q0 = Q[i]
    name = "square2_" + str(i) + "___" + str(q0[0]) + "_" + str(q0[1]) + "_" + str(q0[2]) + ".txt"
    file = open(name, 'w')

    q0 = [saturate(q0[0], -180, 180), saturate(q0[1], -70, 135), saturate(q0[2], -120, 100)]
    q = [5 * q0[0], -5 * q0[1], -5 / 3 * q0[2]]

    timeStart = time.time()
    last_t = time.time()
    sum = [0, 0, 0]
    last_e = [0, 0, 0]

    for j in range(3):
        while abs(q[0] - motors_set[0].position) > inaccuracy or abs(q[1] - motors_set[1].position) > inaccuracy or abs(
                q[2] - motors_set[2].position) > inaccuracy:
            for i in range(3):
                e[i] = q[i] - motors_set[i].position
                dt = time.time() - last_t
                U[i] = k_p[i] * e[i] + k_d[i] * (e[i] - last_e[i]) / dt + k_i[i] * sum[i] * dt
                U[i] = U[i] / U_max * 100
                sum[i] += e[i]
                last_e[i] = e[i]
                last_t = time.time()
            motorA.run_direct(duty_cycle_sp=saturate(U[0], -100, 100))
            motorB.run_direct(duty_cycle_sp=saturate(U[1], -100, 100))
            motorC.run_direct(duty_cycle_sp=saturate(U[2], -100, 100))
            file.write(str(motorA.position) + '\t' + str(motorB.position) + '\t' + str(motorC.position) + '\n')

        motorA.run_direct(duty_cycle_sp=0)
        motorB.run_direct(duty_cycle_sp=0)
        motorC.run_direct(duty_cycle_sp=0)
        sound.beep()

    file.close()
