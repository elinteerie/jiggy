# your_app_name/routing.py
from django.urls import re_path
from post import consumers

websocket_urlpatterns = [
    re_path(r'ws/posts/$', consumers.PostConsumer.as_asgi()),
]
