def rima(paraula_1, paraula_2):
    if len(paraula_1) < 3 or len(paraula_2) < 3:
        return False  # No poden rimar si tenen menys de 3 lletres

    tres_ultimes_lletres_1 = paraula_1[-3:]
    tres_ultimes_lletres_2 = paraula_2[-3:]
    dues_ultimes_lletres_1 = paraula_1[-2:]
    dues_ultimes_lletres_2 = paraula_2[-2:]

    if tres_ultimes_lletres_1 == tres_ultimes_lletres_2:
        return "Rimen"
    elif dues_ultimes_lletres_1 == dues_ultimes_lletres_2:
        return "Rimen un poc"
    else:
        return "No rimen"

def programa_principal():
    print("Introdueix dues paraules per comprovar si rimen:")
    paraula_1 = input("Paraula 1: ")
    paraula_2 = input("Paraula 2: ")

    resultat = rima(paraula_1, paraula_2)
    print(resultat)

programa_principal()