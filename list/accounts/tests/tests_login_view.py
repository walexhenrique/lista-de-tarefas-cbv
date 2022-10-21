from django.contrib.auth.models import User
from django.urls import reverse

from .tests_accounts_base import AccountsBaseTest


class LoginViewTest(AccountsBaseTest):
    """class responsible for testing all features of the login view"""
    def setUp(self) -> None:
        self.url = reverse('accounts:login')
        self.login_data = {
            'username': 'breno',
            'password': '123456',
        }
        return super().setUp()

    def test_login_view_returns_status_code_200_OK(self) -> None:
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_login_successfully_sign_in_with_a_valid_user(self) -> None:

        # Create a User
        self.create_account()
        response = self.client.post(self.url, data=self.login_data)

        # Redirects to dashboard, login worked
        self.assertRedirects(response, reverse('tasks:painel'))
    
    def test_login_username_does_not_belong_to_any_user_must_not_login(self) -> None:

        # Create a User
        self.create_account()
        self.login_data['username'] = 'veronica'

        response = self.client.post(self.url, data=self.login_data)

        # Login redirect to the same view
        self.assertRedirects(response, self.url)
    
    def test_login_if_the_password_is_not_correct_the_login_should_not_work(self) -> None:

        # Create a User
        self.create_account()
        self.login_data['password'] = 'abc123'
        
        response = self.client.post(self.url, data=self.login_data)

        # Login redirect to the same view
        self.assertRedirects(response, self.url)

    def test_login_view_redirects_if_user_logged_alredy(self) -> None:

        self.create_account()
        self.client.login(username='breno', password='123456')
        response = self.client.get(self.url)

        self.assertRedirects(response, '/painel/')
        self.assertEqual(response.status_code, 302)

