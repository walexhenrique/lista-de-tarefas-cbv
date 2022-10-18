from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'accounts/login.html')
