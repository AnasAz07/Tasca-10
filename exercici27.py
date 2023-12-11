def contar_majuscules(s):
    num_majuscules = 0
    num_minuscules = 0
    for e in s:
        if e.isupper():
            num_majuscules += 1
        elif e.lower():
            num_minuscules += 1
        else:
            print("")
    
    return (num_majuscules,num_minuscules)

s = input("Introdueix una cadena de caràcters: ")
resultat = contar_majuscules(s)
print("La cadena de caràcters té {} lletres majúscules i minuscules".format(resultat))