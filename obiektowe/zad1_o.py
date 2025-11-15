from math import gcd

class Ulamek:
    def __init__(self,licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def calkowita(self):
        return self.licznik % self.mianownik == 0

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"
    def __float__(self):
        return self.licznik/self.mianownik

    def skroc(self):
        return f"{self.licznik/gcd(self.licznik,self.mianownik)}/{self.mianownik/gcd(self.licznik,self.mianownik)}"


if __name__ == '__main__':

    u = Ulamek(5,15)
    print(u.skroc())
    

