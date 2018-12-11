text = input("What do you want to say?").upper()
text = list(text)

for i in range(len(text)):
    accText = text[i]
    if accText == "A":
        text[i] = "4"
    elif accText == "B":
        text[i] = "8"
    elif accText == "C":
        text[i] = "("
    elif accText == "D":
        text[i] = "|)"
    elif accText == "E":
        text[i] = "3"
    elif accText == "F":
        text[i] = "|²"
    elif accText == "G":
        text[i] = "6"
    elif accText == "H":
        text[i] = "#"
    elif accText == "I":
        text[i] = "1"
    elif accText == "J":
        text[i] = "_|"
    elif accText == "K":
        text[i] = "|<"
    elif accText == "L":
        text[i] = "|_"
    elif accText == "M":
        text[i] = "^^"
    elif accText == "N":
        text[i] = "2"
    elif accText == "O":
        text[i] = "0"
    elif accText == "P":
        text[i] = "9"
    elif accText == "Q":
        text[i] = "0,"
    elif accText == "R":
        text[i] = "1²"
    elif accText == "S":
        text[i] = "5"
    elif accText == "T":
        text[i] = "7"
    elif accText == "U":
        text[i] = "v"
    elif accText == "V":
        text[i] = "\‘"
    elif accText == "W":
        text[i] = "uj"
    elif accText == "X":
        text[i] = "}{"
    elif accText == "Y":
        text[i] = "‘/"
    elif accText == "Z":
        text[i] = "z"
    elif accText == " ":
        text[i] = " "

textOut = ""
for i in range(len(text)):
    textOut += text[i]

print(textOut)
