# Zahlen raten
import random
geheimnis = random.randint(1,99)
tipp = 0
versuche = 6
print("Ahoi, Gebe eine Zahl zwischen 1 und 99 ein. Du hast 6 Versuche")
while tipp != geheimnis and versuche > 0:
    tipp = int(input("Was rätsts Du? "))
    if tipp < geheimnis:
        print("zu niedrig")
    elif tipp > geheimnis:
        print("zu hoch")

    versuche -= 1
    if versuche > 0:
        print("noch ", versuche, "Versuche")

if tipp == geheimnis:
    print("Treffer")
else:
    print("Game Over")
    print("Die Zahl war: ", geheimnis)
        
