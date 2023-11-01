from django.urls import path
from reloj.views import CrearReloj, reloj

urlpatterns = [
        path('crear_reloj/', CrearReloj.as_view(), name='crear_reloj'),
        path(' ', reloj, name='reloj'),
    ]