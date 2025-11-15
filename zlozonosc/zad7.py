def silnia(n):
    if n>1:
        return n*silnia(n-1)
    else:
        return 1

if __name__ == '__main__':
    print(silnia(4))

# M(N) = N
# O(N) = N

