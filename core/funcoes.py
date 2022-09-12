import time 

def converter(seconds): 
    tempo = time.strftime("%H:%M:%S", time.gmtime(seconds))
    return tempo

def converter_humano(tempo):
    horas, minutos, segundos = tempo.split(':')

    if int(horas) < 1:
        horas = ''
    elif int(horas) == 1:
        horas = horas + ' hora' + ', '
    else:
        horas = horas + ' horas' + ', '

    if int(minutos) < 1:
        minutos = ''
    elif int(minutos) == 1:
        minutos = minutos + ' minuto' + ', '
    else:
        minutos = minutos + ' minutos' + ', '

    if int(segundos) < 1:
        segundos = ''
    elif int(segundos) == 1:
        segundos = segundos + ' segundo '
    else:
        segundos = segundos + ' segundos '

    return horas + minutos + segundos  

def calcular_estatisticas(planejamento_inicio, planejamento_termino, execucao_inicio, execucao_termino):
    
    delta_planejamento = planejamento_termino - planejamento_inicio
    delta_planejamento_convertido = converter(delta_planejamento.total_seconds())
    delta_planejamento_humano = converter_humano(delta_planejamento_convertido)

    delta_execucao = execucao_termino - execucao_inicio
    delta_execucao_convertido = converter(delta_execucao.total_seconds())
    delta_execucao_humano = converter_humano(delta_execucao_convertido)


    resultado = delta_planejamento - delta_execucao
    resultado_convertido = converter(resultado.total_seconds())
    #import ipdb; ipdb.set_trace()
    return delta_planejamento_convertido, delta_execucao_convertido, resultado_convertido 