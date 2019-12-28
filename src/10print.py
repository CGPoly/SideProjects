import random
# import turtle
import matplotlib.pyplot as plt


# def pretty_turtle(length: int, size=10):
#     turtle.setworldcoordinates(-1, -1, length*size, length*size)
#     t = turtle.Turtle()
#     t.speed(0)
#     t.ht()
#     for x in range(length):
#         for y in range(length):
#             dir = random.random() < 0.5
#             t.pu()
#             t.goto(x*size, y*size) if dir else t.goto(x*size, y*size+size)
#             t.pd()
#             t.goto(x*size+size, y*size+size) if dir else t.goto(x*size+size, y*size)
#             # t.lt(90 + (-1 if random.random() < 0.5 else 1)*45)
#             # t.fd(size)

def pretty(ax, length: int, size=10):
    for x in range(length):
        for y in range(length):
            ax.plot([x*size, x*size+size], [y*size, y*size+size], c="black", antialiased=True) if random.random() < 0.5 \
                else plt.plot([x*size, x*size+size], [y*size+size, y*size], c="black", antialiased=True)
            

def short(length):
    [[print(random.choice('/\\'), end="" if i < length else "\n") for i in range(length + 1)] for _ in range(length)]


if __name__ == "__main__":
    length = 50
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    plt.axis('off')
    pretty(ax, length)
    plt.savefig("save.png", bbox_inches=0, dpi=300)
    plt.show()
