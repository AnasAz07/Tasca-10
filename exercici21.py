def crear_repetits(numero,caracter): #Definició de la funció
    return caracter * numero #Retorna les vegades que vols imprimir el caràcter

numero = int(input("Introdueix un numero: ")) # Introduir les vegades que es produirà el caràcter
caracter = input("Introdueix un caràcter: ") # El caràcter que vols reproduir

resultat = crear_repetits(numero,caracter) # Cridar la funció
print("{}".format(resultat)) # Retorna el caràcter reproduit
