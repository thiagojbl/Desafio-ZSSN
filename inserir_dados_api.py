import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zssn.settings')
django.setup() 

import random

from faker import Faker

from api.models import Itens, Sobrevivente, SobreviventeInventario

fake = Faker('pt_BR')
Faker.seed(10)

def gerar_nome_sexo(op):
    if op: 
        return fake.name_female(), 'Feminino'
    else:
        return fake.name_male(), 'Masculino'
 
def criando_inventário(sobrevivente):
    itens = Itens.objects.all()
    for item in itens:
        si = SobreviventeInventario(sobrevivente=sobrevivente, item=item, quantidade=random.randrange(0,50))
        si.save()
    

def criando_sobreviventes(quantidade_de_pessoas=10):
    for i in range(quantidade_de_pessoas):
        random.seed(i)
        id_nome_sexo = random.randrange(0, 2)
        nome, sexo  = gerar_nome_sexo(id_nome_sexo)
        idade = "{}".format(random.randrange(15, 80)) 
        latitude = fake.latitude()
        longitude = fake.longitude()
        s = Sobrevivente(nome=nome,idade=idade, sexo=sexo, latitude=latitude, longitude=longitude)
        print('Nome: {},  Idade: {}, Sexo: {}, Latitude: {}, Longitude: {}'.format(nome, idade, sexo, latitude, longitude))
        s.save()
        criando_inventário(s)

def criando_itens():
    items_nome = ['Água', 'Alimentação', 'Medicação', 'Munição']
    itens_pontos = [4, 3, 2, 1] 
    for i in range(4):
        print('Nome: {}, Pontos: {}'.format(items_nome[i], itens_pontos[i]))
        i = Itens(nome=items_nome[i], pontos=itens_pontos[i])
        i.save()

# Povoando as tabelas Itens, Sobrevivente(defaul=20) e Inventário  
sobreviventes = Sobrevivente.objects.all()
itens = Itens.objects.all()
 
# Verificar se os itens já foram inseridos
if len(itens) < 4: 
    criando_itens()

# Verificar se já exitem sobreviventes (defaul=20)
qtd_sobreviventes = 4
if len(sobreviventes) < qtd_sobreviventes: 
    criando_sobreviventes(qtd_sobreviventes)
