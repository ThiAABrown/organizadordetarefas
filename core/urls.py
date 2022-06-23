from django.urls import path

from .views import detalhes_planejamento, index, criar_planejamento, executar_planejamento, estatisticas_planejamento, planejamentos_executados

urlpatterns = [
    path('', index, name='index'),
    path('planejamento/', criar_planejamento, name='planejamento'),
    path('executar/<int:planejamento_id>/', executar_planejamento, name='executar'),
    path('executado/', planejamentos_executados, name='executado'),
    path('estatisticas/', estatisticas_planejamento, name='estatisticas'),
    path('detalhes/<int:planejamento_id>/', detalhes_planejamento, name='detalhes')
]