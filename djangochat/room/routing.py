from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('/ws/hobby/', consumers.ChatConsumer.as_asgi()),
]