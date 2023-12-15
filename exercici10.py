#Definició de la funció
def major(a):
    if x>18: #Si es major de 18 es major d'edat
        print("És major d'edat")
    elif x<18: #Si no es major de 18 es menor d'edat
        print("És menor d'edat")
    else: #Si no es cap dels 2 casos anteriors, es perquè té 18
        print("Té 18 anys") 

#Programa principal
x = int(input("Introdueix la teva edat: ")) #Introduir un número (int)
major(x) #fer el procés d'identificar si es major d'edat o no a la variable 'x'