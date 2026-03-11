from allat import *
from emlos import *
from main import *

allatok = []
with open("adatok/allatok.txt", "r", encoding="utf-8") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, faj, eletkor, szorzet_szine = sor.strip().split(",")
        if faj == "kutya":
            allatok.append(Kutya(nev, int(eletkor), "udvar", szorzet_szine))
        elif faj == "macska":
            allatok.append(Macska(nev, int(eletkor), "ház", szorzet_szine))
        elif faj == "madár":
            allatok.append(Madar(nev, int(eletkor)))
        elif faj == "kétéltű":
            allatok.append(Keteltu(nev, int(eletkor)))
        elif faj == "hüllő":
            allatok.append(Hullo(nev, int(eletkor)))

for allat in allatok:
    print(allat)