from .models import Transacoes
from .serializers import TransacoesSerializer, DebCredSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from django.db.models import Sum, F, FloatField
from rest_framework import filters
import django_filters

#POST e GET de debito e credito
class TransacoestList(generics.ListCreateAPIView):
    queryset = Transacoes.objects.all()
    serializer_class = DebCredSerializer

#GET, PUT e DELETE dos debitos e creditos
class TransacoestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer

#GET dos debitos, creditos e saldo por transação e filtro de ordenação
class UserListView(generics.ListAPIView):
	def get_queryset(self):
		return Transacoes.objects.annotate(saldo=F('credito')-F('debito'))	
	queryset = Transacoes.objects.all()
	serializer_class = TransacoesSerializer
	filter_backends = [filters.OrderingFilter]
	ordering_fields  = ('debito', 'credito')		

#GET do saldo total
@api_view(['GET'])
def SaldoList(request):
	queryset = Transacoes.objects.aggregate(total=Sum(F('credito')-F('debito'), output_field=FloatField()))
	return Response({'saldo':queryset})

#ROOT da pagina inicial
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
    	'Realizar Débito e Crédito': reverse('transacoes-list', request=request, format=format),
        'Extrato': reverse('extrato-list', request=request, format=format),
        'Saldo total': reverse('saldo-list', request=request, format=format),
    })       