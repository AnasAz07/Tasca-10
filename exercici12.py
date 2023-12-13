def menu_principal(): #El Menú principal de la calculadora
    print("""
          Menú Principal:
          1. Calculadora de Nombres Enters
          2. Calculadora de Nombres Reals
          3. Canvi de Base
          4. Sortir
    
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
        """) # Les calculadores a seleccionar
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
                print("{} / {} = {}".format(x, y, x//y))
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
        op = float(input("Elegeix una opció: ")) #El float es per als nombres reals (amb decimals)
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
                print("{} // {} = {}".format(x, y, x/y))
            case 5: # Sortir
                print("Ara tornaràs a la calculadora inicial \n\n")
                op = -1 #Tornar enrere a la calculadora inicial

def canvi_base():
    print("Hem passat per canvi de base")
    op = 1 # Per activar el bucle 
    while op>0: #Bucle
        print("""
              Menú canvi de base
              1. Donat un binari ho passem a tota la resta
              2. Donat un octal ho passem a tota la resta
              3. Donat un decimal ho passem a tota la resta
              4. Donat un hexadecimal ho passem a tota la resta
              5. Sortir
        """)
        op = int(input("Elegeix una opció: ")) #Per elegir el canvi de base que vols fer
        match op: #Els casos segons la opció elegida
            case 1: # Binari to
                b = input("Introdueix el número binari: ")
                o = bin_to_oct(b)
                d = bin_to_dec(b)
                h = bin_to_hex(b)
                print("El número binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            case 2: # Octal to
                o = input("Introdueix el nombre octal: ")
                b = oct_to_bin(o)
                d = oct_to_dec(o)
                h = oct_to_hex(o)
                print("El número binari {} és: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            case 3: # Decimal to
                d = input("Introdueix el nombre decimal: ")
                b = dec_to_bin(d)
                o = dec_to_oct(d)
                h = dec_to_hex(d)
                print("El número binari {} és: \n bin -> {} \n oct -> {} \n hex -> {}".format(d,b,o,h))
            case 4: # Hexadecimal to
                h = input("Introdueix el nombre hexadecimal: ")
                b = hex_to_bin(h)
                o = hex_to_oct(h)
                d = hex_to_dec(h)
                print("El número binari {} és: \n bin -> {} \n oct -> {} \n dec -> {}".format(h,b,o,d))
            case 5: # Sortir
                print("Ara tornaràs al menu principal de canvi de base")
                op = -1 #Sortir de la calculadora de canvis de base

# Definicions Binari to

def bin_to_oct(binary_num):
    decimal_num = int(binary_num, 2) #Començant el calcul amb nombre decimal, el converteix a binari
    octal_num = oct(decimal_num) # Passar el nobre decimal convertit en binari a octal
    return octal_num[2:] #Retorna el nombre octal, i la llista lleva dos lletres que surten a la vora del resultat

def bin_to_dec(binary_num):
    decimal_num = int(binary_num, 2) #Començant el calcul amb nombre decimal, el converteix a binari
    return decimal_num[2:] #Retorna el nombre decimal llevant les lletres que surten a la vora del resultat 

def bin_to_hex(binary_num):
    decimal_num = int(binary_num, 2) #Començant el calcul amb nombre decimal, el converteix a binari
    hex_num = hex(decimal_num) # Passar el nobre decimal convertit en binari a hexadecimal
    return hex_num[2:] #Retorna el nombre hexadecimal, la llista sempre amb la mateixa funció

# Definicions Octal to

def oct_to_bin(octal_num):
    decimal_num = int(octal_num, 8) #Començant el calcul amb nombre decimal, el converteix a octal
    binary_num = bin(decimal_num) # Passar el nobre decimal convertit en octal a binari
    return binary_num[2:] # Retorna el nobre binari

def oct_to_dec(octal_num):
    decimal_num = int(octal_num, 8) #Començant el calcul amb nombre decimal, el converteix a octal
    return decimal_num[2:] # Retorna el nombre decimal

def oct_to_hex(octal_num):
    decimal_num = int(octal_num, 8) #Començant el calcul amb nombre decimal, el converteix a octal
    hex_num = hex(decimal_num) #Passar el nombre decimal convertit en octal a hexadecimal
    return hex_num[2:] # Retorna al nombre hexadecimal

# Definicions Decimal to

def dec_to_bin(decimal_num):
    binary_num = bin(int(decimal_num)) # Passa el nombre decimal a binari
    return binary_num[2:] # Retorna el nombre binari

def dec_to_oct(decimal_num):
    octal_num = oct(int(decimal_num)) # Passa el decimal a octal
    return octal_num[2:] # Retorna el nombre octal

def dec_to_hex(decimal_num):
    hex_num = hex(int(decimal_num)) # Decimal a Hexadecimal
    return hex_num[2:] # Retorna el nombre hexadecimal

# Definicions Hexadecimal to

def hex_to_bin(hex_num):
    decimal_num = int(hex_num, 16) # Començant el calcul amb nombre decimal, el converteix a hexadecimal
    binary_num = bin(decimal_num) # Converteix el nombre hexadecimal a binari
    return binary_num[2:] # Retorna el nombre binari

def hex_to_oct(hex_num):
    decimal_num = int(hex_num, 16) # Començant el calcul amb nombre decimal, el converteix a hexadecimal
    octal_num = oct(decimal_num) # passa el nombre hexadecimal a octal
    return octal_num[2:] #Retorna el nombre octal

def hex_to_dec(hex_num):
    decimal_num = int(hex_num, 16) # Nombre hexadecimal
    return decimal_num[2:] # Retorna el nombre decimal

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
            canvi_base()
        case 4:
            a = -1 #Per sortir del programa de la calculadora
        case other:
            print("Opció no vàlida") #Quan poses un nombre que no està entre les opcions
