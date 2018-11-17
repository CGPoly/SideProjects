# fragt dich die Hauptstädte zu den Bundesländern von Deutschland ab.
# Ende beendet die Abfragung
# du kannst die Funktion auch mit Vokabeln aufrufen
# das ist erst die Funktion
def Abfrage(d):
    k = list(d.keys())
    v = list(d.values())
    t = False
    n = 0
    while not t:
        x = input("Wie lautet die Hauptstadt von " + k[n] + "?")
        if x == v[n]:
            print("Das ist richtig.")
        elif x == "Ende":
            print("Auf Wiedersehen.")
            t = True
        else:
            print("Das ist leider falsch. Richtige Antwort wäre: " + v[n])
        n = n + 1
        if n == len(d):
            t = True


# hier wird jetzt die Funktion mit dem dictionarie Hauptstädte aufgerufen

Hauptstädte = {
    'Schleswig-Holstein':'Kiel',
    'Hamburg':'Hamburg',
    'Mecklenburg-Vorpommern':'Schwerin',
    'Niedersachsen':'Hannover',
    'Bremen':'Bremen',
    'Sachsen-Anhalt':'Magdeburg',
    'Brandenburg':'Potsdam',
    'Berlin':'Berlin',
    'Nordrhein-Westfalen':'Düsseldorf',
    'Hessen':'Wiesbaden',
    'Thüringen':'Erfurt',
    'Sachsen':'Dresden',
    'Rheinland-Pfalz':'Mainz',
    'Saarland':'Saarbrücken',
    'Baden-Württemberg':'Stuttgart',
    'Bayern':'München'
    }

Abfrage(Hauptstädte)
