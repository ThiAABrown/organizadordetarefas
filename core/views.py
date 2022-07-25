from cmath import e
from email import message_from_binary_file
from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

from .forms import PlanejamentoForm, ExecucaoForm
from .models import Planejamento, Execucao
from .funcoes import converter, converter_humano 

def index(request):
    context = {
        'planejamentos': Planejamento.objects.all()
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

def estatisticas_planejamento(request, planejamento_id, execucao_id):

    planejamento = Planejamento.objects.get(id=planejamento_id)
    execucao = Execucao.objects.get(id=execucao_id)

    delta_planejamento = planejamento.termino - planejamento.inicio
    delta_planejamento_convertido = converter(delta_planejamento.total_seconds())
    delta_planejamento_humano = converter_humano(delta_planejamento_convertido)

    delta_execucao = execucao.termino - execucao.inicio
    delta_execucao_convertido = converter(delta_execucao.total_seconds())
    delta_execucao_humano = converter_humano(delta_execucao_convertido)

    # import ipdb; ipdb.set_trace()

    resultado = delta_planejamento - delta_execucao
    resultado_convertido = converter(resultado.total_seconds())

    mensagem_inicio = f'O planejamento deveria iniciar as {planejamento.inicio}, porem foi iniciado as {execucao.inicio}.'
    mensagem_termino = f'O planejamento deveria terminar as {planejamento.termino}, porem foi finalizado as {execucao.termino}.'
    mensagem_tempo_total = f'Você planejou trabalhar/estudar {delta_planejamento_convertido}, porem trabalhou/estudou {delta_execucao_convertido}.' 
    mensagem_resultado = f'Você falhou no seu planejamento e deve organizar melhor o seu tempo. O tempo de estudo foi de {resultado_convertido}.'

    context = { 'mensagem_inicio': mensagem_inicio, 
    'mensagem_termino': mensagem_termino, 
    'mensagem_tempo_total': mensagem_tempo_total, 
    'mensagem_resultado': mensagem_resultado, }


    return render(request, 'estatisticas_planejamento.html', context)

def detalhes_planejamento(request, planejamento_id):

    context = {
        'planejamento': Planejamento.objects.get(id=planejamento_id)
    }
    return render(request, 'detalhes_planejamento.html', context)

def planejamentos_executados(request):
    context = {
        'execucao' : Execucao.objects.all()
        }
    return render(request, 'planejamentos_executados.html', context)
