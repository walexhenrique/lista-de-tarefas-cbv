import time

import pytest
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from list.tasks.tests.tests_tasks_base import TasksMixin
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser


class BaseFunctionalTest(StaticLiveServerTestCase, TasksMixin):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5) -> None:
        time.sleep(seconds)
    
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )
    
    def fast_login(self) -> User:
        """ Function performs a quick login """
        str_password='123456'
        # Create account and login
        user = self.create_account()
        
        # Acess login page
        self.browser.get(
            self.live_server_url + reverse('accounts:login')
        )

        # User sees the form
        form = self.browser.find_element(By.CLASS_NAME, 'forms')

        # User tries to send values valid
        username = self.get_by_placeholder(form, 'John..')
        password = self.get_by_placeholder(form, 'Senha...')
        username.send_keys('breno')
        password.send_keys(str_password)

        # Send form
        form.submit()
        return user
        
@pytest.mark.functional_test
class AllFunctionalTest(BaseFunctionalTest):
    """ Class responsible for all functional testing, registration, login, creation, editing and deletion of tasks """
    def _create_generic_task_functional_test(self):
        # User sees "criar nova tarefa"
        new_task = self.browser.find_element(By.CLASS_NAME, 'new-task')
        new_task.click()

        # User sees login and creates
        form = self.browser.find_element(By.CLASS_NAME, 'forms')
        title = self.get_by_placeholder(form, 'Titulo...')
        title.send_keys('Tarefa 1')

        # User send form
        form.submit()

    def test_form_login_invalid_credentials(self) -> None:
        # Create a login user
        self.create_account()

        # User opens the page
        self.browser.get(
            self.live_server_url
        )

        # User sees the form
        form = self.browser.find_element(By.CLASS_NAME, 'forms')

        # User tries to send values ​​that do not match
        username = self.get_by_placeholder(form, 'John..')
        password = self.get_by_placeholder(form, 'Senha...')

        username.send_keys('Vagner')
        password.send_keys('123456789')

        # Send form
        form.submit()

        self.assertIn(
            'Nome de usuário e Senha não correspondem!',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
    
    def test_form_login_user_valid_data_can_login_successfully(self) -> None:
        str_password = '123456'

        # Create a login user
        self.create_account()

        # User opens the page
        self.browser.get(
            self.live_server_url
        )

        # User sees the form
        form = self.browser.find_element(By.CLASS_NAME, 'forms')

        # User tries to send values valid
        username = self.get_by_placeholder(form, 'John..')
        password = self.get_by_placeholder(form, 'Senha...')
        username.send_keys('breno')
        password.send_keys(str_password)

        # Send form
        form.submit()

        self.assertIn(
            'Bem vindo:',
            self.browser.find_element(By.CLASS_NAME, 'welcome').text
        )

    def test_form_register_user_the_user_is_able_to_register_successfully(self) -> None:
        # User opens the page
        self.browser.get(
            self.live_server_url + reverse('accounts:register')
        )

        # Form for register
        form_data = {
            'username': 'breno',
            'email': 'breno@email.com',
            'password': '123456',
            'password2': '123456'
        }

        form_placeholders = {
            'username': 'Ex.: John',
            'email': 'Ex.: bruno@email.com',
            'password': 'Digite sua senha...',
            'password2': 'Repita sua senha...',
        }

        # User sees the form
        form = self.browser.find_element(By.CLASS_NAME, 'forms')

        # User tries to send values valid
        for key, value in form_data.items():
            self.get_by_placeholder(form, form_placeholders[key]).send_keys(value)

        # User send form
        form.submit()

        self.assertIn(
            'Usuário criado com sucesso!',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_register_should_generate_an_error_if_the_username_is_already_in_use(self) -> None:
        # Create user
        self.create_account(email='brenogameplays@email.com')

        # User opens the page
        self.browser.get(
            self.live_server_url + reverse('accounts:register')
        )

        # Form for register
        form_data = {
            'username': 'breno',
            'email': 'breno@email.com',
            'password': '123456',
            'password2': '123456'
        }

        form_placeholders = {
            'username': 'Ex.: John',
            'email': 'Ex.: bruno@email.com',
            'password': 'Digite sua senha...',
            'password2': 'Repita sua senha...',
        }

        # User sees the form
        form = self.browser.find_element(By.CLASS_NAME, 'forms')

        # User tries to send values valid
        for key, value in form_data.items():
            self.get_by_placeholder(form, form_placeholders[key]).send_keys(value)

        # User send form
        form.submit()

        self.assertIn(
            'Um usuário com este nome de usuário já existe.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_tasks_user_login_and_successfully_creates_a_new_task(self) -> None:
        # User logs in
        self.fast_login()
        
        self._create_generic_task_functional_test()

        self.assertIn(
            'Tarefa criada com sucesso!',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
    
    def test_tasks_user_login_and_successfully_creates_a_new_task_and_edit_with_successfully(self):
        # User logs in
        self.fast_login()
        
        self._create_generic_task_functional_test()

        # User sees "Editar tarefa" and click
        edit_task = self.browser.find_element(By.CLASS_NAME, 'edit')
        edit_task.click()

        # User sees form and change title and status
        form = self.browser.find_element(By.CLASS_NAME, 'forms')
        self.get_by_placeholder(form, 'Titulo...').clear()
        self.get_by_placeholder(form, 'Titulo...').send_keys('Another title')
        self.browser.find_element(By.NAME, 'finished').click()

        # User send form
        form.submit()

        self.assertIn(
            'Tarefa atualizada com sucesso',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )


        # checks if the task has been marked as finished
        try:
            task_finished = True
            self.browser.find_element(By.CLASS_NAME, 'finished').text
        except:
            task_finished = False

        self.assertTrue(task_finished)

    def test_tasks_user_login_and_successfully_creates_a_new_task_and_delete_with_successfully(self):
        # User logs in
        self.fast_login()
        
        # User create a new task
        self._create_generic_task_functional_test()

        # User sees "Apagar tarefa" and click
        self.browser.find_element(By.CLASS_NAME, 'delete').click()

        # User is redirect for confirmation page
        # User confirm delete
        form = self.browser.find_element(By.CLASS_NAME, 'forms')
        form.submit()

        self.assertIn(
            'Tarefa excluida com sucesso',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
    
    def test_user_logs_in_and_then_logout_successfully_and_redirects_to_login_page(self):
        # User logs in
        self.fast_login()

        # User sees "Sair" and click
        self.browser.find_element(By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(2) > a').click()

        self.assertIn(
            'Entrar',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )




