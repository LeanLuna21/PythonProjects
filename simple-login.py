# Crea un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
# Creado por: Leandro Luna - Python-Flex/comision 56050 - Preentrega n°1

bbdd = { }

def agregar_usuario(dic):
    new_user = input("Ingrese nuevo usuario: ")
    new_pass = input("Ingrese contraseña: ")
    dic[new_user] = new_pass
    print("¡Usuario creado con éxito!")

def mostrar_data(dic):
    print("Los datos de usuarios almacenados son: ")
    if dic == {}:
       print ("No se encuentran datos registrados.")
    else: 
       for u,p in dic.items():    
         print (f"- {u} {p};")

def login(dic):
    usuario = input("Ingrese su usuario: ")
    if usuario not in dic.keys():
        print("Usuario inexistente")
    else:   
        tries = 0
        while tries < 3: 
            contraseña = input("Ingrese su contraseña: ")
            if dic[usuario] == contraseña:
                print("¡Has iniciado sesion correctamente!")
                break
            else:
                print("Contraseña incorrecta.")
                tries += 1
        if tries == 3:
            print("Ha sobrepasado el máximo de intentos...")
            print("¡Cuenta bloqueada! Por favor, comunicarse con soporte técnico.")

def menu_opciones():
    print("""
        Indique acción a realizar: 

        1. Crear usuario
        2. Leer Base de datos
        3. Log In
        4. Salir
        """)
    
    opcion = input(": ")
    return opcion
    
def decision():
    salir = False
    while salir == False:
        resultado = input("¿Desea realizar otra operacion?: Y or N ").upper()     
        if resultado == "Y":
            salir = True
        elif resultado == "N": 
            salir = False
            print("¡Hasta pronto!")
            break
        else:
            print("Introduzca una opcion valida")
    return salir

def main():
    print("¡Bienvenidx!")
    while True:
        try:          
            opcion = menu_opciones()
            opcion = int(opcion)
        except:
            print("Ingrese un número valido")
        else:
            if opcion not in [1,2,3,4]:
                print("Seleccione un número de opción válida")
            else:
                if opcion == 1:
                    agregar_usuario(bbdd)
                    if decision() == False:
                        break
                elif opcion == 2:
                    mostrar_data(bbdd)
                    if decision() == False:
                        break
                elif opcion == 3:
                     login(bbdd)
                     break
                else:
                    print("¡Hasta pronto!")
                    break

main()