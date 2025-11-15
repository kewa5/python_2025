from obiektowe.zadaniep import Punkt

class Prostokat:
    def __init__(self, lewy_gorny_wierzcholek, szerokosc, wysokosc):
        self.lewy_gorny_wierzcholek  = lewy_gorny_wierzcholek
        self.szerokosc  = szerokosc
        self.wysokosc = wysokosc

    def pole (self):
        return self.wysokosc *self.szerokosc

if __name__ == '__main__':

    lg = Punkt(5,10)
    print(lg.x,lg.y)
    pr = Prostokat(lg, 20, 3)
    print (pr.pole())