# findet in einer liste die größte und die kleinste zahl:
# liste variierbar
Zahlen = [41, 25, 40, 97, 76, 40, 43, 10]

Anzahl = len(Zahlen)
k = min(Zahlen)
g = max(Zahlen)

Antwort1 = "Die kleinste Zahl ist {} "
Antwort2 = "und die größte Zahl ist {}."
print(Antwort1.format(k) + Antwort2.format(g))
