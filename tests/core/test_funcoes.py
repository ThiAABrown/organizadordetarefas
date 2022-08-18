from core.funcoes import calcular_estatisticas, converter, converter_humano

def test_calcular_estatisticas():
    # TODO: Criar um teste para a funcao calcular_estatisticas usando o ex: http://127.0.0.1:8000/estatisticas/12/6/
    assert 1==1

def test_converter_humano_ex1():
    converterhumanoex1 = converter_humano('00:00:15')
    assert converterhumanoex1 == '00 horas, 00 minutos e 15 segundos '

def test_converter_humano_ex2():
    converterhumanoex2 = converter_humano('00:11:40')
    assert converterhumanoex2 == '00 horas, 11 minutos e 40 segundos '

def test_converter_humano_ex3():
    converterhumanoex3 = converter_humano('01:15:59')
    assert converterhumanoex3 == '01 horas, 15 minutos e 59 segundos '

def test_converter_ex1():
    converterex1 = converter(15)
    assert converterex1=='00:00:15'

def test_converter_ex2():
    converterex2 = converter(700)
    assert converterex2=='00:11:40'
