def suma_cuadrats(num):
    if num >= 100:
        print("El número ha de ser menor que 100.")
        return

    suma = sum(i**2 for i in range(num, 0, -4))
    print("La suma dels quadrats dels números separats per quatre posicions és {}".format(suma))

def main():
    while True:
        try:
            num = int(input("Introdueix un número menor que 100: "))
            if num < 100:
                break
            else:
                print("El número ha de ser menor que 100. Torna-ho a intentar.")
        except ValueError:
            print("Entrada invàlida. Si us plau, introdueix un número vàlid.")

    suma_cuadrats(num)

main()
