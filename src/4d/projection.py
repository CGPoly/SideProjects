import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

obj = []


# Hypercubes
def recursive_cuber(dimension, acc_old):
    if dimension <= 0:
        obj.append(acc_old)
        return
    for i in range(2):
        recursive_cuber(dimension - 1, acc_old + [(-1) ** i])


dim = 4
recursive_cuber(dim, [])
# 5-Cell
# obj = [[1/(10**0.5), 1/(6**0.5), 1/(3**0.5), 1],
#        [1/(10**0.5), 1/(6**0.5), 1/(3**0.5), -1],
#        [1/(10**0.5), 1/(6**0.5), -2/(3**0.5), 0],
#        [1/(10**0.5), -((3/2)**0.5), 0, 0],
#        [-2*((2/5)**0.5), 0, 0, 0]]
obj = np.asarray(obj)

# rotation = lambda angle: np.asarray([[1, 0, 0, 0],
#                                      [0, 1, 0, 0],
#                                      [0, 0, np.cos(angle), -np.sin(angle)],
#                                      [0, 0, np.sin(angle), np.cos(angle)]])
# 5D
rotation = lambda angle: np.asarray([[1, 0, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 0, np.cos(angle), -np.sin(angle)],
                                     [0, 0, np.sin(angle), np.cos(angle)]])
# Wrong but cool 5D rotation
# rotation = lambda angle: np.asarray([[1, 0, 0, 0, 0],
#                                      [0, 1, 0, 0, 0],
#                                      [0, 0, np.cos(angle), -np.sin(angle), 0],
#                                      [0, 0, 0, 1, 0],
#                                      [0, 0, 0, np.sin(angle), np.cos(angle)]])
# rotation = lambda angle: np.identity(dim)
distance = 2
# project = lambda w: np.asarray([[w, 0, 0, 0],
#                                 [0, w, 0, 0],
#                                 [0, 0, w, 0]])
project = lambda w, d: np.append(np.identity(d - 1) * w, np.zeros((d - 1, 1)), axis=1)

an = 0
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(-2, 2)

while True:
    ax.clear()
    Axes3D.set_xlim3d(ax, -2, 2)  # just to deactivate the unused Warning from Axes3D
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(-2, 2)
    
    rotated = np.asarray([np.dot(rotation(an), i) for i in obj])
    an += 0.1
    projected = rotated
    while projected.shape[1] > 3:
        projected = np.asarray([np.dot(project(1 / (distance - i[-1]), len(i)), i) for i in projected])
    edge = []
    for i in range(len(obj)):
        for j in range(len(obj)):
            if round((sum([(obj[i, n] - obj[j, n]) ** 2 for n in range(len(obj[i]))]) ** 0.5) * 1000) / 1000 == 2:
                edge.append([projected[i], projected[j]])
    edge = np.asarray(edge)
    for e in edge:
        ax.plot(e[:, 0], e[:, 1], e[:, 2], c='b')
    ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2], c='b', marker='o')
    plt.pause(1e-16)
