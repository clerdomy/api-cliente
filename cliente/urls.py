from django.urls import path, include
from rest_framework import routers
from .views import ClienteView

router = routers.DefaultRouter()
router.register('clientes',viewset=ClienteView, basename="clientes")

urlpatterns = [
    path('', include(router.urls)),
]
