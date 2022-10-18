from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    username = forms.CharField(
        max_length=120,
        label='Nome de usuário',
        error_messages={
            'max_length': 'Credenciais inválidas',
        },
        widget=forms.TextInput(attrs={'placeholder': 'John..'})
    )

    password = forms.CharField(
        max_length=150,
        label='Senha',
        error_messages={
            'max_length': 'Credenciais inválidas',
        },
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha...'})
    )

