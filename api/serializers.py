from rest_framework import serializers 
from .models import Itens, Sobrevivente, SobreviventeInventario, Sinalizar

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ['id', 'nome', 'idade', 'sexo', 'latitude', 'longitude', 'infectado', 'inventario']

class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = ['id', 'nome', 'pontos']

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreviventeInventario
        fields = ['id', 'item', 'sobrevivente', 'quantidade']


class SinalizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinalizar
        fields = ['id', 'sobrevivente', 'sobrevivente_infectado']