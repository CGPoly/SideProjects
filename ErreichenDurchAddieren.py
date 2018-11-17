#sagt wieviele der ersten natürlichen zahlen man addieren muss um eine Zahl X zu erreichen

X = int(input("Bis zu welcher Zahl soll gegangen werden?"))

Zahl = 0
Summe = 0
N = 0
while Summe < X:
    Zahl = Zahl + 1
    Summe = Summe+Zahl
    N = N + 1
print(N)
