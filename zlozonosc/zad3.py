lista = [2,4,7,9,14,45]

def ktore_liczby(lista, suma):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[i]+lista[j+i+1] == suma:
                return i, i+j+1
    return None

if __name__ == '__main__':

    print (ktore_liczby(lista, 60))

#T(n)=(N-1)(N-2)/2
#O(n)=N^2