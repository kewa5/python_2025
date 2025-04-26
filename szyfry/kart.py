def odkoduj(tekst, alfabet):
    n = len(alfabet)
    for klucz in range(n):
        odszyfrowany = []
        for znak in tekst.lower():
            if znak in alfabet:
                nr = (alfabet.index(znak) - klucz) % n
                odszyfrowany.append(alfabet[nr])
            else:
                odszyfrowany.append(znak)
        print(f"Klucz {klucz}: {''.join(odszyfrowany)}")

    klucz = 22
    odszyfrowany = []
    for znak in tekst.lower():
        if znak in alfabet:
            nr = (alfabet.index(znak) - klucz) % n
            odszyfrowany.append(alfabet[nr])
        else:
            odszyfrowany.append(znak)
    print(f"odpowiedź: {''.join(odszyfrowany)}")
alfabet = 'aąbcćdeęfghijklłmnopqrsśtuvwxyzźż'
tekst = "eax toćę ksbax khlwex, fhsmws?"

odkoduj(tekst, alfabet)

