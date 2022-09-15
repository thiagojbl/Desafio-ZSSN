import api.gerar_dados as dados
from api.models import Sinalizar, Sobrevivente
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SobreviventeTestCase(APITestCase):
 
    def setUp(self):
        self.list_urls = reverse('sobreviventes-list')
        Sobrevivente.objects.all().delete()
    
    def tearDown(self):
        Sobrevivente.objects.all().delete()
        Sinalizar.objects.all().delete()

    def test_relatorio_infectados_nao_infectados(self):
        """Teste para ara verificar os sobreviventes infectados e não infectados"""
        # Criando 5 sobreviventes
        qtd_sobreviventes = 100
        for i in range(qtd_sobreviventes): 
            nome, idade, sexo, latitude, longitude= dados.sobrevivente2(seed=i+1) 
            sobrevivente1 = Sobrevivente.objects.create(
                nome=nome,
                idade=idade,
                sexo=sexo,
                latitude=latitude,
                longitude=longitude,
            )
        # Listando todos os sobreviventes 
        qtd_sobreviventes = Sobrevivente.objects.all().count()
        response = self.client.get('/sobreviventes/infectados-nao-infectados/')
        print('response: ', response.data)
        # Teste que verifica a quantidade de sobrevientes infectados
        self.assertEqual(response.data['total_infectados'], 0)
        # Teste que verifica a quantidade de sobrevientes não infectados
        self.assertEqual(response.data['total_nao_infectados'], qtd_sobreviventes)
        # Teste que verifica o percentual de sobrevientes não infectados
        self.assertEqual(response.data['per_infectados'], 0.0)
        # Teste que verifica o percentual de sobrevientes não infectados
        self.assertEqual(response.data['per_nao_infectados'], 100.0)

        # Vamos sinalizar um sobrevivente (infectado) 
        # Definir sobrevivente infectado 
        sobrevivente_infectado = Sobrevivente.objects.all().last()
        # Listando todos os sobreviventes
        sobreviventes = Sobrevivente.objects.all()
        print('sobreviventes: ', sobreviventes)
        for i, sobrevivente in enumerate(sobreviventes):
            Sinalizar.objects.create(                 
                sobrevivente=sobrevivente,  
                sobrevivente_infectado=sobrevivente_infectado
            ) 
            if i >= 2:
                break
        
        # Relatório dos sobreviventes infectado e não infectados
        # Total de sobreviventes: 5
        # Sobreviventes infectados: 1
        # Sobreviventes não infectado: 4
        # Percentual infectado: 20 %
        # Percentual não infectado: 80 % 
        per_infectado = round(1 * 100 / qtd_sobreviventes, 1)
        per_nao_infectado = round(((qtd_sobreviventes - 1) * 100) / qtd_sobreviventes, 1)
        print('Percentual: ', per_infectado)
        response2 = self.client.get('/sobreviventes/infectados-nao-infectados/')
        print('response2: ', response2.data)
        # Teste que verifica a quantidade de sobrevientes infectados
        self.assertEqual(response2.data['total_infectados'], 1)
        # Teste que verifica a quantidade de sobrevientes não infectados
        self.assertEqual(response2.data['total_nao_infectados'], qtd_sobreviventes - 1)
        # Teste que verifica o percentual de sobrevientes não infectados
        self.assertEqual(response2.data['per_infectados'], per_infectado)
        # Teste que verifica o percentual de sobrevientes não infectados
        self.assertEqual(response2.data['per_nao_infectados'], per_nao_infectado)







