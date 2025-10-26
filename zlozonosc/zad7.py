def silnia(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        wynik = n
        for i in range(n-1):
            wynik = wynik*(n-i-1)
        return wynik

if __name__ == '__main__':
    print(silnia(1))

# T(kl)=
# O(kl)=