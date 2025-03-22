def wyszukaj_naiwnie2(sprawdzany, szukany):
  for i in range ( len(sprawdzany)-len(szukany)+1):
      znaleziono = True
      for j in range(len(szukany)):
          if not sprawdzany[i + j] == szukany[j]:
              znaleziono = False
              break
      if znaleziono:
          return i

  return " nie ma"



if __name__ == '__main__':
 sprawdzany = "Ala ma kota i psa"
 szukany = "a i p"
 print (wyszukaj_naiwnie2(sprawdzany, szukany))