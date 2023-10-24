#Definició de la funció
def major(a):
    if x>18:
        print("És major d'edat")
    elif x<18:
        print("És menor d'edat")
    else:
        print("Té 18 anys")

#Programa principal
x = int(input("Introdueix la teva edat: "))
major(x)
