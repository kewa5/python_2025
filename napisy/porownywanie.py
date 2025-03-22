"""
Ala ma kota
Ala nie ma kota

ala ma kota
Ala nie ma kota

"""

def napisy (napis1, napis2):
    shortest_len = min(len(napis1),len(napis2))
    for i in range (0, shortest_len):
        if napis1[i]< napis2[i]:
            return -(i+1)
        elif napis1[i] > napis2[i]:
            return (i+1)

    if len(napis1) == len(napis2):
        return 0
    elif len(napis1) < len(napis2):
        return -shortest_len
    else:
        return shortest_len
if __name__ == '__main__':
    napis1 = 'Ala ma kota'
    napis2 = 'Ala ma kotA'
    print (napisy (napis1, napis2))