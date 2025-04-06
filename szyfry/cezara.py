alfabet = []
import random
alfabet = [chr(i) for i in range (ord('a'), ord('z')+1)] + list ( " ,ąćęłńóżź")
random.shuffle (alfabet)
print (alfabet)

def szyfruj(napis, klucz):
   szyfr = [alfabet[(i+ klucz) % len (alfabet)] for i in range (len(alfabet))]
   wynik = ''
   for znak in napis:
       if znak in alfabet:    # zamiast znak.islower()
           indeks = alfabet.index(znak)
           zaszyfrowany_znak = szyfr [ indeks]
           wynik += zaszyfrowany_znak

       else:
           wynik += znak
   return wynik

   print(szyfr)
def odszyfruj(napis, klucz):
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    wynik = ''
    for znak in napis:
        if znak in alfabet:  # zamiast znak.islower()
            indeks = szyfr.index(znak)
            zaszyfrowany_znak = alfabet[indeks]
            wynik += zaszyfrowany_znak

        else:
            wynik += znak
    return wynik

if __name__ == '__main__':
    napis = "Ala ma kota, żabę i psa"
    klucz = 5


    zaszyfrowany_napis = szyfruj(napis, klucz)
    print (zaszyfrowany_napis)
    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    print (odszyfrowany_napis)


