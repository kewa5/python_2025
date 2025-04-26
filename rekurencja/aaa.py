def wyswietl(liczba):

    if liczba >= 1:

        wyswietl(liczba - 1)
    print(liczba)





if __name__ == '__main__':
    wyswietl(10)