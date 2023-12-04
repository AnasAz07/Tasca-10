def llegir_llista_i_mes_gran():
    a = 'l'
    l = []
    while a!= '.':
        a = input("Introduce la lista, para terminarla mete un . : ")
        if a!= '.':
            l.append(int(a))
           
    if l: 
        return max(l)
    else:
        return None 

resultat = llegir_llista_i_mes_gran()

print("El número més gran de la llista és {}".format(resultat))