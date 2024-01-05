# creando una contraseña aleatoria:
# 
# necesitamos datos random en listas de donde sacaremos los caracteres para nuestra contraseña
# importaremos asi la funcion random
# creamos variables que contenga los datos de las listas, para luego randomizarlos
# indicaremos mediante una funcion de repeticion la cantdad de caracteres a utilizar para la contraseña
# almacenamos dichos caracteres en una nueva variable final, que sera la contraseña creada
# imprimiremos por pantalla dicha contraseña

import random

def generate_password():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    mayus = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    minus = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    simbols = ["#","$","&","-","%","?"]
    
    mixedcharacters = numbers + mayus + minus + simbols
    password = []

    for i in range (10):
        random_characters = random.choice(mixedcharacters)
        password.append(random_characters)                      # agregamos los datos recien randomizados a una lista vacia password con el metodo ".append()"
    password = ''.join(password)                                # la variable password se escribira toda por separado a menos que utilicemos el metodo ".join()"
    return password
    
def run():
    password = generate_password()
    print("Your new safe password is: " + password)


if __name__ == '__main__':
    run() 




