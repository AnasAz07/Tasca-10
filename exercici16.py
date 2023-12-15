# Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas 
# contrari retorni fals.

def detectar_vocals(a): # Definir la funció
    l = ('a', 'e', 'i', 'o', 'u') #id de les vocals
    d = a.lower() # Per dir que estiguin en minuscules
    if d in l: # Si les vocals són minúscules:
        print("És Vocal")
    else:
        print("No és vocal")

a = input("Introdueix un caràcter: ") # Introduir la cadena de caràcters
b = detectar_vocals(a) # Cridar la funció