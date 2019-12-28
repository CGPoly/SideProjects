import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

wait = 0.5
rose_step = 0.01
change = 10
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
    a: float = 0
    b: float = 1
    yield a/b, b
    target_a: int = int(a)
    target_b: int = int(b)
    while b < change:
        if target_b > round(b*1/(rose_step/10))*rose_step/10:
            b += rose_step / (change-1)
            a -= rose_step
        elif target_a > round(a*1/(rose_step/10))*rose_step/10:
            a += rose_step
        elif round(a*1/(rose_step/10))*rose_step/10 < change:
            print(str(target_a) + "/" + str(target_b))
            target_a += 1
            while fft(target_a, target_b) != 1:
                target_a += 1
                if not a < change:
                    target_a = 1
                    target_b += 1

            time.sleep(wait)
        else:
            target_a = 1
            target_b += 1
            time.sleep(wait)
        yield a/b, b
    target_b += 1
    while target_b > round(b*1/(rose_step/10))*rose_step/10:
        b += rose_step / change
        a -= rose_step
        yield a/b, b


def generate(data):
    n = data[0]
    b = data[1]
    listX = []
    listY = []
    for phi in range(int((2*b) * np.pi * steps) + steps):
        listX.append(np.cos(n * phi / steps) * np.cos(phi / steps))
        listY.append(np.cos(n * phi / steps) * np.sin(phi / steps))
    line.set_data(listX, listY)
    return line,


def init():
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(-1.5, 1.5)
    return line,


ani = animation.FuncAnimation(fig, generate, count, blit=False, interval=10, repeat=False, init_func=init)
plt.show()
