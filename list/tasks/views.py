from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from .models import Tarefa


class TarefaListView(View):
    def get(self, *args, **kwargs):
        tarefas = Tarefa.objects.filter(user=self.request.user)
        per_page = self.request.GET.get('per', '5')

        options_per_page = {
            '5': 5,
            '10': 10,
            '15': 15
        }

        # Get the correct value according to the dictionary of choices, if there is none, get the value 5 per page
        option_choice = options_per_page.get(per_page, 5)

        paginator = Paginator(tarefas, option_choice)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(self.request, 'tasks/tarefa_list.html', {'page_obj': page_obj})
