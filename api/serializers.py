from rest_framework import serializers 
from .models import Itens, Sobrevivente

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ['nome', 'idade', 'sexo', 'latitude', 'longitude', 'infectado']

class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = ['nome', 'pontos']
