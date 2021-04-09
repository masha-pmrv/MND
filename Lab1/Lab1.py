import random

a0 = 3
a1 = 4
a2 = 2
a3 = 3

x1 = [random.randint(0, 20) for _ in range(8)]
x2 = [random.randint(0, 20) for _ in range(8)]
x3 = [random.randint(0, 20) for _ in range(8)]


def calculate_y(x_1, x_2, x_3):
    return a0 + a1 * x_1 + a2 * x_2 + a3 * x_3


y = [calculate_y(x1[i], x2[i], x3[i]) for i in range(8)]

x01 = (max(x1) + min(x1)) / 2
x02 = (max(x2) + min(x2)) / 2
x03 = (max(x3) + min(x3)) / 2

dx1 = x01 - min(x1)
dx2 = x02 - min(x2)
dx3 = x03 - min(x3)

xn1 = [(x1[i] - x01) / dx1 for i in range(8)]
xn2 = [(x2[i] - x02) / dx2 for i in range(8)]
xn3 = [(x3[i] - x03) / dx3 for i in range(8)]

y_et = calculate_y(x01, x02, x03)

print(f'y: {y}')
print(f'y_et: {y_et}')
print(f'max((Y - Yet)^2): {max([(el - y_et) ** 2 for el in y])}')
