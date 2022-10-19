from django.urls import reverse

from .tests_tasks_base import TasksBaseTest


class TarefaUpdateViewTest(TasksBaseTest):
    def setUp(self) -> None:
        self.url = reverse('tasks:update-tarefa', kwargs={'pk': 1})
        return super().setUp()

    def test_tarefa_update_view_returns_status_code_200_OK(self) -> None:
        user = self.create_account()
        self.create_task(user)
        self.client.login(username='breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_tarefa_update_view_returns_404_if_task_does_not_exists(self) -> None:
        self.create_account()
        self.client.login(username='breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
    
    def test_tarefa_update_view_returns_404_if_the_task_is_not_for_the_logged_in_user(self) -> None:
        self.create_account()
        self.client.login(username='breno', password='123456')

        user2 = self.create_account(username='magali', email='magali@email.com')
        self.create_task(user2)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
    
    def test_tarefa_update_view_does_not_update_task_if_title_is_longer_than_120_characters(self) -> None:
        user = self.create_account()
        self.client.login(username='breno', password='123456')

        self.create_task(user)

        form_data = {
            'title': 'A' * 121,
        }

        response = self.client.post(self.url, data=form_data)
        self.assertContains(response, 'Erro, o titulo da tarefa deve ter no máximo 120 caracteres')


