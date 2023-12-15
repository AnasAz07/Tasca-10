def invertir(cadena): #Definició de la funció
    cadena_invertida = "" #Inicialitzar una cadena buida per a la invertida
    for caracter in cadena: # Recorrer cada caràcter en la cadena introduida
        cadena_invertida = caracter + cadena_invertida 
    return cadena_invertida #Retorna la cadena ja invertida

cadena_original = input("Introdueix una cadena de caràcters: ") #Introduir la cadena

cadena_invertida = invertir(cadena_original) #Cridar la funció per invertir la cadena introduïda

print("La cadena invertida sería així: {}".format(cadena_invertida))
#Retorna la cadena invertida