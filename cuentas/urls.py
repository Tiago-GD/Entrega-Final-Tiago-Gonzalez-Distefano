from django.urls import path
from cuentas.views import login, registrarse, editar_perfil, CambiarPassword, ver_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name= 'login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('regitro/', registrarse, name= 'registro'),
    path('editar_perfil/', editar_perfil, name= 'editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password'),
    path('perfil/cuenta/info/', ver_perfil , name='info_cuenta'),

]
