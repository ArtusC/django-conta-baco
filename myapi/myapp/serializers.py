from rest_framework import serializers
from .models import Saldo, Transacoes

class SaldoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Saldo
		fields = '__all__'

class TransacoesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transacoes
		fields = '__all__'