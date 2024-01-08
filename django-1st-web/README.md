# django_model1
Esta es la 1ra version de la tienda "That's No Moon"
Este es un proyecto de tienda online de Sables Laser de Star Wars.

La tienda esta desarrollada con el framework Django, y esta divida en 2 aplicaciones: Stock(de productos) y Ventas(transacciones realizadas).

Consta de 3 modelos: 
    - El modelo Producto(en la app de stock), que define nombre, medida, color, cantidad de stock y precio
    - El modelo Cliente(en la app de ventas), que recibe un nombre, un mail y un dni como atributos.
    - El modelo Transaccion(tambien en la app de ventas), que consta de un numero de transaccion, el cliente, el producto y a cantidad vendida en la transaccion, la fecha de venta y el precio total. Tanto el producto como el cliente estan relacionados a este modelo mediante una clave foranea.

La tienda esta desarrollada con un template padre que contiene el nav, y el footer el cual se repite para todos los demas templates. 

Al iniciarse, se muestra el index.html con el nombre de la tienda, la barra de navegacion  (que te redirige a las otras pestañas de la tienda: clientes, productos, ventas), y el formulario de busqueda de productos. Pueden testear su funcionamiento usando Rey, u Obi como ejemplos.

Las demas paginas se inicializan con el formulario vacio para poder ingresar un nuevo producto, cliente o venta realizada.
Para probarlos, sugiero estos ejemplos:

    -Producto:
    sable Anakin Skywalker
    120cm
    gris plata con negro
    azul
    2
    sable inspirado en el jedi de las precuelas
    200

    -Producto2:
    sable Mace Windu
    100cm
    gris plata con blanco
    violeta
    2
    sable inspirado en el jedi de las precuelas
    200 

    -Cliente:
    Padawan Ramiro
    padawanR@mail.com
    3213151

- Hasta acá los requerimientos del TP -

- Cosas que me gustaria agregar:
   
    - en la busqueda de producto:  
        ### como verificar si el producto existe? 
        ### como envio 'error' si no completo el campo de busqueda?
        ### como traigo no solo el producto sino tambien el precio y otros datos

    - en el formulario de ventas:
        ### el nro de transaccion no deberia poder repetirse... quiza traer el nro siguiente al que esta?
        ### el precio total deberia ser un resultado de la cantidad (elegida por el usuario), y el precio (traido del modelo)
        ### la cantidad no deberia ser superior al stock 

