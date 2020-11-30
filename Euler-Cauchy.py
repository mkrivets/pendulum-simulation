import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')

v = 0.2  # frequency
a = 0.1  # amplitude
g = 9.8  # free fall acceleration
length = 20  # length of rigid and light pendulum
tMax = 250  # the number of seconds

t0 = 0  # moment
h = 0.2  # step
y0 = np.pi / 3  # angle
u0 = 0.75  # accelerate

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
while (t < tMax):
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

# animation

x_horizontal = []
w_vertical = []
for y in accurate_y_list:
    x_horizontal.append(length * np.sin(y))
    w_vertical.append(length * np.cos(y))
print(x_horizontal)
print(w_vertical)

# Scatter plot
fig = plt.figure()
axes = fig.add_subplot()
axes.set_xlim(min(x_horizontal)-1, max(x_horizontal)+1)
axes.set_ylim(min(w_vertical)-1, max(w_vertical)+1)
plt.axis('square')

point, = axes.plot([x_horizontal[0]],[w_vertical[0]], 'go')
line, = axes.plot([x_horizontal[0],0],[w_vertical[0],0])

def ani(coords):
    point.set_data([coords[0]],[coords[1]])
    line.set_data([coords[0], 0],[coords[1], 0])
    return point, line

def frames():
    for x_pos, w_pos in zip(x_horizontal, w_vertical):
        yield x_pos, w_pos

ani = FuncAnimation(fig, ani, frames=frames, interval = 50)
ani.save("Euler-Cauchy.mp4")
plt.show()