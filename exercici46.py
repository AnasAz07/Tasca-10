def esta_ordenada(a):
    b = a.copy()
    a.sort()
    if a == b:
        print("La llista {} està ordenada {}".format(a, b))
    else:
        print("La llista {} no està ordenada {}".format(a, b))

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
