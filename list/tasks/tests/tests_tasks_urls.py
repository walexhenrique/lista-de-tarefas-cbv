from unittest import TestCase

from django.urls import reverse


class TasksURLsTest(TestCase):
    def test_tasks_list_url_path_is_correct(self):
        url = reverse('tasks:painel')
        self.assertEqual(url, '/painel/')
