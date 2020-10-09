from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('', views.api_root),
    path('transacoes/', views.TransacoestList.as_view(), name='transacoes-list'),
    path('transacoes/<int:pk>/', views.TransacoestDetail.as_view()),
    path('extrato/', views.UserListView.as_view(), name='extrato-list'),
    path('saldo/', views.SaldoList, name='saldo-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


'''
urlpatterns = [
    path('transacoes/', views.transacoes_list),
    path('saldo/<int:pk>/', views.saldo_detail),
]
'''