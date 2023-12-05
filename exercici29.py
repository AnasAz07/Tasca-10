def calcular_edat(nom, any_naixement, any_actual):
    edat = any_actual - any_naixement
    print("""
          {}: 
          Any naixement: {}
          Edat: {}
          """.format(nom,any_naixement,edat))

any_actual = int(input("Introdueix l'any actual: "))

for i in range(4):
    nom = input("Introdueix el nom de la persona {}: ".format(i + 1))
    any_naixement = int(input("Introdueix l'any de naixement de {}: ".format(nom)))
    calcular_edat(nom, any_naixement, any_actual)