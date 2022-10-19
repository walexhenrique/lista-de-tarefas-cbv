from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TarefaListView.as_view(), name='painel'),
    path('criar-tarefa/', views.TarefaCreateView.as_view(), name='create-tarefa'),
    path('editar-tarefa/<int:pk>/', views.TarefaUpdateView.as_view(), name='update-tarefa'),
    path('apagar-tarefa/<int:pk>/', views.TarefaDeleteView.as_view(), name='delete-tarefa'),
]
