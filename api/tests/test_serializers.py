from django.test import TestCase
from api.models import Sobrevivente, Itens, SobreviventeInventario
from api.serializers import SobreviventeSerializer, ItensSerializer, InventarioSerializer

# Teste de Unidade utilizando o TestCase - Não precisa salvar no banco de dados
class SobreviventeSerializerTestCase(TestCase):

    def setUp(self):
        self.sobrevivente = Sobrevivente(
            nome = 'José',
            idade = 25,
            sexo = 'Masculino',
            latitude = '0384756',
            longitude = '9384756', 
            # infectado = default(False)
        )

        self.serializer = SobreviventeSerializer(instance=self.sobrevivente)

    def test_verifica_campos_serializados_sobrevivente(self):
        """Teste que verifica os campos que estão sendo serializados (sobrevivente)"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'idade', 'sexo', 'latitude', 'longitude', 'infectado', 'inventario']))

    def test_verifica_conteudo_dos_campos_serializados_sobrevivente(self):
        """Teste que verifica o conteúdo dos campos serializados(sobrevivente)"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.sobrevivente.nome)
        self.assertEqual(data['idade'], self.sobrevivente.idade)
        self.assertEqual(data['sexo'], self.sobrevivente.sexo)
        self.assertEqual(data['latitude'], self.sobrevivente.latitude)
        self.assertEqual(data['longitude'], self.sobrevivente.longitude)
        self.assertEqual(data['infectado'], self.sobrevivente.infectado)
        # print(f'\n\nSobrevivente infectado ? {self.sobrevivente.infectado}')

class ItensSerializerTestCase(TestCase):

    def setUp(self):
        self.itens = Itens(
            nome = 'Água',
            pontos = 5
        )

        self.serializer = ItensSerializer(instance=self.itens)

    def test_verifica_campos_serializados_itens(self):
        """Teste que verifica os campos que estão sendo serializados (itens)"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'pontos']))

    def test_verifica_conteudo_dos_campos_serializados_itens(self):
        """Teste que verifica o conteúdo dos campos serializados(itens)"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.itens.nome)
        self.assertEqual(data['pontos'], self.itens.pontos)


class InventarioSerializerTestCase(TestCase):

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


        self.serializer = InventarioSerializer(instance=self.inventario)

    def test_verifica_campos_serializados_inventario(self):
        """Teste que verifica os campos que estão sendo serializados (inventario)"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'item', 'sobrevivente', 'quantidade']))

    def test_verifica_conteudo_dos_campos_serializados_inventario(self):
        """Teste que verifica o conteúdo dos campos serializados(inventario)"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.inventario.pk)
        self.assertEqual(data['item'], self.itens.pk)
        self.assertEqual(data['sobrevivente'], self.sobrevivente.pk)
        self.assertEqual(data['quantidade'], self.inventario.quantidade)




