def szukane_przez_haszowanie(sprawdzany, szukany):

    suma_szuk = 0
    for i in range (len(szukany)):
        suma_szuk += ord ( szukany[i])
    suma = 0
    for i in range (len(szukany)):
        suma += ord ( sprawdzany[i])
    for i in range(len(sprawdzany) - len(szukany) + 1):
        if suma == suma_szuk:
            znaleziono = True
            for j in range(len(szukany)):
                if not sprawdzany[i + j] == szukany[j]:
                    znaleziono = False
                    break
            if znaleziono:
                return i
        suma -=ord(sprawdzany[i])
        suma += ord(sprawdzany[i + len(szukany)])


if __name__ == '__main__':
 sprawdzany = "ala ma koguta, kota i psa"
 szukany = "kota"
 print (szukane_przez_haszowanie(sprawdzany, szukany))