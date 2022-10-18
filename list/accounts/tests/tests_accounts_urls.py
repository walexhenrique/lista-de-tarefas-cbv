from unittest import TestCase

from django.urls import reverse


class AccountsURLsTest(TestCase):
    """class responsible for testing the urls of the Accounts app"""

    def test_login_url_path_is_correct(self) -> None:
        url = reverse('accounts:login')
        self.assertEqual(url, '/')
    
    def test_register_url_path_is_correct(self) -> None:
        url = reverse('accounts:register')
        self.assertEqual(url, '/registrar/')
