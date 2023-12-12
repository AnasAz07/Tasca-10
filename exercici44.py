def digits_parells(num):
    digits_parells = [int(digit) for digit in str(num) if int(digit) % 2 == 0]
    return digits_parells

#Programa Principal
while True:
    try:
        num = int(input("Introdueix un número: "))
        break
    except ValueError:
        print("Entrada invàlida")

parells = digits_parells(num)

if parells:
    print("Els dígits parells de {} són: {}".format(num,', '.join(map(str, parells))))
else:
    print("No hi ha dígits parells en {}.".format(num))