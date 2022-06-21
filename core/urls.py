from django.urls import path

from .views import detalhes, index, planejamento, execucao, estatisticas, executado

urlpatterns = [
    path('', index, name='index'),
    path('planejamento/', planejamento, name='planejamento'),
    path('execucao/<int:planejamento_id>/', execucao, name='execucao'),
    path('executado/', executado, name='executado'),
    path('estatisticas/', estatisticas, name='estatisticas'),
    path('detalhes/<int:planejamento_id>/', detalhes, name='detalhes')
]