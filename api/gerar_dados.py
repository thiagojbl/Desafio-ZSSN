import random

from faker import Faker

fake = Faker('pt_BR') 
 

def gerar_nome_sexo(op):
    if op: 
        return fake.name_female(), 'Feminino'
    else:
        return fake.name_male(), 'Masculino'


def sobrevivente(seed=1):
    Faker.seed(seed)
    random.seed(seed)
    id_nome_sexo = random.randrange(0, 2)
    nome,  sexo = gerar_nome_sexo(id_nome_sexo)
    idade = "{}".format(random.randrange(15, 80)) 
    latitude = fake.latitude()
    longitude = fake.longitude()
    return {'nome': nome, 'idade': idade, 'sexo': sexo, 
    'latitude': latitude, 'longitude': longitude} 
