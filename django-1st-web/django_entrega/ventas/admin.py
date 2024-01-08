from django.contrib import admin

# Registramos los modelos para que impacten en la BBDD.

from ventas.models import Cliente,Transaccion
admin.site.register(Cliente)
admin.site.register(Transaccion)