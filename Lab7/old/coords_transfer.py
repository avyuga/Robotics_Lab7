import numpy as np
from math import*


def multiply(x, y):
    res = np.zeros((4, 4), dtype=float)
    elem = 0
    for i in range(4):        # для всех строк в первой матрице
        for k in range(4):        # для каждого столбца во второй матрице
            for j in range(4):        # подсчет значения каждого пересечения
                elem += x[i][j] * y[j][k]
            res[i][k] = elem
            elem = 0
    return res


def multiply_vector(x, y):
    res = np.zeros((4, 1), dtype=float)
    elem = 0
    for i in range(4):        # для всех строк в первой матрице
        for j in range(4):        # подсчет значения каждого пересечения
            elem += x[i][j] * y[j][0]
        res[i][0] = elem
        elem = 0
    return res


def straight_transfer(theta1, theta2, theta3):
    # перевод из градусов в радианы
    theta1 = np.deg2rad(theta1)
    theta2 = np.deg2rad(theta2)
    theta3 = np.deg2rad(theta3)
    Q = np.array([[theta1], [theta2], [theta3], [1]])

    a = [0, 0.007, 0.128, 0.128]   # массив значений a_i
    alpha = [0, pi/2, 0, pi/2]   # alpha[3] либо pi, либо pi/2
    d = [0, 0.18, 0, 0]   # массив значений d_i

    T_0_1__1 = np.array([[cos(theta1), -sin(theta1), 0, 0],
                         [sin(theta1), cos(theta1), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    T_0_1__2 = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, d[1]],
                         [0, 0, 0, 1]])
    T_0_1__3 = np.array([[1, 0, 0, a[1]],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    T_0_1__4 = np.array([[1, 0, 0, 0],
                         [0, cos(alpha[1]), -sin(alpha[1]), 0],
                         [0, sin(alpha[1]), cos(alpha[1]), 0],
                         [0, 0, 0, 1]])

    T_0_1 = multiply(T_0_1__1, T_0_1__2)
    T_0_1 = multiply(T_0_1, T_0_1__3)
    T_0_1 = multiply(T_0_1, T_0_1__4)

    # T_0_1 = np.array([[cos(theta1), -sin(theta1)*cos(alpha[1]), sin(theta1)*sin(alpha[1]), a[1]*cos(theta1)],
    #                   [sin(theta1), cos(theta1)*cos(alpha[1]), -cos(theta1)*sin(alpha[1]), a[1]*sin(theta1)],
    #                   [0, sin(alpha[1]), cos(alpha[1]), d[1]],
    #                   [0, 0, 0, 1]])

    T_1_2__1 = np.array([[cos(theta2), -sin(theta2), 0, 0],
                         [sin(theta2), cos(theta2), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    T_1_2__2 = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, d[2]],
                         [0, 0, 0, 1]])
    T_1_2__3 = np.array([[1, 0, 0, a[2]],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    T_1_2__4 = np.array([[1, 0, 0, 0],
                         [0, cos(alpha[2]), -sin(alpha[2]), 0],
                         [0, sin(alpha[2]), cos(alpha[2]), 0],
                         [0, 0, 0, 1]])

    T_1_2 = multiply(T_1_2__1, T_1_2__2)
    T_1_2 = multiply(T_1_2, T_1_2__3)
    T_1_2 = multiply(T_1_2, T_1_2__4)
    # T_1_2 = np.array([[cos(theta2), -sin(theta2) * cos(alpha[2]), sin(theta2) * sin(alpha[2]), a[2] * cos(theta2)],
    #                   [sin(theta2), cos(theta2) * cos(alpha[2]), -cos(theta2) * sin(alpha[2]), a[2] * sin(theta2)],
    #                   [0, sin(alpha[2]), cos(alpha[2]), d[2]],
    #                   [0, 0, 0, 1]])

    T_2_3__1 = np.array([[cos(theta3), -sin(theta3), 0, 0],
                         [sin(theta3), cos(theta3), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    T_2_3__2 = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, d[3]],
                         [0, 0, 0, 1]])
    T_2_3__3 = np.array([[1, 0, 0, a[3]],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    T_2_3__4 = np.array([[1, 0, 0, 0],
                         [0, cos(alpha[3]), -sin(alpha[3]), 0],
                         [0, sin(alpha[3]), cos(alpha[3]), 0],
                         [0, 0, 0, 1]])

    T_2_3 = multiply(T_2_3__1, T_2_3__2)
    T_2_3 = multiply(T_2_3, T_2_3__3)
    T_2_3 = multiply(T_2_3, T_2_3__4)

    # T_2_3 = np.array([[cos(theta3), -sin(theta3) * cos(alpha[3]), sin(theta3) * sin(alpha[3]), a[3] * cos(theta3)],
    #                   [sin(theta3), cos(theta3) * cos(alpha[3]), -cos(theta3) * sin(alpha[3]), a[3] * sin(theta3)],
    #                   [0, sin(alpha[3]), cos(alpha[3]), d[3]],
    #                   [0, 0, 0, 1]])

    T = multiply(multiply(T_0_1, T_1_2), T_2_3)

    XYZ = multiply_vector(T, Q)
    print(XYZ)


def backwards_transfer(x, y, z):
    a = [0, 0.007, 0.128, 0.128]  # массив значений a_i
    d = [0, 0.18, 0, 0]  # массив значений d_i
    r1 = sqrt(x**2 + y**2)
    r2 = z - d[1]
    r3 = sqrt(r1**2 + r2**2)

    theta1 = atan(y/x)
    psi1 = acos((a[2]**2 + r3**2 - a[3]**2)/(2*a[2]*r3))
    psi2 = atan(r2/r1)
    theta2 = psi2 + psi1

    psi3 = acos((a[2]**2 + a[3]**2 - r3**2)/(2*a[2]*a[3]))
    theta3 = pi - psi3
    print("theta1 = ", np.rad2deg(theta1))
    print("theta2 = ", np.rad2deg(theta2))
    print("theta3 = ", np.rad2deg(theta3))


# принимает значения в градусах
straight_transfer(30, 30, 30)