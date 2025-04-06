alfabet = []
import random
alfabet = [chr(i) for i in range (ord('a'), ord('z')+1)] + list ( " ,ąćęłńóżź")
random.shuffle (alfabet)

import math
def szyfruj(napis, klucz):
    k = len (klucz)
    w = math.ceil(len(napis))/len(klucz)
    rozmiar = k * w
    wiadomosc = napis + '_' * (rozmiar - len(napis))
    print (wiadomosc)
def odszyfruj(napis, klucz):
    pass


if __name__ == '__main__':
    napis = "Ala ma kota"
    klucz = "pies"


    zaszyfrowany_napis = szyfruj(napis, klucz)
    print (zaszyfrowany_napis)
    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    print (odszyfrowany_napis)
