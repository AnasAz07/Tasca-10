def sumar_digits(num):
    suma = sum(int(digit) for digit in str(num))
    return suma

def parell_o_scenar(num):
    if num % 2 == 0:
        return "parell"
    else:
        return "scenar"

def programa():
    while True:
        try:
            num = int(input("Introdueix un número: "))
            break
        except ValueError:
            print("Entrada invàlida")

    suma = sumar_digits(num)
    resultat = parell_o_scenar(suma)

    print("La suma dels dígits de {} és {} i és {}.".format(num,suma,resultat))

programa()
