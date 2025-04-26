def pot(a, n):
    if n > 1:
        return a*pot(a, n-1)
    if n == 0:
        return 1
    else:
        return a









if __name__ == '__main__':
    a = 10
    n = 200
    print(pot(a, n))