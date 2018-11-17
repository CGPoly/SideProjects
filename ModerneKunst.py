# zeichnet mit einer sich zufällig bewegenden Turtle moderne Kunst:
from turtle import *
from random import randint

t = Turtle()
x = 1


for e in range(randint(1, 10)):
    for i in range(randint(10, 40)):
        t.forward(randint(10, 100))
        i = randint(1, 2)
        if i == 1:
            t.right(randint(10, 170))
        else:
            t.left(randint(10, 170))
    t.up()
    t.goto(0,0)
    t.down()
    print(x)
    x = x+1
t.up()
t.goto(300, 300)
print('fertig')
