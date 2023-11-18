from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import MiFormularioDeCreacion, EdicionPerfil
from django.urls import reverse_lazy
from cuentas.models import DatosExtra

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')
              
    return render(request, 'cuentas/login.html', {'form': formulario})

def registrarse(request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
            
    return render(request, 'cuentas/registrarse.html', {'formulario': formulario})

def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = EdicionPerfil(instance=request.user, initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar})
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nueva_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nueva_avatar:
                datos_extra.avatar = nueva_avatar
            
            datos_extra.save()
            formulario.save()
            
            return redirect('info_cuenta')
    
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('info_cuenta')
    
def ver_perfil(request):
    return render(request, 'cuentas/cuenta_info.html')
