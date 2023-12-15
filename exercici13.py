# Definir una funció gran() que, donats dos números, retorni el major.
def gran(x,y): # Definició de la funció
    if x>y:
        print("El nombre més gran és {}".format(x)) # Si el primer nombre introduit es mes gran que el segon retorna x

    elif x<y:
        print("El nombre més gran és {}".format(y)) # Si el segon nombre introduit es mes gran que el primer retorna y

    else:
        print("Els dos nombres són iguals") # En un altre cas retorni que son iguals

x = int(input("Introdueix el primer nombre: ")) #Introduir el primer nombre
y = int(input("Introdueix el segon nombre: ")) #Introduir el segon nombre

gran(x,y) # Cridar la funció