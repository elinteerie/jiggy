import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import post.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jiggy.settings')

# Ensure Django setup is called before the application is initialized
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            post.routing.websocket_urlpatterns
        )
    ),
})