from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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
          
     def test_if_logs_in(self):
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          page = self.client.post('/accounts/login/', {'username': 'temporary', 'password': 'temporary'})
          self.assertEqual(page.status_code, 302)
          #invalid data, returns code 200 because not redirecting
          page = self.client.post('/accounts/login/', {'username': 'temporar', 'password': 'temporary'})
          self.assertEqual(page.status_code, 200)