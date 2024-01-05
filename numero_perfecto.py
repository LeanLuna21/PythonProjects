# Un numero perfecto es aquel que al sumar todos sus divisores(excepto el nro mismo), nos da el numero dado como resultado. Ej 6 (divisores: 1,2,3) sumados dan 6 como resultado

def buscando_la_perfeccion(num):
    divisores = []
    for i in range(1,num):
        if num%i == 0:
            divisores.append(i)
    print (f"Divisores: {divisores}")
    if sum(divisores) == num:
        return f"El numero {num} ES perfecto"
    else:
        return f"El numero {num} NO ES perfecto"

def ask_for_number():
    try:
        number = int(input("Tirame un numero: "))
    except:
        print("Un numero te dije! Chau.")
        quit()
    else:
        return number
    
print ("Ejemplos: ")
print (buscando_la_perfeccion(6))
print (buscando_la_perfeccion(10))
print (buscando_la_perfeccion(32))
print (buscando_la_perfeccion(28))
print ("--------------------------------")
print ("Para saber si un número es perfecto...")
print (buscando_la_perfeccion(ask_for_number()))
