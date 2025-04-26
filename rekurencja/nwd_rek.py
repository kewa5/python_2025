def nwd_r(a, b):
    while a!=b:
        if a > b:
            return nwd_r (a-b, b)
        else:
            return nwd_r (a, b-a)
    return a

def nwd_modulo (a, b):
    if a != 0:
        return nwd_modulo(b % a, a)
    return b




if __name__ == '__main__':
    a = 48
    b = 36
    print(nwd_modulo (a, b))