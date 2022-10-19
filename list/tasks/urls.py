from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TarefaListView.as_view(), name='painel'),
    path('criar-tarefa/', views.TarefaCreateView.as_view(), name='create-tarefa'),
]
