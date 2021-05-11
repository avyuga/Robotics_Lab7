import numpy as np
from math import *


def transfer(theta1, theta2, theta3):
    theta1 = np.deg2rad(theta1)
    theta2 = np.deg2rad(theta2)
    theta3 = np.deg2rad(theta3)
    a2 = a3 = 0.128
    d1 = 0.18

    x = cos(theta1)*(a2*cos(theta2) + a3*cos(theta3))
    y = sin(theta1) * (a2 * cos(theta2) + a3 * cos(theta3))
    z = d1 + a2 * sin(theta2) + a3 * sin(theta3)
    print("Прямой перевод: ")
    print("x = ", x)
    print("y = ", y)
    print("z = ", z)
    # transfer_back(x, y, z)


def transfer_back(x, y, z):
    a2 = a3 = 0.128
    d1 = 0.18
    theta1 = atan(y/x)
    L_sq = x**2 + y**2 + (z - d1)**2
    theta2 = atan((z-d1)/sqrt(x**2 + y**2)) - acos((L_sq + a2**2 - a3**2)/(2*a2*sqrt(L_sq)))
    theta3 = theta2 + acos((L_sq - (a2**2 + a3**2))/(2*a2*a3))
    theta1 = np.rad2deg(theta1)
    theta2 = np.rad2deg(theta2)
    theta3 = np.rad2deg(theta3)
    print("Обратный перевод:")
    print("theta1 = ", theta1)
    print("theta2 = ", theta2)
    print("theta3 = ", theta3)
    transfer(theta1, theta2, theta3)


transfer_back(0.0903, 0.1698, 0.0041)
# transfer(62, -47, 7)
