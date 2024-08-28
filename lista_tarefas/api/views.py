from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'All Tasks': '/all',
        'Search by titulo': '/?titulo=titulo_name',
        'Search by data_criacao': '/?data_criacao=yyyy-mm-dd',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/tarefa/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_tarefa(request):
    tarefa = TarefaSerializer(data=request.data)

    if tarefa.is_valid():
        tarefa.save()
        return Response(tarefa.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tarefas(request):
    # checking for the parameters from the URL
    if request.query_params:
        tarefas = Tarefa.objects.filter(**request.query_params.dict())
    else:
        tarefas = Tarefa.objects.all()
 
    # if there is something in items else raise error
    if tarefas:
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_tarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa_serialized = TarefaSerializer(instance=tarefa, data=request.data)

    if tarefa_serialized.is_valid():
        tarefa_serialized.save()
        return Response(tarefa_serialized.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return Response(status=status.HTTP_202_ACCEPTED)