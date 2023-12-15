def llegir_llista(): #Definició de la funció
    a = 'l'
    l = [] # Fer que la variable 'l' sigui una llista
    while a!= '.': # Bucle per dir que mentre no posis un . en la llista no s'aturarà la introducció d'elements
        a = input("Introduce la lista, para terminarla mete un . : ") #Introduir la llista
        if a!= '.': # Quan posis un . s'aturarà la introduccó d'elements
            l.append(int(a))
        else:
            return l # Mentre posis un element et demanarà introduir més elements

def sumar_llista(l): #definició de sumar una llista
    s = 0 #Començar la variable a 0
    for e in l: # Fer un bucle (recorrer cada element per anar sumant cada un)
        s += e #El 0 amb el que començava la operació sigui el resultat de la suma
    print("El resultat de la suma és {}".format(s)) #Retorna el resultat

def multiplicar_llista(l): #Definició de multiplicar els elements de una llista
    m = 1 #Començam l'operació amb un 1 perquè si multipliques per 0 dona 0
    for e in l: #recorrer cada element per anar multiplicant cada un
        m *= e #L'1 amb el que començava l'operació sigui el resultat
    print("El resultat de la multiplicació és {}".format(m)) #Retorna el resultat


#Programa Principal, Cridar les funcions
l = llegir_llista()
sumar_llista(l)
multiplicar_llista(l)
