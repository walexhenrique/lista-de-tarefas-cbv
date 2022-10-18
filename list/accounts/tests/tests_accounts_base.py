from django.contrib.auth.models import User
from django.test import TestCase


class AccountsBaseTest(TestCase):
    def create_account(
        self,
        username: str ='breno',
        email: str = 'breno@email.com',
        password: str ='123456',
    ) -> User:
        """ Function create a generic account """
        return User.objects.create_user(username=username, email=email, password=password)
