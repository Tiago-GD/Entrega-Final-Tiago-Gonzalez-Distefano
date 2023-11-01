from django.shortcuts import render
from telefono.models import Telefono
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from telefono.forms import BusquedaTelefonoFormulario

def inicio(request): 
    return render(request, 'telefono/inicio.html', {})

class CrearTelefono(CreateView):
    model = Telefono
    template_name = "telefono/crear_telefono.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('telefono')
    queryset = Telefono.objects.using('TelefonoBD').all()


def telefono(request):
    formulario = BusquedaTelefonoFormulario(request.GET)
    listado_de_telefonos = None
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_telefonos = Telefono.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaTelefonoFormulario()
    return render(request, 'telefono/telefonos.html', {'formulario': formulario, 'listado_de_telefonos': listado_de_telefonos})
    