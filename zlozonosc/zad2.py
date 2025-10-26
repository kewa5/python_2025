lista = [2,4,7,9,14,45]

def zmiana(lista):
    for i in range(len(lista)):
        if i%2 == 0:
            lista[i] = lista[i]*2
        else:
            lista[i] = lista[i] / 2
    return lista

if __name__ == '__main__':
    zmiana(lista)
    print (lista)

#T(n)=2N  ilość obliczeń
#O(n)=N