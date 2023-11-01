from django.shortcuts import render
from auricular.models import Auricular
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from auricular.forms import BusquedaAuricularFormulario

class CrearAuricular(CreateView):
    model = Auricular
    template_name = "auricular/crear_auricular.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('auricular')

def auris(request):
    formulario = BusquedaAuricularFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_auriculares = Auricular.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaAuricularFormulario()
    return render(request, 'auricular/auriculares.html', {'formulario': formulario, 'listado_de_auriculares': listado_de_auriculares})