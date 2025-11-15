from obiektowe.zad1_o import Ulamek

def compare(a,b):
    if a.licznik/a.mianownik > b.licznik/b.mianownik:
        return -1
    elif a.licznik/a.mianownik == b.licznik/b.mianownik:
        return 0
    else:
        return 1

if __name__ == '__main__':

    u = Ulamek(5,10)
    print (u.licznik,u.mianownik)
    print (compare(Ulamek(9,7),Ulamek(1,2)))
