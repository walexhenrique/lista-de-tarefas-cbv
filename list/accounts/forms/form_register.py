from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    username = forms.CharField(
        max_length=120,
        label='Nome de usuário',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: John'
            }
        ),
        error_messages = {
            'max_length': 'Erro, nome de usuário muito longo.',
            'min_length': 'Erro, nome de usuário precisa de mais de 5 caracteres.',
        },
        min_length=5,
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs = {
                'placeholder': 'Ex.: bruno@email.com'
            }
        ),
    )
    
    password = forms.CharField(
        max_length=150,
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha...'
            }
        ),
        error_messages={
            'max_length': 'Erro, sua senha é muito longa',
            'min_length': 'Erro, sua senha é muito curta',
        },
        min_length=4,
    )
    
    password2 = forms.CharField(
        max_length=150,
        label='Repita sua senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita sua senha...'}),
        error_messages= {
            'max_length': 'Erro, sua senha é muito longa.',
            'min_length': 'Erro, sua senha é muito curta',
        },
        min_length=4
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise ValidationError('Erro, email já utilizado')
        
        return email

    def clean(self):
        super().clean()

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError('Erro, as senhas não correspondem')
