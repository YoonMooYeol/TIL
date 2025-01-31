# chat/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ChatViewSet
from .views import ChatViewSet

router = DefaultRouter()
router.register(r'conversations', ChatViewSet, basename='conversation')

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', ChatViewSet.as_view({'get': 'chat_interface'}), name='chat_interface'),
]