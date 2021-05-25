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

# РїРµСЂРІР°СЏ РєРѕРѕСЂРґРёРЅР°С‚Р° - motorA
# РІС‚РѕСЂР°СЏ РєРѕРѕСЂРґРёРЅР°С‚Р° - motorB
# С‚СЂРµС‚СЊСЏ РєРѕРѕСЂРґРёРЅР°С‚Р° - motorC
Q = [[90, -2, 78], [-27, 34, 57], [20, -10, 20], [0, 45, 10], [-90, 90, 0]]

# Р·РЅР°С‡РµРЅРёРµ РєРѕСЌС„С„РёС†РёРµРЅС‚РѕРІ РІ РіСЂР°РґСѓСЃРЅС‹С… РјРµСЂР°С…
k_p = [0.3, 0.3, 0.1]
k_i = [0.25 / 60, 0.25 / 60, 0]
k_d = [1 / 60, 1 / 60, 0]

inaccuracy = 5  # РїРѕРіСЂРµС€РЅРѕСЃС‚СЊ РІ РіСЂР°РґСѓСЃР°С…
U_max = 6.97

motorA = LargeMotor('outA')
motorB = LargeMotor('outB')
motorC = MediumMotor('outC')

motorA.position = 0
motorB.position = 0
motorC.position = 0

motors_set = [motorA, motorB, motorC]

for i in range(5):
    q0 = Q[i]
    name = "square1_" + str(i) + "___" + str(q0[0]) + "_" + str(q0[1]) + "_" + str(q0[2]) + ".txt"
    file = open(name, 'w')

    # РєР°Р»РёР±СЂРѕРІРєР° РєРѕРѕСЂРґРёРЅР°С‚
    q0 = [saturate(q0[0], -180, 180), saturate(q0[1], -70, 40), saturate(q0[2], -120, 100)]
    q = [5 * q0[0], -5 * q0[1], -5 / 3 * q0[2]]

    timeStart = time.time()
    last_t = time.time()
    sum = 0
    last_e = 0

    for j in range(3):
        while abs(q[j] - motors_set[j].position) > inaccuracy:
            e = q[j] - motors_set[j].position
            dt = time.time() - last_t
            U = k_p[j] * e + k_d[j] * (e - last_e) / dt + k_i[j] * sum * dt
            U = U / U_max * 100
            motors_set[j].run_direct(duty_cycle_sp=saturate(U, -100, 100))
            file.write(str(motorA.position) + '\t' + str(motorB.position) + '\t' + str(motorC.position) + '\t' + str(
                saturate(U, -100, 100)) + '\t' + str(k_p[j] * e) + '\t' + str(k_d[j] * (e - last_e) / dt) + '\t' +
                       str(k_i[j] * sum * dt) + '\n')
            sum += e
            last_e = e
            last_t = time.time()
        sum = 0
        last_e = 0
        last_t = time.time()
        motors_set[j].run_direct(duty_cycle_sp=0)

    sound = Sound()
    sound.set_volume(100)
    sound.beep
    time.sleep(3)

file.close()
