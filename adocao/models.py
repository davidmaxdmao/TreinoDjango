from django.db import models
from animais.models import Animal
# Create your models here.

class Adocao(models.Model):
    nome_do_responsavel = models.CharField(max_length=100, null=False, blank=False)
    animal = models.ForeignKey(Animal, null=False, blank=False, on_delete=models.PROTECT)

