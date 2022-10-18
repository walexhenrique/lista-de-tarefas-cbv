from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('painel/', views.TarefaListView.as_view(), name='painel' )
]
