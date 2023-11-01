from django.shortcuts import render
from reloj.models import Reloj
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from reloj.forms import BusquedaRelojFormulario

class CrearReloj(CreateView):
    model = Reloj
    template_name = "reloj/crear_reloj.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('reloj')
    queryset = Reloj.objects.using('RelojBD').all()


def reloj(request):
    formulario = BusquedaRelojFormulario(request.GET)
    listado_de_relojes = None
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_relojes = Reloj.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaRelojFormulario()
    return render(request, 'reloj/relojes.html', {'formulario': formulario, 'listado_de_relojes': listado_de_relojes})
    