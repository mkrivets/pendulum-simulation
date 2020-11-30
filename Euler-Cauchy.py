import numpy as np
import matplotlib.pyplot as plt

v = 0.2  # frequency
a = 0.3  # amplitude
g = 9.8  # free fall acceleration
length = 20  # length of rigid and light pendulum

t0 = 0  # moment
h = 0.01  # step
y0 = np.pi / 3  # angle
u0 = 1  # accelerate

approx_y_list = []
accurate_y_list = []
approx_u_list = []
accurate_u_list = []
t_list = []

accurate_y_list.append(y0)
accurate_u_list.append(u0)
approx_y_list.append(0)
approx_u_list.append(0)


def derivative_func(t, f):
    return (-g - a * pow(v, 2) * np.cos(v * t)) * (np.sin(f) / length)


t = 0
while (t < 100):
    t_list.append(t)
    t += h

i = 1
while (i < len(t_list)):
    approx_y_list.append(accurate_y_list[i - 1] + h * accurate_u_list[i - 1])  # approx y [i]
    approx_u_list.append(
        accurate_u_list[i - 1] + h * derivative_func(t_list[i - 1], accurate_y_list[i - 1]))  # approx u [i]
    accurate_u_list.append(accurate_u_list[i - 1] + (h / 2) *
                           (derivative_func(t_list[i - 1], accurate_y_list[i - 1]) +
                            derivative_func(t_list[i], approx_y_list[i])))  # accurate u [i]
    accurate_y_list.append(accurate_y_list[i - 1] + (h / 2) * (accurate_u_list[i - 1] + accurate_u_list[i]))
    i += 1

print(accurate_y_list)
plt.plot(t_list, accurate_y_list)
plt.savefig('Euler-Cauchy.png')
plt.show()