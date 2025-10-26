dane = [3, 7,9, 12, 19, 30, 41, 56]

def brute_force(dane, szukane):
    for i in range(len(dane)):
        if dane[i] == szukane:
            return i
    return None

def binary_search(dane, szukana):
    pozycja_min = 0
    pozycja_max = len(dane) - 1
    while pozycja_max - pozycja_min > 1:
        pozycja_srodkowa = pozycja_min + (pozycja_max - pozycja_min) // 2
        wartosc_srodkowa = dane[pozycja_srodkowa]
        if wartosc_srodkowa == szukana:
            return pozycja_srodkowa
        elif wartosc_srodkowa > szukana:
            pozycja_max = pozycja_srodkowa
        else: # wartosc_srodkowa > szukana
            pozycja_min = pozycja_srodkowa


if __name__ == '__main__':

 #   print(brute_force(dane, 12))
     print(binary_search(dane, 12))