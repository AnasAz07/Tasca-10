def contar_digits(num):
    if num < 1 or num > 900000:
        print("El número ha d'estar entre 1 i 900000.")
        return

    num_digits = len(str(num))
    print("El número {} té {} dígits".format(num,num_digits))

def programa():
    while True:
        try:
            num = int(input("Introdueix un número (entre 1 i 900000): "))
            if 1 <= num <= 900000:
                break
            else:
                print("El número ha d'estar entre 1 i 900000. Torna-ho a intentar.")
        except ValueError:
            print("Entrada invàlida. Si us plau, introdueix un número vàlid.")

    contar_digits(num)

programa()
