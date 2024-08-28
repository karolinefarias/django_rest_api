from django.db.models import fields
from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('titulo', 'descricao', 'status', 'data_criacao')
        