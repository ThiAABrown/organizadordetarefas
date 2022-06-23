from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages

from .forms import PlanejamentoForm, ExecucaoForm
from .models import Planejamento, Execucao

def index(request):
    context = {
        'planejamento': Planejamento.objects.all()
    }
    return render(request, 'index.html', context)
    
def criar_planejamento(request):
    form = PlanejamentoForm()
    if str(request.method) == 'POST':
        form = PlanejamentoForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Planejamento criado com sucesso!')
            form = PlanejamentoForm()
        else:
            messages.error(request, 'Erro ao criar o planejamento.')
    context = {
        'form_planejamento': form
    }
    return render(request, 'criar_planejamento.html', context)

def executar_planejamento(request, planejamento_id):
    form = ExecucaoForm()
    if str(request.method) == 'POST':
        form = ExecucaoForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Você realizou um planejamento com sucesso!')
            form = ExecucaoForm()
        else:
            messages.error(request, 'Erro ao executar o planejamento.')
    context = {
        'form_execucao': form, 'planejamento_id': planejamento_id 
    }
    return render(request, 'executar_planejamento.html', context)

def estatisticas_planejamento(request):

    return render(request, 'estatisticas_planejamento.html')

def detalhes_planejamento(request, planejamento_id):

    context = {
        'planejamento': Planejamento.objects.get(id=planejamento_id)
    }
    return render(request, 'detalhes_planejamento.html', context)

def planejamentos_executados(request):
    context = {}
    return render(request, 'planejamentos_executados.html', context)
