
weeks = int(input("weeks: "))
days = int(input("days: "))
hours = int(input("hours: "))
minutes = int(input("minutes: "))
seconds = int(input("seconds: "))


daysCalc = weeks*7 + days
hoursCalc = daysCalc*24 + hours
minutesCalc = hoursCalc*60 + minutes
secondsCalc = minutes*60 + seconds
print(secondsCalc)
