

import math

def indeksy_klucza(klucz):
    posortowany_klucz = sorted(klucz)
    return [posortowany_klucz.index(znak)for znak in klucz]


def szyfruj(napis, klucz):
    k = len(klucz)
    w = math.ceil(len(napis))/len(klucz)
    rozmiar = k * w
    a = rozmiar - len(napis)
    wiadomosc = napis + '_' * a
    kolejnosc = indeksy_klucza(klucz)

    tablica = []
    for wiersz in range (w):
        poczatek = wiersz * len(klucz)
        koniec = (wiersz + 1)* len(klucz)
        linia = wiadomosc[poczatek:koniec]
        zaszyfrowana_linia = ''.join([linia[i] for i in kolejnosc])
        # for i in kolejnosc:
       #     zaszyfrowana_linia.append([i])
        tablica += zaszyfrowana_linia
    return tablica

def odszyfruj(napis, klucz):
    pass


if __name__ == '__main__':
    napis = "Ala ma kota"
    klucz = "pies"


    zaszyfrowany_napis = szyfruj(napis, klucz)
    print (zaszyfrowany_napis)
   # odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    # print (odszyfrowany_napis)
