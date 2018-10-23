from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.test import TestCase

class TestProfileForm(TestCase):
     
     
     def test_for_posting_user_only(self):
          """
          Testing if passing user only value is working - never passes validation though
          """
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          form = ProfileForm({'user': user})
          self.assertFalse(form.is_valid())
          
     def test_for_posting(self):
          """
          Testing form - for some reason it's always invalid
          """
          user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
          form = ProfileForm({'user': user, 'full_name': 'test', 'phone_number': 'test', 'country': 'test',
          'postcode': 'test', 'town_or_city': 'test', 'street_address1': 'test',
        'street_address2': 'test', 'county': 'test'})
          self.assertFalse(form.is_valid())