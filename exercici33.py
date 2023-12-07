def comptar_vocals(paraula):
    vocals = "a" "e" "i" "o" "u"
    comptador = {vocal: 0 for vocal in vocals}

    for lletra in paraula:
        lletra_min = lletra.lower()
        if lletra_min in vocals:
            comptador[lletra_min] += 1

    return comptador

paraula = input("Introdueix una paraula: ")
resultat = comptar_vocals(paraula)

for vocal, compt in resultat.items():
    print("{}: {}".format(vocal,compt))