def menu_principal():
    print("""
          Menú Principal:
          1. Calculadora de Nombres Enters
          2. Calculadora de Nombres Reals
          3. Canvi de Base
          4. Sortir
    
    """)
    a = int(input("Elegeix una opció: "))
    return a

def calculadora_enters ():
    print("Hem passat per la calculadora d'enters")
    
    op = 1
    while op>0:
        print("""
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
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
                op = -1

def calculadora_reals():
    print("Hem passat per la calculadora de reals")

    op = 1
    while op>0:
        print("""
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = float(input("Elegeix una opció: "))
        match op:
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
                op = -1
def canvi_base():
    print("Hem passat per canvi de base")
    op = 1
    while op>0:
        print("""
              Menú canvi de base
              1. Donat un binari ho passem a tota la resta
              2. Donat un octal ho passem a tota la resta
              3. Donat un decimal ho passem a tota la resta
              4. Donat un hexadecimal ho passem a tota la resta
              5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
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
                op = -1

# Definicions Binari to

def bin_to_oct(binary_num):
    decimal_num = int(binary_num, 2)
    octal_num = oct(decimal_num)
    return octal_num

def bin_to_dec(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num

def bin_to_hex(binary_num):
    decimal_num = int(binary_num, 2)
    hex_num = hex(decimal_num)
    return hex_num[2:]

# Definicions Octal to

def oct_to_bin(octal_num):
    decimal_num = int(octal_num, 8)
    binary_num = bin(decimal_num)
    return binary_num[2:]

def oct_to_dec(octal_num):
    decimal_num = int(octal_num, 8)
    return decimal_num

def oct_to_hex(octal_num):
    decimal_num = int(octal_num, 8)
    hex_num = hex(decimal_num)
    return hex_num[2:]

# Definicions Decimal to

def dec_to_bin(decimal_num):
    binary_num = bin(int(decimal_num))
    return binary_num[2:]

def dec_to_oct(decimal_num):
    octal_num = oct(int(decimal_num))
    return octal_num[2:]

def dec_to_hex(decimal_num):
    hex_num = hex(int(decimal_num))
    return hex_num[2:]

# Definicions Hexadecimal to

def hex_to_bin(hex_num):
    decimal_num = int(hex_num, 16)
    binary_num = bin(decimal_num)
    return binary_num[2:]

def hex_to_oct(hex_num):
    decimal_num = int(hex_num, 16)
    octal_num = oct(decimal_num)
    return octal_num[2:]

def hex_to_dec(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num

#Programa Principal

a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            canvi_base()
        case 4:
            a = -1
        case other:
            print("Opció no vàlida")
