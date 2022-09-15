from django.db.models import (Avg, Count, DecimalField, ExpressionWrapper, F,
                              Sum)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Itens, Sinalizar, Sobrevivente, SobreviventeInventario
from api.serializers import (InventarioSerializer, ItensSerializer,
                             SinalizarSerializer, SobreviventePatchSerializer,
                             SobreviventeSerializer)


class SobreviventeViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.all()
    filter_backend = [DjangoFilterBackend]
    http_method_names = ['get', 'post', 'patch']
    # serializer_class = SobreviventeSerializer

    def get_serializer_class(self):
        if self.request.method == 'PATCH': 
            return SobreviventePatchSerializer
        else:
            return SobreviventeSerializer

    @action(methods=["get"], detail=False,  url_path=r'infectados-nao-infectados')
    def infectados(self, request):
        count_sob = Sobrevivente.objects.all().count()
        count_inf = Sobrevivente.objects.filter(
            infectado=True).count()

        count_no_inf = Sobrevivente.objects.filter(
            infectado=False).count()
        # print('\nSobreviventes: ', cout_sob)
        # print('\nInfectados: ', cout_inf)
        # print('\nNo Infectado: ', cout_no_inf)
        per_infectados = (count_inf * 100) / count_sob
        per_noinfectados = (count_no_inf * 100) / count_sob

        return Response({
            'total_sobreviventes': count_sob,
            'total_nao_infectados': count_no_inf,
            'total_infectados': count_inf,
            'per_infectados':  round(per_infectados, 1),
            'per_noinfectados': round(per_noinfectados, 1)
        }, status=200)

    @action(methods=["get"], detail=False,  url_path=r'perdidos')
    def perdidos(self, request):
        total = SobreviventeInventario.objects.filter(
            sobrevivente__infectado=True).annotate(
                perdidos=ExpressionWrapper(
                    F('quantidade') * F('item__pontos'),
                    output_field=DecimalField()))

        # total_nao_infectado = SobreviventeInventario.objects.filter(
        #     sobrevivente__infectado=False).annotate(
        #         nao_infectado=ExpressionWrapper(
        #             F('quantidade') * F('item__pontos'), 
        #             output_field=DecimalField()))

        return Response({
            'pontos_perdidos': total.aggregate(total=Sum('perdidos'))['total']
        }, status=200)

    @action(methods=["get"], detail=False,  url_path=r'mediaitens')
    def media_itens(self, request):
        # Obtem todos os itens
        itens = Itens.objects.all()
        # Obtem a quantidade de sobreviventes
        count_sobreviventes = Sobrevivente.objects.filter(infectado=False).count()
        print(count_sobreviventes)
        # Gera uma lista mádia
        media_geral = {"media": []}
        for item in itens:  
            media_itens = SobreviventeInventario.objects.filter(
                sobrevivente__infectado=False, item__nome=item).annotate(
                    sobrevivente_count=Count('sobrevivente'),
                    itens=Avg('quantidade')).values(
                        'item__nome', 'quantidade')           
            soma_total = media_itens.aggregate(Sum('quantidade'))
            media_geral["media"].append(
                {
                    f'{item}': round(soma_total['quantidade__sum']/count_sobreviventes, 1),
                }
            )
        print(media_geral)
        # payload = dict(media_geral=media_geral)
        return Response(media_geral, status=200)

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
