def llegir_llista():
    a = 'l'
    l = []
    while a!= '.':
        a = input("Introduce la lista, para terminarla mete un . : ")
        if a!= '.':
            l.append(int(a))
        else:
            return l

def sumar_llista(l):
    s = 0
    for e in l:
        s += e
    print("El resultat de la suma és {}".format(s))

def multiplicar_llista(l):
    m = 1
    for e in l:
        m *= e
    print("El resultat de la multiplicació és {}".format(m))


#Programa Principal
l = llegir_llista()
sumar_llista(l)
multiplicar_llista(l)
