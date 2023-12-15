def es_palindrom(a): #Definició de la funció
    a = a.lower() #Per dir que la paraula sigui en minúscula
    return a == a[::-1] #Retorni la paraula minúscula però invertida 
    
b = input("Introdueix una paraula: ") #Introduir la paraula

if es_palindrom(b): #Si la segona meitat de la paraula es invertida és un palíndrom ,i no, no.
    print("Aquesta paraula es un palíndrom")
else:
    print("Aquesta paraula no es un palíndrom")