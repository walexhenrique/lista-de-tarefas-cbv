from ..forms.form_register import RegisterForm
from .tests_accounts_base import AccountsBaseTest


class RegisterFormTest(AccountsBaseTest):

    def setUp(self) -> None:
        self.form_data = {
            'username': 'breno',
            'email': 'breno@email.com',
            'password': '123456',
            'password2': '123456',
        }
        return super().setUp()

    def test_register_form_unused_email_and_passwords_the_same_equals_validation_works(self):
        form = RegisterForm(self.form_data)
        self.assertTrue(form.is_valid())
    

    def test_register_form_is_not_valid_if_email_is_already_being_used(self):
        self.create_account()
        self.form_data['username'] = 'carlinhos'
        form = RegisterForm(self.form_data)

        self.assertFalse(form.is_valid())
    
    def test_register_form_is_not_valid_if_passwords_not_equals(self):
        self.form_data['password2'] = '11111111'
        form = RegisterForm(self.form_data)
        self.assertFalse(form.is_valid())
    

