import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots(dpi=250)
line, = ax.plot([], [], lw=0.5, color="blue")
line_reg, = ax.plot([], [], lw=0.5, color="red")

d_step = 0.25
change = 5
steps = 100
plt.axis('equal')


def fft(a: int, b: int):
    h: int
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    while True:
        h = a % b
        a = b
        b = h
        if b == 0:
            return abs(a)


def count():
    a = 0
    b = 1
    d = 1
    in_d = False
    while True:
        if in_d:
            if d > 360:
                d = 1
                in_d = False
            d += 1
            while fft(360, d) != 1:
                d += 1
            time.sleep(0.1)
            # d += d_step
            # while fft(360, d) != 1:
            #     d += d_step
        else:
            if a < change:
                print(str(a) + "/" + str(b))
                a += 1
                while fft(a, b) != 1:
                    a += 1
                    if not a < change:
                        a = 1
                        b += 1
            else:
                a = 1
                b += 1
            in_d = True
        yield a/b, b, d


def generate(data):
    n = data[0]
    b = data[1]
    d = data[2]
    # regular Rose
    listX = []
    listY = []
    for phi in range(int((2*b) * np.pi * steps)+steps):
        listX.append(np.cos(n * phi / steps) * np.cos(phi / steps))
        listY.append(np.cos(n * phi / steps) * np.sin(phi / steps))
    line_reg.set_data(listX, listY)

    # maurer Rose
    listX = []
    listY = []
    for phi in range(361):  # only works in degrees
        listX.append(np.cos(n * phi*d*2*np.pi/360) * np.cos(phi*d*2*np.pi/360))
        listY.append(np.cos(n * phi*d*2*np.pi/360) * np.sin(phi*d*2*np.pi/360))
    line.set_data(listX, listY)
    return line, line_reg


def init():
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(-1.5, 1.5)
    return line, line_reg


# ani_reg = animation.FuncAnimation(fig, generate_regular, count_reg, blit=False, interval=10, repeat=False, init_func=init_reg)
ani = animation.FuncAnimation(fig, generate, count, blit=False, interval=10, repeat=False, init_func=init)
plt.show()