import numpy as np
from math import*

def straight_transfer(theta1, theta2, theta3):
    # перевод из градусов в радианы
    theta1 = 5/3 * np.deg2rad(theta1)
    theta2 = 5 * np.deg2rad(theta2)
    theta3 = 5 * np.deg2rad(theta3)
    Q = np.array([[theta1], [theta2], [theta3], [1]])

    a = [0.007, 0.128, 0.128]   # массив значений a_i
    d = [0.18, 0, 0]   # массив значений d_i

    # матрицы перевода
    T_0_1 = np.array([[cos(theta1), 0, sin(theta1), a[0] * cos(theta1)],
                      [sin(theta1), 0, -cos(theta1), a[0] * sin(theta1)],
                      [0, 1, 0, d[0]],
                      [0, 0, 0, 1]])
    T_1_2 = np.array([[cos(theta2 + pi / 2), -sin(theta2 + pi/2), 0, a[1] * cos(theta2 + pi / 2)],
                      [sin(theta2 + pi / 2), cos(theta2 + pi / 2), 0, a[1] * sin(theta2 + pi / 2)],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    T_2_3 = np.array([[cos(theta3+pi), -sin(theta3+pi), 0, a[2] * cos(theta3+pi)],
                      [sin(theta3+pi), cos(theta3+pi), 0, a[2] * sin(theta3+pi)],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

    T = T_0_1.dot(T_1_2).dot(T_2_3)
    XYZ = T.dot(Q)
    print("x = ", XYZ[0][0])
    print("y = ", XYZ[1][0])
    print("z = ", XYZ[2][0])
    # backwards_transfer(XYZ[0][0], XYZ[1][0], XYZ[2][0])

def backwards_transfer(x, y, z):
    a = [0.007, 0.128, 0.128]  # массив значений a_i
    d = [0.18, 0, 0]  # массив значений d_i

    theta1 = atan(y/x)

    print((a[1] ** 2 + (x**2 + y**2 + z**2 - d[0]**2) - a[2]**2)/
          (2*a[1]*sqrt(x**2 + y**2 + (z - d[0])**2)))
    psi1 = acos((a[1] ** 2 + (x**2 + y**2 + (z - d[0])**2) - a[2]**2)/
              (2*a[1]*sqrt(x**2 + y**2 + (z - d[0])**2)))
    psi2 = atan((z-d[0])/(sqrt(x**2 + y**2)))
    theta2 = psi2 + psi1

    psi3 = acos((a[1]**2 + a[2]**2 - (x**2 + y**2) + (z - d[0])**2)/
                (2*a[1]*sqrt(x**2 + y**2 + (z - d[0])**2)))
    theta3 = pi - psi3
    print("theta1 = ", theta1)
    print("theta2 = ", theta2)
    print("theta3 = ", theta3)


# принимает значения в градусах
straight_transfer(10, 10, 10)
