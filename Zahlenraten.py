#denkt sich eine Zahl aus und lässt dich sie erraten.
#viel zu groß/klein heißt abstand > 20
from random import randint

geraten = False
meine_zahl = randint(1, 100)

while not geraten:
    try:
        zahl = int(input("Gib mir eine  Zahl zwischen 1 und 100!"))
    except ValueError:
        print("Das ist keine Zahl!")
        continue
    if zahl > meine_zahl+20:
        print("{} ist viel zu groß".format(zahl))
    elif zahl < meine_zahl-20:
        print("{} ist viel zu klein".format(zahl))
    elif zahl > meine_zahl:
        print("{} ist zu groß".format(zahl))
    elif zahl < meine_zahl:
        print("{} ist zu klein".format(zahl))
    else:
        geraten = True

print("Herzlichen Glückwunsch, {} ist richig!".format(zahl))
