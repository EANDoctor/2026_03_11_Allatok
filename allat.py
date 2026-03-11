class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = eletkor_
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev} ({self.faj}), {self.eletkor} éves, élőhely: {self.elohely}, méret: {self.meret}"

class Madar(Allat):
    def __init__(self, nev_):
        super().__init__(nev_, "madar", 1, "erdő", "kicsi")

    def csiripel(self):
        print(f"{self.nev} épp csiripel.")

class Keteltu(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "kétéltű", 2, "tópart", "kicsi")