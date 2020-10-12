from rest_framework import serializers
from .models import Transacoes

#Serializer utilizado para o GET
class TransacoesSerializer(serializers.ModelSerializer):
	saldo = serializers.IntegerField()
	class Meta:
		model = Transacoes
		fields = ('credito', 'descricao_credito', 'debito', 'descricao_debito', 'saldo')

#Serializer utilizado para o POST
class DebCredSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transacoes
		fields = ('credito', 'descricao_credito', 'debito', 'descricao_debito')		