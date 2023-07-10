from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializer, models

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ClienteView(viewsets.ModelViewSet):

    queryset = models.Cliente.objects.all()
    serializer_class = serializer.ClienteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome',]
    search_fields = ['nome', 'cpf']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]





