from django import forms
from dataclasses import fields

from .models import Planejamento, Execucao

class PlanejamentoForm(forms.ModelForm):
    class Meta:
        model = Planejamento
        fields = ('nome_planejamento', 'inicio', 'termino', 'descricao')

class ExecucaoForm(forms.ModelForm):
    class Meta:
        model = Execucao
        fields = ('inicio', 'termino')