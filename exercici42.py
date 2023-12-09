def imprimir_taula_multiplicacio(num):
    if num < 1 or num > 20:
        print("El número ha d'estar entre 1 i 20.")
        return

    print("Taula de multiplicar del {}:".format(num))
    for i in range(1, 11):
        resultat = num * i
        print("{} x {} = {}".format(num,i,resultat))

def programa():
    while True:
        try:
            num = int(input("Introdueix un número (entre 1 i 20): "))
            if 1 <= num <= 20:
                break
            else:
                print("El número ha d'estar entre 1 i 20.")
        except ValueError:
            print("Entrada invàlida")

    imprimir_taula_multiplicacio(num)

programa()