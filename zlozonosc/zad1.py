lista = [2,4,7,9,14,45]

def przemnozenie(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2
    return lista

if __name__ == '__main__':
    przemnozenie(lista)
    print (lista)

#T(n)=n
#O(n)=n