from django.shortcuts import render
from reloj.models import Reloj
from django.urls import reverse_lazy
from reloj.forms import BusquedaRelojFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CrearReloj(LoginRequiredMixin, CreateView):
    model = Reloj
    template_name = "reloj/crear_reloj.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('reloj')


def reloj(request):
    formulario = BusquedaRelojFormulario(request.GET)
    listado_de_relojes = None
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_relojes = Reloj.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaRelojFormulario()
    return render(request, 'reloj/relojes.html', {'formulario': formulario, 'listado_de_relojes': listado_de_relojes})
    
 
class ActualizarReloj(LoginRequiredMixin, UpdateView):
    model = Reloj
    template_name = "reloj/actualizar_reloj.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion', 'foto']
    success_url = reverse_lazy('reloj')


class DetalleReloj(DetailView):
    model = Reloj
    template_name = "reloj/detalle_reloj.html"

class EliminarReloj(LoginRequiredMixin, DeleteView):
    model = Reloj
    template_name = "reloj/eliminar_reloj.html"
    success_url = reverse_lazy('reloj')