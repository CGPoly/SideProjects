# Kalkuliert durch Zufallszahlen die Temperaturen der nächsten Woche:
from random import randint

Montag = randint(10, 20)

Dienstag = 0
Mittwoch = 0
Donnerstag = 0
Freitag = 0
Samstag = 0
Sonntag = 0

x = randint(1, 2)
if x == 1:
    Dienstag = Montag - 2
else:
    Dienstag = Montag + 2

x = randint(1, 2)
if x == 1:
    Mittwoch = Dienstag - 2
else:
    Mittwoch = Dienstag + 2

x = randint(1, 2)
if x == 1:
    Donnerstag = Mittwoch - 2
else:
    Donnerstag = Mittwoch + 2

x = randint(1, 2)
if x == 1:
    Freitag = Donnerstag - 2
else:
    Freitag = Donnerstag + 2

x = randint(1, 2)
if x == 1:
    Samstag = Freitag - 2
else:
    Samstag = Freitag + 2

x = randint(1, 2)
if x == 1:
    Sonntag = Samstag - 2
else:
    Sonntag = Samstag + 2

t = "Am"
te = "werden es"
tex = " °C."
Tage = [
    'Montag',
    'Dienstag',
    'Mittwoch',
    'Donnerstag',
    'Freitag',
    'Samstag',
    'Sonntag',
]

q = 0
for i in (Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag):
    grad = "{}" + tex
    y = t + " {}" + " " + te
    print(y.format(Tage[q]), grad.format(i))
    q = q + 1
