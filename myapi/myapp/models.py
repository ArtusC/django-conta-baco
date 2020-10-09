from django.db import models
from django.db.models import Sum, F, FloatField

# Create your models here.

class Transacoes(models.Model):

	class Meta:
		db_table = 'transacoes'

	debito = models.DecimalField(max_digits=19, decimal_places=2)
	credito = models.DecimalField(max_digits=19, decimal_places=2)

	@property
	def sum(self):
		return float(self.debito) - float(self.credito)

	saldoTrans = property(sum)


class Saldo(models.Model):

	class Meta:

		db_table = 'saldo'

	#saldo = Transacoes.sum()
	#saldo = models.DecimalField(max_digits=19, decimal_places=2)
	#saldo_data = models.DateTimeField(blank=True, null=True)