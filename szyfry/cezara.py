alfabet = []


alfabet = [chr(i) for i in range (ord('a'), ord('z')+1)]

def szyfruj(napis, klucz):
   szyfr = [alfabet[(i+ klucz) % len (alfabet)] for i in range (len(alfabet))]
   wynik = ''
   for znak in napis:
       if ord ('a') <= ord (znak) <= ord ('z'):    # zamiast znak.islower()
           indeks = ord (znak) - ord ('a')
           zaszyfrowany_znak = szyfr [ indeks]
           wynik += zaszyfrowany_znak

       else:
           wynik += znak
   return wynik

   print(szyfr)
def odszyfruj(napis, klucz):
    pass


if __name__ == '__main__':
    napis = "Ala ma kota, żabę i psa"
    klucz = 11


    zaszyfrowany_napis = szyfruj(napis, klucz)
    print (zaszyfrowany_napis)
    odszyfrowany_napis = odszyfruj(napis, klucz)
    print (odszyfrowany_napis)


