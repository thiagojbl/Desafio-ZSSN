from django.db import models

class Itens(models.Model):
    nome = models.CharField('Nome', max_length=50)
    pontos = models.IntegerField('Pontos', blank=True, null=True)

    def __str__(self):
        return self.nome


class Sobrevivente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    idade = models.IntegerField('Idade')
    sexo = models.CharField("Sexo", max_length=15)
    latitude = models.CharField("Latitude", max_length=50)
    longitude = models.CharField("Longitude", max_length=50)
    infectado = models.BooleanField("Infectado", default=False)

    def __str__(self):
        return self.nome
