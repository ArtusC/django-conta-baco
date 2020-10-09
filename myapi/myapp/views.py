from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Saldo, Transacoes
from .serializers import SaldoSerializer, TransacoesSerializer
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import django_filters.rest_framework
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics
from django.views import generic
from django.db.models import Sum, F, FloatField

class TransacoestList(generics.ListCreateAPIView):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer

class TransacoestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer

class UserListView(generics.ListAPIView):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ('debito', 'credito')
    #https://stackoverflow.com/questions/51977825/adding-sum-of-object-attributes-to-django-rest-framework-response
	#def get(self, request):
	#	"""List Transactions"""
	#	queryset = Transacoes.objects.all()
	#	serializer_class = TransacoesSerializer(queryset, many=True)
	#	all_sum = Transacoes.objects.aggregate(total=Sum(F('debito')-F('credito')), output_field=FloatField())['amount__sum']
	#	return Response({'sum':all_sum if all_sum else 0, 'objects':serializer_class.data})


@api_view(['GET'])
def SaldoList(request):
	queryset = Transacoes.objects.aggregate(total=Sum(F('debito')-F('credito'), output_field=FloatField()))
	return Response({'saldo':queryset})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'extrato': reverse('extrato-list', request=request, format=format),
        'transacoes': reverse('transacoes-list', request=request, format=format),
        'saldo': reverse('saldo-list', request=request, format=format),
    })       