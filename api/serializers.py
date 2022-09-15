from rest_framework import serializers

from .models import (Itens, Negociar, Sinalizar, Sobrevivente,
                     SobreviventeInventario)


class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ['id', 'nome', 'idade', 'sexo', 'latitude', 
            'longitude', 'infectado', 'inventario']

class SobreviventePatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ['id', 'latitude', 'longitude']


class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Itens
        fields = ['id', 'nome', 'pontos']
    def validate(self, data):
        if data['pontos'] < 0: 
            raise serializers.ValidationError(
                'Os pontos não pode ser negativo.')
        return data

class InventarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SobreviventeInventario
        fields = ['id', 'item', 'sobrevivente', 'quantidade']

    def validate(self, data):
        if data['quantidade'] < 0:
            raise serializers.ValidationError(
                'A quantidade de itens não pode ser negativo.')
        return data

class SinalizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinalizar
        fields = ['id', 'sobrevivente', 'sobrevivente_infectado']


class NegociarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negociar
        fields = '__all__'

    sobrevivente1_itens = serializers.ListField(
        child=serializers.IntegerField(), write_only=True)
    sobrevivente2_itens = serializers.ListField(
        child=serializers.IntegerField(), write_only=True)
    sobrevivente1_quantidade = serializers.ListField(
        child=serializers.IntegerField(), write_only=True)
    sobrevivente2_quantidade = serializers.ListField(
        child=serializers.IntegerField(), write_only=True)

    def validate(self, data):

        if len(data['sobrevivente1_itens']) != len(data['sobrevivente1_quantidade']):
            raise serializers.ValidationError(
                'Ids dos itens e quantidade do sobrevivente1 não são compativeis.')
        if len(data['sobrevivente2_itens']) != len(data['sobrevivente2_quantidade']):
            raise serializers.ValidationError(
                'Ids dos itens e quantidade do sobrevivente2 não são compativeis.')

        data['sobrevivente1_instanceitens'] = []
        sobrevivente1_pontos = 0
        for item_id, quantidade in zip(data['sobrevivente1_itens'], data['sobrevivente1_quantidade']):
            if data['sobrevivente1'].inventario_sobreviventes.filter(pk=item_id).exists():
                data['sobrevivente1_instanceitens'].append(
                    data['sobrevivente1'].inventario_sobreviventes.filter(pk=item_id).first())
                if data['sobrevivente1_instanceitens'][-1].quantidade < quantidade:
                    raise serializers.ValidationError(
                        f'O sobrevivente1 não possui itens suficientes no estoque para o id {item_id}')
                sobrevivente1_pontos += data['sobrevivente1_instanceitens'][-1].item.pontos * quantidade
            else:
                raise serializers.ValidationError(
                    f'O sobrevivente1 não possui itens estoque para o id {item_id}')

        data['sobrevivente2_instanceitens'] = []
        sobrevivente2_pontos = 0
        for item_id, quantidade in zip(data['sobrevivente2_itens'], data['sobrevivente2_quantidade']):
            if data['sobrevivente2'].inventario_sobreviventes.filter(pk=item_id).exists():
                data['sobrevivente2_instanceitens'].append(
                    data['sobrevivente2'].inventario_sobreviventes.filter(pk=item_id).first())
                if data['sobrevivente2_instanceitens'][-1].quantidade < quantidade:
                    raise serializers.ValidationError(
                        f'O sobrevivente2 não possui itens suficientes no estoque para o id {item_id}')
                sobrevivente2_pontos += data['sobrevivente2_instanceitens'][-1].item.pontos * quantidade
            else:
                raise serializers.ValidationError(
                    f'O sobrevivente2 não possui itens estoque para o id {item_id}')

        if sobrevivente1_pontos != sobrevivente2_pontos:
            raise serializers.ValidationError(
                f'Quantidade de prontos dos sobreviventes são diferentes.')

        return data

    def create(self, validated_data):
        print('validated_data: ', validated_data)
        insert_data = {
            'sobrevivente1': validated_data['sobrevivente1'],
            'sobrevivente2': validated_data['sobrevivente2']
        }
        with transaction.atomic():
            instace = super().create(insert_data)
            for item, quantidade in zip(validated_data['sobrevivente1_instanceitens'], validated_data['sobrevivente1_quantidade']):
                item.quantidade -= quantidade
                item.save()
            for item, quantidade in zip(validated_data['sobrevivente2_instanceitens'], validated_data['sobrevivente2_quantidade']):
                item.quantidade -= quantidade
                item.save()
        return instace      
