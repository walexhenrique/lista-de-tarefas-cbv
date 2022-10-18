from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from .forms.form_login import LoginForm


class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, 'accounts/login.html', {'form': form})
    
    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            if user:
                login(self.request, user)
                return redirect('accounts:painel')
        
        return redirect('accounts:login')

def teste(request):
    return HttpResponse('testando painel')
