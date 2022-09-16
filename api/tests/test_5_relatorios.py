import api.gerar_dados as dados
from api.models import Sinalizar, Sobrevivente
from django.urls import reverse
from rest_framework.test import APITestCase


class SobreviventeTestCase(APITestCase):
 
    def setUp(self):
        self.list_urls = reverse('sobreviventes-list')
        self.qtd_sobreviventes = 5
        for i in range(self.qtd_sobreviventes): 
            nome, idade, sexo, latitude, longitude= dados.sobrevivente2(seed=i+1) 
            Sobrevivente.objects.create(
                nome=nome,
                idade=idade,
                sexo=sexo,
                latitude=latitude,
                longitude=longitude,
            )

        sobrevivente_infectado = Sobrevivente.objects.all().last()
        sobreviventes = Sobrevivente.objects.all()
        for i, sobrevivente in enumerate(sobreviventes):
            Sinalizar.objects.create(                 
                sobrevivente=sobrevivente,  
                sobrevivente_infectado=sobrevivente_infectado
            ) 
            if i >= 2:
                break
    
    def tearDown(self):
        Sobrevivente.objects.all().delete()
        Sinalizar.objects.all().delete()

    def test_relatorio_infectados_nao_infectados(self):
        """Teste para ara verificar os sobreviventes infectados e não infectados"""        
        # Relatório dos sobreviventes infectado e não infectados
        # Total de sobreviventes: 5
        # Sobreviventes infectados: 1
        # Sobreviventes não infectado: 4
        # Percentual infectado: 20 %
        # Percentual não infectado: 80 % 
        per_infectado = round(1 * 100 / self.qtd_sobreviventes, 1)
        per_nao_infectado = round(((self.qtd_sobreviventes - 1) * 100) / self.qtd_sobreviventes, 1)
        response2 = self.client.get('/sobreviventes/infectados-nao-infectados/')
        # Teste que verifica a quantidade de sobrevientes infectados
        self.assertEqual(response2.data['total_infectados'], 1)
        # Teste que verifica a quantidade de sobrevientes não infectados
        self.assertEqual(response2.data['total_nao_infectados'], self.qtd_sobreviventes - 1)
        # Teste que verifica o percentual de sobrevientes não infectados
        self.assertEqual(response2.data['per_infectados'], per_infectado)
        # Teste que verifica o percentual de sobrevientes não infectados
        self.assertEqual(response2.data['per_nao_infectados'], per_nao_infectado)
