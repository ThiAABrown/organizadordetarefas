from django.urls import path

from .views import detalhes_planejamento, index, criar_planejamento, executar_planejamento, estatisticas_planejamento, planejamentos_executados

urlpatterns = [
    path('', index, name='index'),
    path('planejamento/', criar_planejamento, name='criar_planejamento'),
    path('executar/<int:planejamento_id>/', executar_planejamento, name='executar_planejamento'),
    path('executados/', planejamentos_executados, name='planejamentos_executados'),
    path('estatisticas/<int:planejamento_id>/<int:execucao_id>/', estatisticas_planejamento, name='estatisticas_planejamento'),
    path('detalhes/<int:planejamento_id>/', detalhes_planejamento, name='detalhes_planejamento')
]