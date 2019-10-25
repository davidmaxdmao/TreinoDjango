from django.db import models

# Create your models here.
class Animal(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'nome: {self.nome}, especie: {self.especie}'