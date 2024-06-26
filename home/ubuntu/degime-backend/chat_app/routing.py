from chat_app.consumers import TextRoomConsumer, PersonalConsumer
from django.urls.conf import re_path

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/(?P<token>[^/]+)/(?P<username>[^/]+)$', TextRoomConsumer.as_asgi()),
    re_path(r'^ws/personal_chat/(?P<room_name>[^/]+)/(?P<token>[^/]+)/(?P<username>[^/]+)$', PersonalConsumer.as_asgi()),
]
