from django.test import TestCase
from django.urls import reverse


class LoginViewTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('accounts:login')
        return super().setUp()

    def test_login_view_returns_status_code_200_OK(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
