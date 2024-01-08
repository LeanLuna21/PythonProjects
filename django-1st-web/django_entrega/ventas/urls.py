from django.urls import path
from ventas.views import *

urlpatterns = [
        path('ingresar_cliente/',ingresar_cliente, name="clientes"), # le asignamos un nombre a las url para luego llamarlas
        path('ingresar_venta/',ingresar_venta, name="ventas")      # en el html de la misma forma ej: href= {% url 'clientes' %}
]