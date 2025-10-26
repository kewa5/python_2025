lista = [2,4,7,9,14,45]

def zmiana_druga(lista):
    for i in range(0,len(lista), 2):
        lista[i] = lista[i]*2
    for i in range(1, len(lista), 2):
        lista[i] = lista[i] / 2
    return lista

if __name__ == '__main__':
    zmiana_druga(lista)
    print (lista)

#T(n)=N  ilość obliczeń
#O(n)=N   złożoność czasowa