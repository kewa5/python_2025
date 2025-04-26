def nwd(a, b):
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

if __name__ == '__main__':
    a=24
    b=36
    print(nwd(a, b))
