from django.urls import path
from auricular.views import CrearAuricular, auris

urlpatterns = [
        path('crear_auricular/', CrearAuricular.as_view(), name='crear_auricular'),
        path(' ', auris, name='auricular')
    ]