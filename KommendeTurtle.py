from turtle import *


t = Turtle()


def ausgabe(x, y):
    t.goto(x, y)


def main():
    t.onscreenclick(ausgabe)
    # t.mainloop()


while True:
    main()
