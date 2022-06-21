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
    
def planejamento(request):
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
    return render(request, 'planejamento.html', context)

def execucao(request, planejamento_id):
    form = ExecucaoForm()
    if str(request.method) == 'POST':
        form = ExecucaoForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Execução completa!')
            form = ExecucaoForm()
        else:
            messages.error(request, 'Erro na execução.')
    context = {
        'form_execucao': form, 'planejamento_id': planejamento_id 
    }
    return render(request, 'execucao.html', context)

def estatisticas(request):

    return render(request, 'estatisticas.html')

def detalhes(request, planejamento_id):

    context = {
        'planejamento': Planejamento.objects.get(id=planejamento_id)
    }
    return render(request, 'detalhes_plan.html', context)

def executado(request):
    context = {}
    return render(request, 'executado.html', context)
