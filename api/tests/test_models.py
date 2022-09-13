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


class ItensModelTestCase(TestCase):
    
    
    def setUp(self):
        self.itens = Itens(
            nome = 'Água',
            pontos = 5,
        )

    def test_verifica_atributos_de_itens(self):
        """Teste que verifica os atributos de um item"""
        self.assertEqual(self.itens.nome, 'Água')
        self.assertEqual(self.itens.pontos, 5)


class InventarioModelTestCase(TestCase):
    
    
    def setUp(self):

        self.itens  = Itens(
            nome = 'Água'
        )

        self.sobrevivente = Sobrevivente(
            nome = 'José'
        )

        self.inventario = SobreviventeInventario(
            item = self.itens,
            sobrevivente = self.sobrevivente,
            quantidade = 7
        )

    def test_verifica_atributos_de_inventario(self):
        """Teste que verifica os atributos de um inventario"""
        self.assertEqual(self.inventario.item, 1)
        self.assertEqual(self.inventario.sobrevivente, 1)
        self.assertEqual(self.inventario.quantidade, 7)