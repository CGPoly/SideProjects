import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

time_step = 0.001
steps = 100
plt.axis('equal')


def count(n=0):
    while True:
        if round(n*1/(time_step/10))*time_step/10 == round(n):
            print(round(n))
        n += time_step
        yield n
        
        
def generate(n):
    listX = []
    listY = []
    for phi in range(int(16 * np.pi * steps) + steps):
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
