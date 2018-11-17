from turtle import *

tSpiegel = Turtle()


def ausgabe(a, b):
    tSpiegel.goto(a, b)
def spiegel(x, y):
    x1 = x * -1
    y1 = y * -1
    ausgabe(x1, y1)

while True:
    tSpiegel.onclick(spiegel)
