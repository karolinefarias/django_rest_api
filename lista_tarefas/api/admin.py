from django.contrib import admin
from .models import Tarefa

class Tarefas(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'status', 'data_criacao']
    search_fields = ['titulo', 'status', 'data_criacao']
    list_filter = ['status', 'data_criacao']

admin.site.register(Tarefa, Tarefas)

