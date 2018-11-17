#das ist ein einfacher Taschenrechner, der nach der ersten zahl, der Rechenart und dann nach der #zweiten zahl fragt.
Zahl1 = input("1. Zahl")
Rechenart = input("Rechenart")
Zahl2 = input("2.Zahl")

Ergeb = " ist {}"

Zahl10 = int(Zahl1)
Zahl20 = int(Zahl2)

if Rechenart == "+":
    Ergebniss = Zahl10 + Zahl20
    print("Das Ergebnis von " + Zahl1 + Rechenart + Zahl2 + Ergeb.format(Ergebniss))
elif Rechenart == "/":
    if Zahl20 == 0:
        print("Nicht durch null dividiern")
    else:
        Ergebniss = Zahl10 / Zahl20
        print("Das Ergebnis von " + Zahl1 + Rechenart + Zahl2 + Ergeb.format(Ergebniss))
elif Rechenart == "*":
   Ergebniss = Zahl10 * Zahl20
   print("Das Ergebnis von " + Zahl1 + Rechenart + Zahl2 + Ergeb.format(Ergebniss))
elif Rechenart == "-":
    Ergebniss = Zahl10 - Zahl20
    print("Das Ergebnis von " + Zahl1 + Rechenart + Zahl2 + Ergeb.format(Ergebniss))
else:
    print("Falsche Rechenart")
