from allat import Allat

class Emlos(Allat):
    def __init__(self, nev_, faj_, eletkor_, elohely_, szorzet_szine):
        super().__init__(nev_, faj_, eletkor_, elohely_, "közepes")
        self.szorzet_szine = szorzet_szine

    def __str__(self):
        return super().__str__() + f", szőrzete: {self.szorzet_szine}"
        # return f"{self.nev} ({self.faj}), {self.eletkor} éves, élőhelye: {self.elohely}, mérete: {self.meret}, szőrzete: {self.szorzet_szine}"

class Macska(Emlos):
    def __init__(self, nev_, eletkor_, elohely_, szorzet_szine):
        super().__init__(nev_, "macska", eletkor_, elohely_, szorzet_szine)

    def dorombol(self):
        print(f"{self.nev} épp dorombol.")

class Kutya(Emlos):
    def __init__(self, nev_, eletkor_, elohely_, szorzet_szine):
        super().__init__(nev_, "kutya", eletkor_, elohely_, szorzet_szine)

    def ugat(self):
        print(f"{self.nev} épp ugat.")