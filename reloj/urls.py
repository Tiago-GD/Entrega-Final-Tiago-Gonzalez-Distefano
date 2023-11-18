from django.urls import path
from reloj.views import CrearReloj, reloj, EliminarReloj, DetalleReloj, ActualizarReloj

urlpatterns = [
        path('crear_reloj/', CrearReloj.as_view(), name='crear_reloj'),
        path('reloj/', reloj, name='reloj'),  
        path('reloj/<int:pk>/eliminar/', EliminarReloj.as_view(), name='eliminar_reloj'),
        path('reloj/<int:pk>/detalle/', DetalleReloj.as_view(), name='detalle_reloj'),
        path('reloj/<int:pk>/actualizar/',ActualizarReloj.as_view(),name='actualizar_reloj')
    ]