# lässt eine Turtle vor dir fliehen, wenn du in ihre Nähe klickst:
from turtle import *
from random import randint

t = Turtle()


def flieh(x, y):
    xt, yt = t.pos()
    xd = xt+yt
    if x+y > xd-21:
        if x+y < xd+21:
            t.goto(randint(-150, 150), randint(-150, 150))
        else:
            t.forward(0)
    else:
        t.forward(0)


while True:
    t.onclick(flieh)
