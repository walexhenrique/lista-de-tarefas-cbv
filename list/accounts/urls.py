from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('registrar/', views.RegisterView.as_view(), name='register'),
    path('painel/', views.teste, name='painel')
]
