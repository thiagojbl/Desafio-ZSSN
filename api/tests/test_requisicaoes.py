from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Sobrevivente
import api.gerar_dados as dados
from rest_framework import status
from rest_framework.test import RequestsClient

 
class SobreviventeTestCase(APITestCase):

    def setUp(self):
        self.list_urls = reverse('sobreviventes-list')
        s1 = dados.sobrevivente(seed=1) 
        self.sobrevivente1 = Sobrevivente.objects.create(
            nome=s1['nome'],
            idade=s1['idade'],
            sexo=s1['sexo'],
            latitude=s1['latitude'],
            longitude=s1['longitude'],
        )

    def test_requisicao_get_para_listar_sobrevivente(self):
        """Teste para verificar a requisição GET para listar os sobreviventes"""
        response = self.client.get(self.list_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_sobrevivente(self):
        """Teste par averificar a requisição POST para criar um curso"""
        data = dados.sobrevivente(1)
        response = self.client.post(self.list_urls, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_sobrevivente(self):
        """Teste para verificar requisição DELETE não permitido para deletar um sobrevivente"""  
        response = self.client.delete('/sobreviventes/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_patch_para_atualizar_sobrevivente(self):
        """Teste para verificar a requisição PATCH para atualizar dados de um sobrevivente"""
        # Sobrevivente 1
        # {'nome': 'Miguel Campos', 'idade': '23', 'sexo': 'Masculino', 'latitude': Decimal('-21.5304285'), 'longitude': Decimal('-116.692879')}
        # seed -> Garante que serão esses dados acima (seed=1)
        data = {'nome': 'Bryan Cardoso', 'idade':20}
        response = self.client.patch('/sobreviventes/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_requisicao_delete_para_put_sobrevivente(self):
        """Teste para verificar requisição PUT não permitido para atualizar todos os campos de um sobrevivente"""  
        # Sobrevivente 1
        # {'nome': 'Miguel Campos', 'idade': '23', 'sexo': 'Masculino', 'latitude': Decimal('-21.5304285'), 'longitude': Decimal('-116.692879')}
        # seed -> Garante que serão esses dados acima (seed=1)

        # Sobrevivente 2
        # {'nome': 'Miguel Campos', 'idade': '23', 'sexo': 'Masculino', 'latitude': Decimal('-21.5304285'), 'longitude': Decimal('-116.692879')}
        # seed -> Garante que serão esses dados acima (seed=2)
        data = dados.sobrevivente(seed=2)
        response = self.client.put('/sobreviventes/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_verificar_quantidade_de_sobrevivente(self):
        """Teste para verificar a quantidade de sobreviventes na base de dados"""
        # Sobrevivente 1
        # {'nome': 'Miguel Campos', 'idade': '23', 'sexo': 'Masculino', 'latitude': Decimal('-21.5304285'), 'longitude': Decimal('-116.692879')}
        # Temos um sobrevivente cadastrado e vamos gerar 9... total = 10
        for i in range(9):
            s = dados.sobrevivente(seed=(i+2)) 
            Sobrevivente.objects.create(
                nome=s['nome'],
                idade=s['idade'],
                sexo=s['sexo'],
                latitude=s['latitude'],
                longitude=s['longitude'],
            )
        response = self.client.get(self.list_urls, format='json') 
        sobreviventes = Sobrevivente.objects.all()
        # Verifica se a requisição GET teve sucesso
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica a quantidade de sobreviventes
        self.assertEqual(len(response.data), 10) 
        # Verifica se o nome do primeiro sobrevivente está correto
        self.assertEqual(response.data[0].get('nome'), 'Miguel Campos') 
