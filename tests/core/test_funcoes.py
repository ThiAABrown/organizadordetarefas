from core.funcoes import calcular_estatisticas, converter, converter_humano
from datetime import datetime, timezone 


def test_calcular_estatisticas_ex1():
    # EX http://127.0.0.1:8000/estatisticas/12/6/
    parametro_planejamento_inicio = datetime(2022, 7, 11, 14, 0, tzinfo=timezone.utc)
    parametro_planejamento_termino = datetime(2022, 7, 11, 16, 0, tzinfo=timezone.utc)
    parametro_execucao_inicio = datetime(2022, 7, 11, 17, 30, tzinfo=timezone.utc)
    parametro_execucao_termino = datetime(2022, 7, 11, 18, 30, tzinfo=timezone.utc)

    calcularestatisticasex1 = calcular_estatisticas(parametro_planejamento_inicio, 
                                                    parametro_planejamento_termino, 
                                                    parametro_execucao_inicio, 
                                                    parametro_execucao_termino)

    delta_planejamento_convertido = '02:00:00'
    delta_execucao_convertido = '01:00:00'
    resultado_convertido = '01:00:00'

    retorno_esperado = (delta_planejamento_convertido, delta_execucao_convertido, resultado_convertido)

    assert calcularestatisticasex1 == retorno_esperado

# TODO: Criar um teste para a funcao calcular_estatisticas usando o ex: http://127.0.0.1:8000/estatisticas/4/2/

def test_converter_humano_ex1():
    converterhumanoex1 = converter_humano('00:00:15')
    assert converterhumanoex1 == '15 segundos '

def test_converter_humano_ex2():
    converterhumanoex2 = converter_humano('00:11:40')
    assert converterhumanoex2 == '11 minutos, 40 segundos '

def test_converter_humano_ex3():
    converterhumanoex3 = converter_humano('01:00:59')
    assert converterhumanoex3 == '01 hora, 59 segundos '

def test_converter_humano_ex4():
    converterhumanoex4 = converter_humano('01:15:59')
    assert converterhumanoex4 == '01 hora, 15 minutos, 59 segundos '

def test_converter_ex1():
    converterex1 = converter(15)
    assert converterex1=='00:00:15'

def test_converter_ex2():
    converterex2 = converter(700)
    assert converterex2=='00:11:40'
