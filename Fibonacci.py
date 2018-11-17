#Diese Funktion berechnet das Ergebnis der ersten N zahlen.
#sollte z.B. N = 4 sein würde sie 1+2+3+4 = 10 rechenen
N = int(input("Nenne eine Zahl, die benutzt werden soll"))
def Summe(N):
    x = 0
    for i in range(N):
        x = x+i+1
    print(x)
Summe(N)
