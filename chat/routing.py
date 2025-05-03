from django.urls import re_path

from . import consumer



websocket_urlpatterns = [

    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
    re_path(r'ws/notifications/(?P<user_id>\w+)/$', consumer.NotificationConsumer.as_asgi()),

]