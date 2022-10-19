from unittest import TestCase

from django.urls import reverse


class TasksURLsTest(TestCase):
    def test_tarefa_list_url_path_is_correct(self):
        url = reverse('tasks:painel')
        self.assertEqual(url, '/painel/')
    
    def test_tarefa_create_view_url_path_is_correct(self):
        url = reverse('tasks:create-tarefa')
        self.assertEqual(url, '/painel/criar-tarefa/')

    def test_tarefa_update_view_url_path_is_correct(self):
        url = reverse('tasks:update-tarefa', kwargs={'pk': 1})
        self.assertEqual(url, '/painel/editar-tarefa/1/')