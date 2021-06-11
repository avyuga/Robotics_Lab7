import numpy as np
from math import *


def straight_transfer_formulas(theta1, theta2, theta3):
    theta3 = theta2-theta3
    theta1 = np.deg2rad(theta1)
    theta2 = np.deg2rad(theta2)
    theta3 = np.deg2rad(theta3)
    a = [0, 0.007, 0.128, 0.128]  # массив значений a_i
    alpha = [0, pi / 2, 0, 0]
    d = [0, 0.18, 0, 0]  # массив значений d_i
    x = (a[2] * cos(theta2) + a[3] * cos(theta3)) * cos(theta1)
    y = (a[2] * cos(theta2) + a[3] * cos(theta3)) * sin(theta1)
    z = d[1] + a[2] * sin(theta2) + a[3] * sin(theta3)
    x=round(x, 4)
    y=round(y, 4)
    z=round(z, 4)
    print("x = ", x)
    print("y = ", y)
    print("z = ", z)
    print(x, ",", y, ",", z)


def straight_transfer(theta1, theta2, theta3):
    theta3 = -theta3
    # перевод из градусов в радианы
    theta1 = np.deg2rad(theta1)
    theta2 = np.deg2rad(theta2)
    theta3 = np.deg2rad(theta3)
    Q = np.array([[0], [0], [0], [1]])

    a = [0, 0, 0.128, 0.128]  # массив значений a_i
    alpha = [0, pi / 2, 0, 0]
    d = [0, 0.18, 0, 0]  # массив значений d_i

    T_0_1 = np.array([[cos(theta1), -sin(theta1) * cos(alpha[1]), sin(theta1) * sin(alpha[1]), a[1] * cos(theta1)],
                      [sin(theta1), cos(theta1) * cos(alpha[1]), -cos(theta1) * sin(alpha[1]), a[1] * sin(theta1)],
                      [0, sin(alpha[1]), cos(alpha[1]), d[1]],
                      [0, 0, 0, 1]])

    T_1_2 = np.array([[cos(theta2), -sin(theta2) * cos(alpha[2]), sin(theta2) * sin(alpha[2]), a[2] * cos(theta2)],
                      [sin(theta2), cos(theta2) * cos(alpha[2]), -cos(theta2) * sin(alpha[2]), a[2] * sin(theta2)],
                      [0, sin(alpha[2]), cos(alpha[2]), d[2]],
                      [0, 0, 0, 1]])

    T_2_3 = np.array([[cos(theta3), -sin(theta3) * cos(alpha[3]), sin(theta3) * sin(alpha[3]), a[3] * cos(theta3)],
                      [sin(theta3), cos(theta3) * cos(alpha[3]), -cos(theta3) * sin(alpha[3]), a[3] * sin(theta3)],
                      [0, sin(alpha[3]), cos(alpha[3]), d[3]],
                      [0, 0, 0, 1]])
    T = T_0_1.dot(T_1_2).dot(T_2_3)
    XYZ = T.dot(Q)
    x = round(XYZ[0][0], 4)
    y = round(XYZ[1][0], 4)
    z = round(XYZ[2][0], 4)
    print("x = ", x)
    print("y = ", y)
    print("z = ", z)
    print(x, ",", y, ",", z)

def backwards_transfer(x, y, z):
    a = [0, 0, 0.128, 0.128]  # массив значений a_i
    d = [0, 0.18, 0, 0]  # массив значений d_i
    r1 = sqrt(x ** 2 + y ** 2)
    r2 = z - d[1]
    r3 = sqrt(r1 ** 2 + r2 ** 2)
    theta1 = atan(y / x)

    print((a[2] ** 2 + r3 ** 2 - a[3] ** 2) / (2 * a[2] * r3))
    psi1 = acos((a[2] ** 2 + r3 ** 2 - a[3] ** 2) / (2 * a[2] * r3))
    psi2 = atan(r2 / r1)
    print("psi1=", round(np.rad2deg(psi1), 3), "psi2=", round(np.rad2deg(psi2), 3))
    theta2 = psi2 + psi1

    psi3 = acos((a[2] ** 2 + a[3] ** 2 - r3 ** 2) / (2 * a[2] * a[3]))
    theta3 = pi - psi3

    theta1 = round(np.rad2deg(theta1), 3)
    theta2 = round(np.rad2deg(theta2), 3)
    theta3 = round(np.rad2deg(theta3), 3)

    print(theta1)
    print(theta2)
    print(theta3)
    print(theta1, ",", theta2, ",", theta3)


# принимает значения в градусах
straight_transfer_formulas(80.4, -11.0, 87.6)
