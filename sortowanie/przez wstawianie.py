dane = [7, 1, 6, 9, 3, 5, 4, 6]
n = len(dane)
for i in range (1,n):
    cz = dane[i]
    for j in range (0, i):
        if cz < dane[j]:
            dane.pop(i)
            dane.insert(j, cz)
            break
print (dane )