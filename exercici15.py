# Definir una funció que calculi la longitud d’una llista o d’una cadena donada.

def contar_caràcters(element): # Definició de la funció
    return len(str(element)) # Rotrni longitud de la cadena de caràcters

a = input("Introdueix una llista o cadena de caràcters: ") # Introduir la cadena
b = contar_caràcters(a) # Cridar la funció

print("La llista o cadena de caràcters té {} caràcters".format(b))
#Retorna el nombre de caràcters