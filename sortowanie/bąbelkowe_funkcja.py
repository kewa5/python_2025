def sortuj_przez_babelkowe (dane):
    n = len (dane)
    licznik_z = 0
    licznik_p = 0
    for i in range (0, n-1):
        for j in range(0, n-1-i):
            if dane[j] > dane [j+1]:
                 dane[j],dane[j+1] = dane[j + 1],dane[j]
                 licznik_z = licznik_z + 1
            licznik_p = licznik_p + 1
        print (dane)
    print (licznik_z)
    print (licznik_p)