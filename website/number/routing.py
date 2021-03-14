from django.urls import path
from .consumers import NumberConsumer

ws_urlpatterns = [
	path('ws/number/', NumberConsumer.as_asgi())
]