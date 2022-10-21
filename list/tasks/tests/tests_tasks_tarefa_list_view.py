from django.contrib.auth.models import User
from django.urls import reverse

from .tests_tasks_base import TasksBaseTest


class TarefaListViewTest(TasksBaseTest):
    def setUp(self) -> None:
        self.url = reverse('tasks:painel')
        return super().setUp()
    
    def create_and_login(self) -> User:
        user = self.create_account()
        self.client.login(username='breno', password='123456')
        return user
    
    def create_generic_pagination(self, per_page: int = 5):
        """simulates pagination according to the amount per page"""
        user = self.create_and_login()
        self.client.login(username='breno', password='123456')

        self.create_multiple_tasks(user, quantity=per_page+5)
        
        response = self.client.get(self.url + f'?limit={per_page}')
        return response
    
    def create_multiple_tasks(self, user: User, quantity: int = 10):
        for i in range(quantity):
            self.create_task(user, title=f'tarefa {i}', finished=False)
        
    def test_tarefa_list_view_returns_status_code_200_OK(self) -> None:
        self.create_and_login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_tarefa_list_view_pagination_works_correctly_on_the_5_per_page_option(self) -> None:
        
        response = self.create_generic_pagination()
        self.assertEqual(len(response.context['page_obj']), 5)
    
    def test_tarefa_list_view_pagination_works_correctly_on_the_10_per_page_option(self) -> None:
        response = self.create_generic_pagination(10)
        self.assertEqual(len(response.context['page_obj']), 10)
    
    def test_tarefa_list_view_pagination_works_correctly_on_the_15_per_page_option(self) -> None:
        response = self.create_generic_pagination(15)
        self.assertEqual(len(response.context['page_obj']), 15)
    
    def test_tarefa_list_view_pagination_works_correctly_with_5_tasks_per_page_if_the_number_passed_is_not_allowed(self) -> None:
        response = self.create_generic_pagination(32)
        self.assertEqual(len(response.context['page_obj']), 5)
    
    def test_tarefa_list_view_pagination_works_correctly_showing_the_tasks_of_a_given_page(self) -> None:
        """Checks if pagination is correct, ordering is inverse by id"""
        user = self.create_and_login()
        self.client.login(username='breno', password='123456')

        self.create_multiple_tasks(user, quantity=10)
        
        response = self.client.get(self.url + f'?page=2')
        self.assertIn('tarefa 4', response.content.decode('utf-8'))
        self.assertNotIn('tarefa 5', response.content.decode('utf-8'))

