from django.test import TestCase
from api.models import Sobrevivente, Itens, SobreviventeInventario

class SobreviventeModelTestCase(TestCase):
    
    
    def setUp(self):
        self.sobrevivente = Sobrevivente(
            nome = 'José',
            idade = 25,
            sexo = 'Masculino',
            latitude = '0384756',
            longitude = '9384756', 
            # infectado = default(False)
        )

    def test_verifica_atributos_de_sobreviventes(self):
        """Teste que verifica os atributos de um sobrevivente com valor default para infectado"""
        self.assertEqual(self.sobrevivente.nome, 'José')
        self.assertEqual(self.sobrevivente.idade, 25)
        self.assertEqual(self.sobrevivente.sexo, 'Masculino')
        self.assertEqual(self.sobrevivente.latitude, '0384756')
        self.assertEqual(self.sobrevivente.longitude, '9384756')
        self.assertEqual(self.sobrevivente.infectado, False) 