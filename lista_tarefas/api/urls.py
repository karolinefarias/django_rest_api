from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_tarefa, name='add-tarefa'),
    path('all/', views.view_tarefas, name='view_tarefas'),
    path('update/<int:pk>/', views.update_tarefa, name='update-tarefa'),
    path('delete/<int:pk>/', views.delete_tarefa, name='delete-tarefa'),
]