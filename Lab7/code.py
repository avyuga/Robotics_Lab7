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
q0 = [90, 45, 45]
q = [5 * q0[0], 5 * q0[1], 5/3 * q0[2]]

# Р·РЅР°С‡РµРЅРёРµ РєРѕСЌС„С„РёС†РёРµРЅС‚РѕРІ РІ РіСЂР°РґСѓСЃРЅС‹С… РјРµСЂР°С…
k_p = [0.6, 0.3, 0.5]
k_i = [0.00001, 0.00001, 0.00001]
k_d = [0.9, 0.1, 0.1]

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
inaccuracy = 10  # РїРѕРіСЂРµС€РЅРѕСЃС‚СЊ РІ РіСЂР°РґСѓСЃР°С…

name = str(q0[0]) + "_" + str(q0[1]) + "_" + str(q0[2]) + ".txt"
file = open(name, 'w')

motors_set = [motorA, motorB, motorC]
while time.time() - timeStart < 20:
    for i in range(3):
        while abs(motors_set[i].position + inaccuracy) < q[i]:
            e = q[i] - motors_set[i].position
            dt = time.time() - last_t
            U = k_p[i] * e + k_d[i] * (e - last_e) / dt + k_i[i] * sum * dt
            motors_set[i].run_direct(duty_cycle_sp=saturate(U, -100, 100))
            file.write(str(motorA.position) + '\t' + str(motorB.position) + '\t' + str(motorC.position) + '\t' + str(
                saturate(U, -100, 100)) + '\n')
            sum += e
            last_e = e
            last_t = time.time()
        sum = 0
        last_e = 0
        last_t = time.time()


file.close()
