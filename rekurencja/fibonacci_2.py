def f(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        fn_1, fn_2  = 1, 0
        for _ in range (2, n+1):
            fn = fn_1 + fn_2
            fn_2, fn_1   = fn_1, fn
        return fn



if __name__ == '__main__':
    n=1000
    print(f(n))