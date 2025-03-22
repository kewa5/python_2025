
def sito(n):
    dane = [True] * (n+1)
    dane[0]= dane [1] = False
    for i in range (2, int(n**0.5)+1):
       if dane[i] == True:
        for j in range (i**2, n+1, i):
            dane[j] = False
    wynik = []
    for i in range (n+1):
        if dane[i] == True:
            wynik += [i]
    return wynik

if __name__ == '__main__':
    pierwsze = sito(230)
    print (pierwsze)
