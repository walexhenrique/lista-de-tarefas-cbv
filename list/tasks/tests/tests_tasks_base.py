from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Tarefa


class TasksBaseTest(TestCase):
    def create_task(
        self,
        user: User = None,
        title: str = 'tarefa 1',
        finished: bool = False,
    ) -> Tarefa:
        return Tarefa.objects.create(title=title, finished=finished, user=user)
    
    def create_account(
        self,
        username: str = 'breno',
        email: str = 'breno@email.com',
        password: str = '123456'
    ) -> User:
        return User.objects.create_user(username=username, email=email, password=password)
