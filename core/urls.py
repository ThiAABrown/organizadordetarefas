from django.urls import path

from .views import detalhes, index, planejamento, execucao, estatisticas

urlpatterns = [
    path('', index, name='index'),
    path('planejamento/', planejamento, name='planejamento'),
    path('execucao/', execucao, name='execucao'),
    path('estatisticas/', estatisticas, name='estatisticas'),
    path('detalhes/<int:id>/', detalhes, name='detalhes')
]