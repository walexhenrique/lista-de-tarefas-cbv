from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import TarefaForm
from .models import Tarefa


@method_decorator(login_required, name='dispatch')
class TarefaDeleteView(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('tasks:painel')
    template_name = 'tasks/tarefa_delete.html'
    context_object_name = 'tarefa'

    def get(self, request, *args, **kwargs):
        tarefa = get_object_or_404(Tarefa, pk=self.kwargs.get('pk'), user=self.request.user)
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Tarefa excluida com sucesso')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TarefaCreateView(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tasks/tarefa_create.html'
    success_url = reverse_lazy('tasks:painel')

    def form_valid(self, form):
        form_edit = form.save(commit=False)
        form_edit.user = self.request.user
        form_edit.save()
        messages.success(self.request, 'Tarefa criada com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tasks/tarefa_update.html'
    success_url = reverse_lazy('tasks:painel')

    def get(self, request, *args, **kwargs):
        tarefa = get_object_or_404(Tarefa, pk=self.kwargs.get('pk'), user=self.request.user)
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Tarefa atualizada com sucesso')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível atualizar essa tarefa')
        return super().form_invalid(form)
    
@method_decorator(login_required, name='dispatch')
class TarefaListView(View):
    def get(self, *args, **kwargs):
        tarefas = Tarefa.objects.filter(user=self.request.user).order_by('-id')
        limits = ['5', '10', '15']

        limit = self.request.GET.get('limit', '5')
        if not limit in limits:
            limit = limits[0]

        paginator = Paginator(tarefas, limit)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(self.request, 'tasks/tarefa_list.html', {
            'page_obj': page_obj, 
            'quantity_per_page': limits, 
            'limit': limit
            }
        )
