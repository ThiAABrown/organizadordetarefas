from django.contrib import admin

from core.models import Planejamento
from .models import Planejamento, Execucao

@admin.register(Planejamento)
class PlanejamentoAdmin(admin.ModelAdmin):
    list_display = ('inicio', 'termino', 'descricao', 'nome_planejamento')

@admin.register(Execucao)
class ExecucaoAdmin(admin.ModelAdmin):
    list_display = ('inicio', 'termino')
