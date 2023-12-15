def menu_principal(): #El Menú principal de la calculadora
    print("""
          Menú Principal:
          1. Calculadora de Nombres Enters
          2. Calculadora de Nombres Reals
          3. Sortir
    
    """)
    a = int(input("Elegeix una opció: ")) #Per elegir a quina calculadora vols anar
    return a # Entres a la calculadora seleccionada

def calculadora_enters (): # La calculadora de nombres enters
    print("Hem passat per la calculadora d'enters")
    
    op = 1 # Per iniciar el bucle, el valor d' op ha der ser major de 0
    while op>0: # Inici del bucle
        print("""
              1. Sumar
              2. Restar
              3. Multiplicar   
              4. Dividir
              5. Sortir
        """)  # Les calculadores a seleccionar
        op = int(input("Elegeix una opció: ")) # Hi ha que posar el nombre que te asignat la calculadora per seleccionar-la
        match op: # Per que aparegui el tipus d'operació segons l'opció elegida anteriorment
            case 1: # Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: # Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: # Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: # Dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: # Sortir
                print("Ara tornaràs a la calculadora inicial \n\n")
                op = -1 #Per tornar enrere si li dones a 'Sortir'

def calculadora_reals(): #Programa de la calculadora de nombres reals
    print("Hem passat per la calculadora de reals")

    op = 1 #Per iniciar el bucle
    while op>0: #Bucle
        print("""
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = float(input("Elegeix una opció: "))
        match op: #La operació que farás segons l'opció seleccionada anteriorment
            case 1: # Sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: # Restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: # Multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: # Dividir
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: # Sortir
                print("Ara tornaràs a la calculadora inicial \n\n")
                op = -1 #Tornar enrere a la calculadora inicial

#Programa Principal

a = 1 #Per iniciar el bucle del menú principal
while a>0: # Bucle
    a = menu_principal()
    match a: 
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            a = -1 #Per sortir del programa de la calculadora
        case other:
            print("Opció no vàlida") #Quan poses un nombre que no està entre les opcions