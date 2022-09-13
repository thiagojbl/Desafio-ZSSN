# from django.db.models import (Avg, Count, DecimalField, ExpressionWrapper, F, Sum)

from rest_framework import viewsets
from api.models import Sobrevivente, Itens, Sinalizar, SobreviventeInventario 
from api.serializers import SobreviventeSerializer, ItensSerializer, SinalizarSerializer, InventarioSerializer

class SobreviventeViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.all() 
    serializer_class = SobreviventeSerializer

class ItensViewSet(viewsets.ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = SobreviventeInventario.objects.all()
    serializer_class = InventarioSerializer


class SinalizarViewSet(viewsets.ModelViewSet):
    queryset = Sinalizar.objects.all()
    serializer_class = SinalizarSerializer






# class NegociarViewSet(viewsets.ModelViewSet):
#     queryset = Negociar.objects.all()
#     serializer_class = NegociarSerializer    