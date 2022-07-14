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

    planejamento_inicio = planejamento.inicio
    planejamento_termino = planejamento.termino

    execucao_inicio = execucao.inicio
    execucao_termino = execucao.termino

    delta_inicio = execucao_inicio - planejamento_inicio
    delta_inicio_convertido = converter(delta_inicio.total_seconds())
    delta_inicio_humano = converter_humano(delta_inicio_convertido)

    delta_termino = execucao_termino - planejamento_termino
    delta_termino_convertido = converter(delta_termino.total_seconds())
    delta_termino_humano = converter_humano(delta_termino_convertido)
    
    # import ipdb; ipdb.set_trace()

    mensagem_inicio = f'O planejamento deveria iniciar as {planejamento_inicio}, porem foi iniciado as {execucao_inicio}.'
    mensagem_termino = f'O planejamento deveria terminar as {planejamento_termino}, porem foi finalizado as {execucao_termino}.'
    mensagem_tempo_total = 'Você planejou trabalhar/estudar 2:00, porem trabalhou/estudou 1:00.'
    mensagem_resultado = 'Você falhou no seu planejamento e deve organizar melhor o seu tempo.'

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
