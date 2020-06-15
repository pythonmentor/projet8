from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import auth
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase, Client, RequestFactory
from ..models import User
from ..views import signup, signin, signout, account
from ..forms import SignUpForm, SignInForm


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'last_name': 'hamdi',
            'first_name': 'yann',
            'email': 'ham@homtmail.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('search')
        
    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

    
    
    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_signin_post(self):
        url = reverse('signin')
        data = {
             'username': 'john',
             'password': 'abcdef123456'
        }
        self.response_2 = self.client.post(url, data)
        self.assertEqual(self.response_2.status_code, 302)

    def test_signin_form_valid(self):
        url = reverse('signin')
        self.client.get(reverse('signout'))
        user, created = User.objects.get_or_create(username='toto',
            last_name='hamdi',
            first_name='yann',
            email='ham@homtmail.com',
            password='abcdef123456')
        
        data = {'username': 'toto', 'password': 'abcdef123456'}
        user.set_password('123456789')
        user.save()
        user = auth.authenticate(username='toto', password= '123456789')
        login = self.client.login(username='toto', password= '123456789')
        form = SignInForm(data={'username': 'toto', 'password':'123456789'})
        self.assertTrue(login)
        self.assertTrue(form.is_valid())



    def test_signout(self):
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)

    def test_account(self):
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
    