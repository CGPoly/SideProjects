#diese Funktion sucht in einer Liste oder in einem Satz nach Palindromen
#Palindrome sind Wörter, die sich in beide Richtungen gleich lesen lassen
#die Liste/der Satz ist variierbar
#das ist jetzt die Funktion:

def ist_Palindrom(Wort):
    x = len(Wort)
    l = -1
    liste = []
    for i in range(x):
        liste.append(Wort[l])
        l = l-1
    y = "".join(liste)
    if y == Wort:
        return True
    else:
        return False
#das ist jetzt der Satz/die Liste:

Worte = """anna und otto und bob haben ein kajak als reittier und fahren mit dem rentner 
        durch die ebbe und treffen sich an der esse zur ehe um ihre neffen zu nennen und
        mit rotor und radar ganz rar einen reliefpfeiler zu treffen und mit einem dlrg retter 
        zu sprechen doch wow am ende der tat sind sie tot""".split()

#der ist jetzt der Aufruf der Funktion

for Wort in Worte:
    if ist_Palindrom(Wort):
        print(Wort)
