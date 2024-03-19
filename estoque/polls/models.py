from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

cimatec1 = 'CIMATEC 01'
cimatec2 = 'CIMATEC 02'
cimatec3 = 'CIMATEC 03'
cimatec4 = 'CIMATEC 05'

class Estoque(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    retirada = models.IntegerField(default=0)
    estoque = models.IntegerField()
    data_estoque = models.DateTimeField(default=timezone.now)
    sala_laboratorio = models.CharField(max_length=100, blank=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f'{self.nome}'

    def save(self, *args, **kwargs):
        # Subtrai o valor de retirada do estoque
        self.estoque -= self.retirada
        super().save(*args, **kwargs)

class Estoque_da_at(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    retirada = models.IntegerField(default=0)
    estoque = models.IntegerField()
    data_estoque = models.DateTimeField(default=timezone.now)
    sala_laboratorio = models.CharField(max_length=100, blank=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f'{self.nome}'

    def save(self, *args, **kwargs):
        # Subtrai o valor de retirada do estoque
        self.estoque -= self.retirada
        super().save(*args, **kwargs)