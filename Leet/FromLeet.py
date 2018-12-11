text = input("What do you want to understand?")
text = list(text)

i = 0
finished = False
textOut = ""
while i < len(text):
    finished = False
    accText = text[i]
    try:
        accText2 = text[i] + text[i+1]
        if accText2 == "|)":
            textOut += "D"
            i = i + 1
            finished = True
        elif accText2 == "|²":
            textOut += "F"
            i = i + 1
            finished = True
        elif accText2 == "_|":
            textOut += "J"
            i = i + 1
            finished = True
        elif accText2 == "|<":
            textOut += "K"
            i = i + 1
            finished = True
        elif accText2 == "|_":
            textOut += "L"
            i = i + 1
            finished = True
        elif accText2 == "^^":
            textOut += "M"
            i = i + 1
            finished = True
        elif accText2 == "0,":
            textOut += "Q"
            i = i + 1
            finished = True
        elif accText2 == "1²":
            textOut += "R"
            i = i + 1
            finished = True
        elif accText2 == "\‘":
            textOut += "V"
            i = i + 1
            finished = True
        elif accText2 == "uj":
            textOut += "W"
            i = i + 1
            finished = True
        elif accText2 == "}{":
            textOut += "X"
            i = i + 1
            finished = True
        elif accText2 == "‘/":
            textOut += "Y"
            i = i + 1
            finished = True
    except IndexError:
        pass
    if not finished:
        if accText == "4":
            textOut += "A"
        elif accText == "8":
            textOut += "B"
        elif accText == "(":
            textOut += "C"
        elif accText == "3":
            textOut += "E"
        elif accText == "6":
            textOut += "G"
        elif accText == "#":
            textOut += "H"
        elif accText == "1":
            textOut += "I"
        elif accText == "2":
            textOut += "N"
        elif accText == "0":
            textOut += "O"
        elif accText == "9":
            textOut += "P"
        elif accText == "5":
            textOut += "S"
        elif accText == "7":
            textOut += "T"
        elif accText == "v":
            textOut += "U"
        elif accText == "z":
            textOut += "Z"
        elif accText == " ":
            textOut += " "
    i = i + 1


print(textOut)
