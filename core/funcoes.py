import time 

def converter(seconds): 
    tempo = time.strftime("%H:%M:%S", time.gmtime(seconds))
    return tempo

def converter_humano(tempo):
    horas, minutos, segundos = tempo.split(':')
    return horas + ' horas, ' + minutos + ' minutos e ' + segundos + ' segundos '
