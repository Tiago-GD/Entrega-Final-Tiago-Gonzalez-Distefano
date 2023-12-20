from django.urls import path
from .views import chat, send_message

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('send_message/', send_message, name='send_message'),
]
