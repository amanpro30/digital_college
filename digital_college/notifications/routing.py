from channels.routing import ProtocolTypeRouter,URL Router
from django.urls import path

from notifications.consumer import EchoConsumer
 
application=ProtocolTypeRouter({
    'websocket':URLRouter([
        path('ws/',EchoConsumer),
    ])
})