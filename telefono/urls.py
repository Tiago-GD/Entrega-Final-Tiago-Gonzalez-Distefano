from django.urls import path
from telefono.views import inicio, telefono, CrearTelefono

urlpatterns = [
    path('', inicio, name='inicio'),
    path('telefono/', telefono, name='telefono' ),
    path('crear_telefonor/', CrearTelefono.as_view(), name='crear_telefono'),
    

    ]