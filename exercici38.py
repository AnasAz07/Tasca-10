def calcular_valor_futur(capital_inicial, interes, anys):
    return capital_inicial * (1 + interes / 100) ** anys

def programa_principal():
    # Solicitar la quantitat a sol·licitar
    while True:
        try:
            capital_inicial = float(input("Introdueix la quantitat a sol·licitar (entre 50000€ i 800000€): "))
            if 50000 <= capital_inicial <= 800000:
                break
            else:
                print("Quantitat fora del rang permès. Torna-ho a intentar.")
        except ValueError:
            print("Entrada invàlida. Si us plau, introdueix un nombre vàlid.")

    # Sol·licitar els interessos
    while True:
        try:
            interes = float(input("Introdueix l'interès (entre 0.5% i 13%): "))
            if 0.5 <= interes <= 13:
                break
            else:
                print("Interès fora del rang permès. Torna-ho a intentar.")
        except ValueError:
            print("Entrada invàlida. Si us plau, introdueix un nombre vàlid.")

    # Sol·licitar el número d'anys
    while True:
        try:
            anys = int(input("Introdueix el nombre d'anys (entre 3 i 40): "))
            if 3 <= anys <= 40:
                break
            else:
                print("Nombre d'anys fora del rang permès. Torna-ho a intentar.")
        except ValueError:
            print("Entrada invàlida. Si us plau, introdueix un nombre vàlid.")

    # Calcular el valor futur
    c_final = calcular_valor_futur(capital_inicial, interes, anys)

    # Mostrar el resultat
    print("\nEl valor futur del capital serà: {:.2f}€".format(c_final))

programa_principal()