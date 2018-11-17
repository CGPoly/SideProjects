import numpy as np
from matplotlib import pyplot as plt


def xAxis(pNum):
	return np.sin(1000*pNum)


def yAxis(pNum, phase, deltaP):
	return np.sin(1000*phase*pNum-deltaP)


listX = []
listY = []
steps = 0.025
phase = float(input("a = "))
deltaP = float(input("b = "))

for i in range(500):
	listX.append(xAxis(i*steps))
	listY.append(yAxis(i*steps, phase, deltaP*np.pi))

plt.figure(figsize=(5, 5))
plt.plot(listX, listY)
plt.show()