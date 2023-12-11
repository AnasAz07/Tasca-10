import random

def generar_codi():
    return [random.randint(0, 9) for _ in range(4)]

def comprovar_intent(codi, intent):
    correctes = 0
    coincideixen = 0

    for i in range(4):
        if intent[i] == codi[i]:
            correctes += 1
        elif intent[i] in codi:
            coincideixen += 1

    return correctes, coincideixen


#Programa Principal
print("Benvingut a MasterMind!")
print("Intenta endevinar el codi de 4 xifres.")

num_aleatori = generar_codi()
intents = 0

while True:
    intento_usuario = input("Introdueix el teu intent (4 xifres): ")
        
    if len(intento_usuario) != 4 or not intento_usuario.isdigit():
        print("Si us plau, introdueix un intent amb 4 xifres vàlides.")
        continue

    intento_usuario = [int(digit) for digit in intento_usuario]
    correctos, coinciden = comprovar_intent(num_aleatori, intento_usuario)

    print("Encertats: {}, Coincidents: {}".format(correctos, coinciden))

    intents += 1

    if correctos == 4:
        print("Felicitats! Has endevinat el codi en {} intents.".format(intents))
        break