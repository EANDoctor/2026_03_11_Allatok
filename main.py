from allat import Allat
from emlos import Emlos, Macska, Kutya

allat = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 2, "ház", "közepes")

print(allat)
print(allat2)

print("\nEmlősök\n")

emlos = Emlos("Morzsi", "kutya", 5, "kert", "barna")
emlos2 = Emlos("Cirma", "macska", 3, "lakás", "fekete")

print(emlos)



macska1 = Macska("Hubert", 4, "ház", "fehér")
print(macska1)

kutya1 = Kutya("Rex", 6, "kert", "fekete")
print(kutya1)