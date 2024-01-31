import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import social_app.routing
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Degime_backend.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":  AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(
            social_app.routing.websocket_urlpatterns
        )
    )),        
})

