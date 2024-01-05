# PRECONCEPTOS
#
# La computadora generara un nro random del 1 al 100
# El usuario ingresara un nro del 1 al 100
# El numero de intentos posibles sera 5
# Se busca la coincidencia de ambos numeros.
    # En caso de coincidir - jugador gana
    # Caso contrario - La computadora dara una pista:
        # Imprimir numero mas grande
        # imprimir numero mas chico
        # se resta un intento
        # Se vuelve al paso 4
    # si los intentos llegasen a 0 - jugador pierde
# fin
#
# VARIABLES:
# nro_random 
# input(usuario)
# nro intentos
# funcion loop que compare variables
# agregar nro de intentos con contador (4 intentos y que vaya bajando)

import random
from tkinter.messagebox import YES

def run():
    print("""¡Bienvenidx! 
Tendrás 5 intentos para adivinar el número. ¿Listx?""")

    nroRandom = random.randint(1, 50)
    numeroElegido = int(input("Pensa un número del 1 al 50: "))
    intentos = 5

    while numeroElegido != nroRandom:
        if numeroElegido < nroRandom:
            print ("Busca un número más grande")
        else:
            print ("Busca un número más chico")
        numeroElegido = int(input("Pensa otro número: "))
        intentos -= 1
        if intentos == 2:
            print("¡¡¡Te queda una única chance!!!")
        if intentos == 1:
            print ("¡Has perdido!")
            break

    if numeroElegido == nroRandom:
        print("¡Ganaste!")
    else:    
        print("Juego terminado")

if __name__ == "__main__":
    run()



