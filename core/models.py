from django.db import models

class Planejamento(models.Model):
    nome_planejamento = models.CharField('Nome do Planejamento', max_length=100,)
    inicio = models.DateTimeField('Inicio', )
    termino = models.DateTimeField('Termino', )
    descricao = models.CharField('Descrição', max_length=2000,)

    def __str__(self):
        return self.nome_planejamento

class Execucao(models.Model):
    inicio = models.DateTimeField('Inicio', )
    termino = models.DateTimeField('Termino', )

    planejamento = models.OneToOneField('Planejamento', on_delete=models.CASCADE,)