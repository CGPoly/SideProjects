#bildet den Durchschnitt in einer Liste aus zahlen:
#liste variierbar
Zahlen = [41, 25, 40, 97, 76, 40, 43, 10]
Anzahl = len(Zahlen)
Durchschnitt = 0
for Zahl in Zahlen:
    Durchschnitt = Durchschnitt+Zahl
Durchschnit = Durchschnitt/Anzahl
print(Durchschnit)
