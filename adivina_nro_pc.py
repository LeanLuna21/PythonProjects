import random

def adivina_nro():
    limite_inferior = 1
    limite_superior = elige_limite()
    print("\n===================")
    print("""¡Bienvenidx!""")
    print("===================\n")
    print(f"La PC intentará adivinar un número del 1 al {limite_superior}.")
    print(f"Piensa el número que desees.")
    opcion = input("\n¿Listo para empezar? ")

    if opcion == "" or opcion:
        run(limite_inferior,limite_superior)

def elige_limite():
    x = int(input("Elige un número limite: "))
    return x


def run(li,ls):
    respuesta = ""
    intentos = 5
    while respuesta != "C" and intentos > 0:
        print("\nIntentos: ", intentos)
        if li != ls:
            prediccion = random.randint(li,ls)
        else:
            prediccion = li
        respuesta = input(f"\nMi respuesta es {prediccion}. ¿Estoy en lo correcto? Elige: \n(A) si el número es mayor, \n(B) si el numero es menor o \n(C) si la respuesta es correcta \n").upper()

        if respuesta == "A":
            li = prediccion +1
        elif respuesta == "B":
            ls = prediccion -1
        
        intentos -= 1
        if intentos == 0:
            print ("La PC a perdido. No ha logrado adivinar tu número.")
        

    if respuesta == "C":
        print(f"\n\n¡La PC gana! Ha adivinado tu numero: {prediccion}.")

if __name__ == "__main__":
    adivina_nro()

