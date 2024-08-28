from django.db import models

# Create your models here.
class Tarefa(models.Model):
    status_choices = [('P', 'Pendente'),
                      ('A', 'Em andamento'),
                      ('C', 'Concluido')]
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=status_choices, default='P')
    data_criacao = models.DateField()

    def __str__(self):
        return self.titulo

# class StatusTarefa(ChoiceEnum):
#     PENDENTE = 'pendente'
#     EM_ANDAMENTO = 'em_andamento'
#     CONCLUIDO = 'concluido'

# class Tarefa(models.Model):
#     titulo = models.CharField(max_length=255)
#     descricao = models.TextField()
#     status = EnumChoiceField(StatusTarefa, default=StatusTarefa.PENDENTE)
#     data_criacao = models.DateField()

#     def __str__(self) -> str:
#         return self.name


