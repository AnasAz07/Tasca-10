def contar_majuscules(s):
    num_maj = 0
    num_menor = 0
    for e in s:
        if e.isupper():
            num_maj += 1
        elif e.lower():
            num_menor += 1
    
    return num_maj

s = input("Introdueix una cadena de caràcters: ")
resultat = contar_majuscules(s)
print("La cadena de caràcters té {} lletres majúscules".format(resultat))