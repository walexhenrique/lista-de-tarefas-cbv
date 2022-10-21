from django.contrib.auth.models import User
from django.urls import reverse

from .tests_accounts_base import AccountsBaseTest


class RegisterViewTest(AccountsBaseTest):
    """class responsible for essential tests for the operation of the view register"""
    def setUp(self) -> None:
        self.url = reverse('accounts:register')
        self.form_data = {
            'username': 'breno',
            'email': 'breno@email.com',
            'password': '123456',
            'password2': '123456',
        }
        return super().setUp()

    def test_register_view_successfully_returns_status_code_200_OK(self) -> None:
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
    
    def test_register_view_is_working_properly_when_the_data_is_right(self) -> None:
        response = self.client.post(self.url, self.form_data)

        user_exists = User.objects.filter(pk=1).exists()
        self.assertTrue(user_exists)

        self.assertRedirects(response, '/')
    
    def test_register_view_registry_should_not_create_user_if_passwords_do_not_match(self) -> None:
        self.form_data['password'] = '123456789'
        self.form_data['password2'] = 'abc123456789'
        response = self.client.post(self.url, self.form_data, follow=True)

        user_not_exists = User.objects.filter(pk=1).exists()

        self.assertFalse(user_not_exists)

        self.assertRedirects(response, '/registrar/')

        self.assertContains(response, 'Erro, as senhas não correspondem')

    def test_register_view_correctly_show_error_message_if_username_is_longer_than_120_characters(self) -> None:
        self.form_data['username'] = 'A'*121
        response = self.client.post(self.url, self.form_data, follow=True)

        user_not_exists = User.objects.filter(pk=1).exists()

        self.assertFalse(user_not_exists)

        self.assertRedirects(response, '/registrar/')

        self.assertContains(response, 'Erro, nome de usuário muito longo.')
    
    def test_register_view_correctly_show_error_message_if_username_is_less_than_5_characters(self) -> None:
        self.form_data['username'] = 'A'*4
        response = self.client.post(self.url, self.form_data, follow=True)

        user_not_exists = User.objects.filter(pk=1).exists()

        self.assertFalse(user_not_exists)

        self.assertRedirects(response, '/registrar/')

        self.assertContains(response, 'Erro, nome de usuário precisa de mais de 5 caracteres.')

    def test_register_view_redirects_if_user_logged_alredy(self) -> None:

        self.create_account()
        self.client.login(username='breno', password='123456')
        response = self.client.get(self.url)

        self.assertRedirects(response, '/painel/')
        self.assertEqual(response.status_code, 302)
