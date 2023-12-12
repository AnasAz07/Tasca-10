def esta_ordenada(a):
    ascendente = sorted(a) == a
    descendente = sorted(a, reverse = True) == a

    if ascendente:
        print("La llista {} està ordenada ascendentment".format(a))
    elif descendente:
        print("La llista {} està ordenada descendentment".format(a))
    else:
        print("La llista {} no està ordenada".format(a))

def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            # Convertir a número
            a.append(int(c))
    return a

# Programa Principal
a = llegir_llista()
esta_ordenada(a)