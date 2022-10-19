from django import forms

from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('title', 'finished')
    
    title = forms.CharField(
        max_length=120,
        label='Titulo da tarefa',
        error_messages={
            'max_length': 'Erro, o titulo da tarefa deve ter no máximo 120 caracteres'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Titulo...'
        })
    )

    finished = forms.BooleanField(
        label='Finalizado',
        required=False,
    )
