from django.urls import path
from auricular.views import CrearAuricular, auris, ActualizarAuricular, DetalleAuricular, EliminarAuricular

urlpatterns = [
        path('crear_auricular/', CrearAuricular.as_view(), name='crear_auricular'),
        path('auricular/', auris, name='auricular'),
        path('auricular/<int:pk>/eliminar/', EliminarAuricular.as_view(), name='eliminar_auricular'),
        path('auricular/<int:pk>/detalle/', DetalleAuricular.as_view(), name='detalle_auricular'),
        path('auricular/<int:pk>/actualizar/',ActualizarAuricular.as_view(),name='actualizar_auricular')
    ]