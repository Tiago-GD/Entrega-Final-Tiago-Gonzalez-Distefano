from django.urls import path
from telefono.views import inicio, telefono, CrearTelefono,EliminarTelefono,DetalleTelefono,ActualizarTelefono,AboutMe

urlpatterns = [
    path('', inicio, name='inicio'),
    path('AboutMe/', AboutMe, name='AboutMe'),
    path('telefono/', telefono, name='telefono' ),
    path('crear_telefonor/', CrearTelefono.as_view(), name='crear_telefono'),
    path('telefono/<int:pk>/eliminar/', EliminarTelefono.as_view(), name='eliminar_telefono'),
    path('telefono/<int:pk>/detalle/', DetalleTelefono.as_view(), name='detalle_telefono'),
    path('telefono/<int:pk>/actualizar/',ActualizarTelefono.as_view(),name='actualizar_telefono')

]