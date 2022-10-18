from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from .forms.form_login import LoginForm
from .forms.form_register import RegisterForm


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


class RegisterView(View):
    def get(self, *args, **kwargs):
        data_session = self.request.session.get('register_data')
        form = RegisterForm(data_session)
        return render(self.request, 'accounts/register.html', {'form': form})
    
    def post(self, *args, **kwargs):
        POST = self.request.POST
        self.request.session['register_data'] = POST
        
        form = RegisterForm(POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            del(self.request.session['register_data'])

            return redirect('accounts:login')

        return redirect('accounts:register')

def teste(request):
    return HttpResponse('testando painel')
