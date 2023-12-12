def llegir_llista_paraules():
    paraules = []
    paraula = "a"
    while paraula != ".":
        paraula = input("Introdueixi les paraules que sortiran al index: ")
        if paraula != ".":
            paraules.append(paraula)
    paraules.sort()
    return paraules

def index_paraula(llista, paraula):
    indices = [i for i, e in enumerate(llista) if paraula.lower() == e.lower()]
    return indices[0] if indices else None

# Programa Principal
paraules = llegir_llista_paraules()
paraula_a_cercar = input("Introdueix la paraula a cercar el seu índex: ")
index_trobat = index_paraula(paraules, paraula_a_cercar)

if index_trobat is None:
    print("Dins la llista {} no hi ha l'element {}".format(paraules, paraula_a_cercar))
else:
    print("Dins la llista {}, la paraula {} apareix a la posició {}".format(paraules, paraula_a_cercar, index_trobat))