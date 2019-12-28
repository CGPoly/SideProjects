import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

master = Tk()

fig = plt.Figure(dpi=200)
ax = fig.add_subplot()
ax.axis('equal')
result = FigureCanvasTkAgg(fig, master=master)
result.get_tk_widget().pack(side='right')

Label(master, text="n=").pack()
n_e = Entry(master)
n_e.pack()
n_e.insert(0, "0")
Label(master, text="d=").pack()
d_e = Scale(master, from_=0, to=360, orient="horizontal")
d_e.pack()
Label(master, text="len=").pack()
length_e = Scale(master, from_=0, to=25, orient="horizontal")
length_e.pack()
length_e.set(2)

while True:
    try:
        if n_e.get().count("/") == 1:
            tmp = n_e.get().split("/")
            n = float(tmp[0]) / float(tmp[1])
        else:
            n = float(n_e.get())
        d = d_e.get()
        length = length_e.get()
        ax.clear()
        
        steps = 100
        
        # maurer Rose
        listX = []
        listY = []
        for phi in range(361):  # only works in degrees
            listX.append(np.cos(n * phi * d * 2 * np.pi / 360) * np.cos(phi * d * 2 * np.pi / 360))
            listY.append(np.cos(n * phi * d * 2 * np.pi / 360) * np.sin(phi * d * 2 * np.pi / 360))
        ax.plot(listX, listY, lw=0.5, color="blue")
        
        # regular Rose
        if length != 0:
            listX = []
            listY = []
            for phi in range(int((2 * length) * np.pi * steps) + steps):
                listX.append(np.cos(n * phi / steps) * np.cos(phi / steps))
                listY.append(np.cos(n * phi / steps) * np.sin(phi / steps))
            ax.plot(listX, listY, lw=1, color="red")
            result.draw()
            master.update()
        else:
            ax.plot([], [], lw=1, color="red")
            result.draw()
            master.update()
    except ValueError:
        master.update()
# good values:
# 4; 101
