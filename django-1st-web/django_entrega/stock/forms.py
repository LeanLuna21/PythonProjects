from django import forms

# creamos el formulario que traera los datos del html
class ProductoFormulario(forms.Form):
    nombre= forms.CharField()
    medida= forms.CharField()
    color_sable= forms.CharField()
    color_luz= forms.CharField() 
    stock= forms.IntegerField()
    descripcion= forms.CharField()
    precio=forms.FloatField()
    