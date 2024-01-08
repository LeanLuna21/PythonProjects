from django.shortcuts import render
from django.http import HttpResponse
from ventas.models import Cliente, Transaccion
from ventas.forms import ClienteFormulario,TransaccionFormulario


# Create your views here.
def ingresar_cliente(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(
                nombre=informacion["nombre"],
                mail=informacion["mail"],
                dni=informacion["dni"])
            cliente.save()
            return render(request,"index.html")

    else:
        mi_formulario = ClienteFormulario()
        return render(request,"clientes.html", {"mi_formulario": mi_formulario})


def ingresar_venta(request):
    if request.method == "POST":
        mi_formulario = TransaccionFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            venta = Transaccion(
                nro_transaccion=informacion["nro_transaccion"],
                cliente=informacion["cliente"],
                producto=informacion["producto"],
                cantidad=informacion["cantidad"],
                precio_total=informacion["precio_total"],
                fecha_de_venta=informacion["fecha_de_venta"])
            venta.save()
            return render(request,'index.html') 

    else:
        mi_formulario = TransaccionFormulario()
        return render(request,'ventas.html', {"mi_formulario": mi_formulario})
