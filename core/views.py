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
    form = PlanejamentoForm(request.POST)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Planejamento criado com sucesso!')
            form = PlanejamentoForm()
        else:
            messages.error(request, 'Erro ao criar o planejamento.')
    return render(request, 'planejamento.html', {
        'form': form
    })

def execucao(request):
    form = ExecucaoForm(request.POST)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Execução completa!')
            form = ExecucaoForm()
        else:
            messages.error(request, 'Erro na execução.')
    context = {
        'execucao': form
    }
    return render(request, 'execucao.html', context)

def estatisticas(request):

    return render(request, 'estatisticas.html')