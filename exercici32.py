def nums_que_comencen_per(llista_noms, lletra):
    comptador = 0
    for nom in llista_noms:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador

llista = input("Introdueix la llista de noms separats per espais: ") 
noms = llista.split()
lletra = input("Introdueix la lletra amb la qual vols comparar: ")

resultat = nums_que_comencen_per(noms, lletra)

print("Número de nombres que comencen amb '{}': {}".format(lletra, resultat))