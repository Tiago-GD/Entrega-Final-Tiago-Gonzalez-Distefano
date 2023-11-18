from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from telefono.forms import BusquedaTelefonoFormulario
from telefono.models import Telefono  

def inicio(request): 
    return render(request, 'telefono/inicio.html', {})

def AboutMe(request): 
    return render(request, 'telefono/AboutMe.html', {})

class CrearTelefono(LoginRequiredMixin, CreateView):
    model = Telefono
    template_name = "telefono/crear_telefono.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion', 'foto']
    success_url = reverse_lazy('telefono')

def telefono(request):
    formulario = BusquedaTelefonoFormulario(request.GET)
    listado_de_telefonos = None
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_telefonos = Telefono.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaTelefonoFormulario()
    return render(request, 'telefono/telefonos.html', {'formulario': formulario, 'listado_de_telefonos': listado_de_telefonos})
    
class ActualizarTelefono(LoginRequiredMixin, UpdateView):
    model = Telefono
    template_name = "telefono/actualizar_telefono.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion', 'foto']
    success_url = reverse_lazy('telefono')


class DetalleTelefono(DetailView):
    model = Telefono
    template_name = "telefono/detalle_telefono.html"

class EliminarTelefono(LoginRequiredMixin, DeleteView):
    model = Telefono
    template_name = "telefono/eliminar_telefono.html"
    success_url = reverse_lazy('telefono')