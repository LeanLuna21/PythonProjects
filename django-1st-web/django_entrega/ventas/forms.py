from django import forms
# importamos los modelos para traer info de ellos en el formulario que se vera en el html 
from ventas.models import Cliente,Producto

# creamos los formularios para recibir los datos del html
class ClienteFormulario (forms.Form):
    nombre = forms.CharField()
    mail = forms.EmailField()
    dni = forms.IntegerField()

class TransaccionFormulario (forms.Form):
    nro_transaccion = forms.IntegerField()
    cliente = forms.ModelChoiceField(       # genera un campo de seleccion
        queryset=Cliente.objects.all(),     # genera una consulta al objeto
        to_field_name='nombre',             # trae los nombres para que el admin pueda elegir
        required=True,
        )
    producto = forms.ModelChoiceField(      # ditto
        queryset=Producto.objects.all(),  
        to_field_name='nombre',           
        required=True,
        )
    cantidad = forms.IntegerField()
    precio_total = forms.FloatField()                   
    fecha_de_venta = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
                                        # de esta forma agregamos un placeholder, para que el usuario sepa que formato
                                        # debe usar para completar la fecha de venta

# cosas por agregar:

# el nro de transaccion no deberia poder repetirse... quiza traer el nro siguiente al que esta?
# el precio total deberia ser un resultado de la cantidad (elegida por el usuario), y el precio (traido del modelo)
# la cantidad no deberia ser superior al stock