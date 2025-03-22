dane = [2, 5, 7, 9, 1, 4, 2]
n = len (dane)
licznik = 0
for i in range (0, n-1):
    for j in range(0, n-1-i):
        if dane[j] > dane [j+1]:
             dane[j],dane[j+1] = dane[j + 1],dane[j]
             licznik = licznik + 1
    print(dane)
print (dane)
print (licznik)
