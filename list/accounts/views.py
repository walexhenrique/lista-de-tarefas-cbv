from django.shortcuts import render
from django.views import View

from .forms.form_login import LoginForm


class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, 'accounts/login.html', {'form': form})
