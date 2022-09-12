# from django.db.models import (Avg, Count, DecimalField, ExpressionWrapper, F, Sum)

from rest_framework import viewsets
from api.models import Sobrevivente, Itens 
from api.serializers import SobreviventeSerializer, ItensSerializer

class SobreviventeViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.all() 
    serializer_class = SobreviventeSerializer

class ItensViewSet(viewsets.ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer