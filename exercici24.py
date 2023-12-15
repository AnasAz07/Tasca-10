def llegir_llista_i_mes_gran(): #Definició de llegir una llista
    a = 'l'
    l = []
    while a!= '.':
        a = input("Introduce la lista, para terminarla mete un . : ")
        if a!= '.':
            l.append(int(a))
           
    if l: #Per reotrnar el nombre més gran de la llista
        return max(l)
    else:
        return None 

resultat = llegir_llista_i_mes_gran() #Asignar la funció en el resultat

print("El número més gran de la llista és {}".format(resultat)) #Retorna el resultat