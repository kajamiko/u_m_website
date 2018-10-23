from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, reverse

class Test_account_views(TestCase):
     
     def test_if_registration_page_works(self):
          page = self.client.get('/accounts/register/')
          self.assertEqual(page.status_code, 200)
          self.assertTemplateUsed(page, 'registration.html')
     
     def test_if_login_page_works(self):
          page = self.client.get('/accounts/login/')
          self.assertEqual(page.status_code, 200)
          self.assertTemplateUsed(page, 'login.html')
     
     def test_if_registers(self):
          #passed, registered
          page = self.client.post('/accounts/register/', {'email': 'some@some.com', 'username': 'some',
          'password1': 'coincoer', 'password2':'coincoer'})
          self.assertEqual(page.status_code, 302)
          # invalid data- didnt redirect after registering, just returned 200 code
          page = self.client.post('/accounts/register/', {'email': 'gnome@some.com', 'username': 'user',
          'password1': 'parapara'})
          self.assertEqual(page.status_code, 200)
     
     def test_redurect_if_user_logged_in(self):
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          self.client.post('/accounts/login/', {'username': 'temporary', 'password': 'temporary'})  
          page = self.client.get('/accounts/register/')
          self.assertEqual(page.status_code, 302)
          
     def test_if_logs_in(self):
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          page = self.client.post('/accounts/login/', {'username': 'temporary', 'password': 'temporary'})
          self.assertEqual(page.status_code, 302)
          #invalid data, returns code 200 because not redirecting
          page = self.client.post('/accounts/login/', {'username': 'temporar', 'password': 'temporary'})
          self.assertEqual(page.status_code, 200)
     
     def test_logout(self):
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          page = self.client.post('/accounts/login/', {'username': 'temporary', 'password': 'temporary'})
          page = self.client.get('/accounts/logout/')
          self.assertEqual(page.status_code, 302)
     
     def test_posting_profile_data(self):
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          self.client.post('/accounts/login/', {'username': 'temporary', 'password': 'temporary'})
          page = self.client.post(reverse('accounts:your_account'), data={ 'full_name': "test"})
          self.assertEqual(page.status_code, 200)
          self.assertIn('test', str(page.content))