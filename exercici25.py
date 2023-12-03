def paraula_mes_llarga(lista_paraules):
    if not lista_paraules:
        return None

    paraula_mes_llarga = lista_paraules[0]
    for paraula in lista_paraules:
        if len(paraula) > len(paraula_mes_llarga):
            paraula_mes_llarga = paraula

    return paraula_mes_llarga

input_paraules = input("Introdueix les paraules separades per espais: ")

paraules = input_paraules.split()

resultat = paraula_mes_llarga(paraules)

if resultat is not None:
    print("La paraula més llarga és:", resultat)
else:
    print("La llista està buida")