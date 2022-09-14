from django.test import TestCase
from api.models import Sobrevivente, Itens, SobreviventeInventario, Sinalizar, Negociar

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
        self.sobrevivente = Sobrevivente(
            nome = 'José',
            idade = 25,
            sexo = 'Masculino',
            latitude = '0384756',
            longitude = '9384756', 
            # infectado = default(False)
        )

        self.itens = Itens(
            nome = 'Água',
            pontos = 5
        )


        self.inventario = SobreviventeInventario(
            item = self.itens,
            sobrevivente = self.sobrevivente,
            quantidade = 25,
        )

    def test_verifica_atributos_de_inventario(self):
        """Teste que verifica os atributos de um inventario"""
        self.assertEqual(self.inventario.item.pk, self.itens.pk)
        self.assertEqual(self.inventario.sobrevivente.pk, self.sobrevivente.pk)
        self.assertEqual(self.inventario.quantidade, 25)

class SinalizarModelTestCase(TestCase):    
    
    def setUp(self):
        self.sobrevivente = Sobrevivente(
            nome = 'João',
            idade = 20,
            sexo = 'Masculino',
            latitude = '09876',
            longitude = '67890', 
            # infectado = default(False)
        )

        self.sobrevivente_infectato = Sobrevivente(
            nome = 'José',
            idade = 25,
            sexo = 'Masculino',
            latitude = '0384756',
            longitude = '9384756', 
            # infectado = default(False)
        )

        self.sinalizar = Sinalizar(
            sobrevivente = self.sobrevivente,
            sobrevivente_infectado = self.sobrevivente_infectato,
        )

    def test_verifica_atributos_de_sinalizar(self):
        """Teste que verifica os atributos de um sinalizar"""
        self.assertEqual(self.sinalizar.sobrevivente.pk, self.sobrevivente.pk)
        self.assertEqual(self.sinalizar.sobrevivente_infectado.pk, self.sobrevivente_infectato.pk)


class NegociarModelTestCase(TestCase):    
    
    def setUp(self):
        self.sobrevivente1 = Sobrevivente(
            nome = 'João',
            idade = 20,
            sexo = 'Masculino',
            latitude = '09876',
            longitude = '67890', 
            # infectado = default(False)
        )

        self.sobrevivente2 = Sobrevivente(
            nome = 'José',
            idade = 25,
            sexo = 'Masculino',
            latitude = '0384756',
            longitude = '9384756', 
            # infectado = default(False)
        )

        self.negociar = Negociar(
            sobrevivente1 = self.sobrevivente1,
            sobrevivente2 = self.sobrevivente2,
        )

    def test_verifica_atributos_de_sinalizar(self):
        """Teste que verifica os atributos de um sinalizar"""
        self.assertEqual(self.negociar.sobrevivente1.pk, self.sobrevivente1.pk)
        self.assertEqual(self.negociar.sobrevivente2.pk, self.sobrevivente2.pk)

    