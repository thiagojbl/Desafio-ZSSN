from api.models import Itens
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ItensTestCase(APITestCase):

    def setUp(self): 
        self.list_urls = reverse('itens-list')
        self.item = Itens.objects.create(
            nome='Água',
            pontos=4
        )

    def test_requisicao_get_para_listar_itens(self):
        """Teste para verificar a requisição GET para listar os itens"""
        response = self.client.get(self.list_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_itens(self):
        """Teste par averificar a requisição POST para criar um item"""
        data = {'nome': 'Água', 'pontos': 4}
        response = self.client.post(self.list_urls, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_para_nao_permitir_criar_itens_com_pontos_negativo(self):
        """Teste par averificar a requisição POST que não permite criar um item com pontos negativos"""
        data = {'nome': 'Água', 'pontos': -4} 
        response = self.client.post(self.list_urls, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
