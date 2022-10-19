from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import TarefaForm
from .models import Tarefa


class TarefaDeleteView(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('tasks:painel')
    template_name = 'tasks/tarefa_delete.html'
    context_object_name = 'tarefa'


class TarefaCreateView(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tasks/tarefa_create.html'
    success_url = reverse_lazy('tasks:painel')

    def form_valid(self, form):
        form_edit = form.save(commit=False)
        form_edit.user = self.request.user
        form_edit.save()
        return super().form_valid(form)


class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tasks/tarefa_update.html'
    success_url = reverse_lazy('tasks:painel')

    def get(self, request, *args, **kwargs):
        tarefa = get_object_or_404(Tarefa, pk=self.kwargs.get('pk'), user=self.request.user)
        return super().get(request, *args, **kwargs)


class TarefaListView(View):
    def get(self, *args, **kwargs):
        tarefas = Tarefa.objects.filter(user=self.request.user).order_by('-id')
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
