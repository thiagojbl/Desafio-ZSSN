from django.db.models import (Avg, Count, DecimalField, ExpressionWrapper, F, Sum)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Sobrevivente, Itens, Sinalizar, SobreviventeInventario 
from api.serializers import SobreviventeSerializer, ItensSerializer, SinalizarSerializer, InventarioSerializer

class SobreviventeViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.all() 
    serializer_class = SobreviventeSerializer
    filter_backend = [DjangoFilterBackend]
    http_method_names = ['get', 'post', 'patch']

    @action(methods=["get"], detail=False,  url_path=r'infectados')
    def infectados(self, request):
        cout_sob = Sobrevivente.objects.all().count()
        cout_inf = Sobrevivente.objects.filter(
            infectado=True).count()
        cout_no_inf = Sobrevivente.objects.filter(
            infectado=False).count()
        # print('\nSobreviventes: ', cout_sob)
        # print('\nInfectados: ', cout_inf)
        # print('\nNo Infectado: ', cout_no_inf)
        per_infectados = (cout_inf * 100) / cout_sob
        per_noinfectados = (cout_no_inf * 100) / cout_sob

        return Response({
            'total': cout_sob,
            'cout_no_inf': cout_no_inf,
            'cout_inf': cout_inf,
            'per_infectados':  per_infectados,
            'per_noinfectados': per_noinfectados
        }, status=200)

    @action(methods=["get"], detail=False,  url_path=r'perdidos')
    def perdidos(self, request):
        total = SobreviventeInventario.objects.filter(
            sobrevivente__infectado=True).annotate(
                perdidos=ExpressionWrapper(
                    F('quantidade') * F('item__pontos'),
                    output_field=DecimalField()))

        total_nao_infectado = SobreviventeInventario.objects.filter(
            sobrevivente__infectado=False).annotate(
                nao_infectado=ExpressionWrapper(
                    F('quantidade') * F('item__pontos'),
                    output_field=DecimalField()))

        return Response({
            'pontos_perdidos': total.aggregate(total=Sum('perdidos'))['total'],
            'pontos_nao_infectado': total_nao_infectado.aggregate(
                total_nao_infectado=Sum('nao_infectado'))['total_nao_infectado']
        }, status=200)

    @action(methods=["get"], detail=False,  url_path=r'mediaitens')
    def media_itens(self, request):
        media_itens = SobreviventeInventario.objects.filter(
            sobrevivente__infectado=False).annotate(
                sobrevivente_count=Count('sobrevivente'),
                itens=Avg('quantidade')).values(
                    'item__nome', 'quantidade')
        print('media_itens:', media_itens)

        return Response(media_itens, status=200)

class ItensViewSet(viewsets.ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer
    http_method_names = ['get', 'post']


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = SobreviventeInventario.objects.all()
    serializer_class = InventarioSerializer


class SinalizarViewSet(viewsets.ModelViewSet):
    queryset = Sinalizar.objects.all()
    serializer_class = SinalizarSerializer


# class NegociarViewSet(viewsets.ModelViewSet):
#     queryset = Negociar.objects.all()
#     serializer_class = NegociarSerializer    