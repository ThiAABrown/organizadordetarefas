import time 

def converter(seconds): 
    tempo = time.strftime("%H:%M:%S", time.gmtime(seconds))
    return tempo

def converter_humano(tempo):
    horas, minutos, segundos = tempo.split(':')
    if int(horas) < 1:
        return minutos + ' minutos e ' + segundos + ' segundos '

    elif int(horas) >= 1 and int(minutos) < 1:
        return horas + ' horas e ' + segundos + ' segundos '

    else:
        return horas + ' horas, ' + minutos + ' minutos e ' + segundos + ' segundos '

def calcular_estatisticas(planejamento_inicio, planejamento_termino, execucao_inicio, execucao_termino):
    
    delta_planejamento = planejamento_termino - planejamento_inicio
    delta_planejamento_convertido = converter(delta_planejamento.total_seconds())
    delta_planejamento_humano = converter_humano(delta_planejamento_convertido)

    delta_execucao = execucao_termino - execucao_inicio
    delta_execucao_convertido = converter(delta_execucao.total_seconds())
    delta_execucao_humano = converter_humano(delta_execucao_convertido)

    # import ipdb; ipdb.set_trace()

    resultado = delta_planejamento - delta_execucao
    resultado_convertido = converter(resultado.total_seconds())

    return delta_planejamento_convertido, delta_execucao_convertido, resultado_convertido