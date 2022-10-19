from django.contrib.auth.models import User
from django.urls import reverse

from ..models import Tarefa
from .tests_tasks_base import TasksBaseTest


class TarefaCreateViewTest(TasksBaseTest):
    def setUp(self) -> None:
        self.url = reverse('tasks:create-tarefa')
        self.form_data = {
            'title': 'Titulo tarefa 1',
        }
        return super().setUp()

    def test_tarefa_create_view_returns_status_code_200_OK(self) -> None:
        self.create_account()
        self.client.login(username='breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_tarefa_create_view_checks_if_the_registered_task_was_saved_in_the_database_correctly(self):
        user = self.create_account()
        self.client.login(username='breno', password='123456')

        response = self.client.post(self.url, data=self.form_data, follow=True)
        self.assertRedirects(response, reverse('tasks:painel'))
        
        tarefa_exists = Tarefa.objects.filter(user=user).exists()
        self.assertTrue(tarefa_exists)

    def test_tarefa_create_view_should_not_create_a_new_task_if_the_task_title_is_longer_than_120_characters(self):
        user = self.create_account()
        self.client.login(username='breno', password='123456')
        self.form_data['title'] = 'A'*121

        self.client.post(self.url, data=self.form_data, follow=True)
        
        tarefa_exists = Tarefa.objects.filter(user=user).exists()
        self.assertFalse(tarefa_exists)




