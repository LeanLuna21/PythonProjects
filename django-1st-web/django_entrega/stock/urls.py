from django.urls import path
from stock.views import *

urlpatterns = [
    path('ingresar_producto/',ingresar_producto, name="productos"),
    path('buscar_producto/',buscar, name='buscar_producto')
]