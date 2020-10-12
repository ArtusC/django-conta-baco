from django.db import models
from django.db.models import Sum, F, FloatField

# Create your models here.

class Transacoes(models.Model):

	class Meta:
		db_table = 'transacoes'

	debito = models.DecimalField(max_digits=19, decimal_places=2)
	descricao_debito = models.CharField(max_length=255)
	credito = models.DecimalField(max_digits=19, decimal_places=2)
	descricao_credito = models.CharField(max_length=255)