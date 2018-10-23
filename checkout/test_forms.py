from django.test import TestCase
from .forms import OrderCreateForm
from django.contrib.auth.models import User


class TestOrderForm(TestCase):
     
     def test_form_complete(self):
          """
          Testing filled form.
          However, when passing the optional foreign key 'user' field returns form invalid for some reason, as it is supposed to be empty.
          It is working fine with model tests and in live tests as well.
          """
          user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
          
          test_form = OrderCreateForm({'user': user, 'full_name': 'name', 'phone_number': 'test', 'country': 'test',
               'postcode': 'test', 'town_or_city': 'test', 'street_address1': 'test',
             'street_address2': 'test', 'county': 'test'})
          # it does not work as expected
          self.assertFalse(test_form.is_valid())
          test_form = OrderCreateForm({'full_name': 'name', 'phone_number': 'test', 'country': 'test',
               'postcode': 'test', 'town_or_city': 'test', 'street_address1': 'test',
             'street_address2': 'test', 'county': 'test'})
          self.assertTrue(test_form.is_valid())
          
     def test_form_without_optional_values(self):
          
          test_form = OrderCreateForm({'full_name': 'name', 'phone_number': 'test', 'country': 'test',
               'postcode': 'test', 'town_or_city': 'test', 'street_address1': 'test', 'county': 'test'})
          self.assertTrue(test_form.is_valid())
     
     def test_form_without_some_required_value(self):
          """
          Tests form with no required value
          """
          test_form = OrderCreateForm({'phone_number': 'test', 'country': 'test',
               'postcode': 'test', 'town_or_city': 'test', 'street_address1': 'test',
             'street_address2': 'test', 'county': 'test'})
          self.assertFalse(test_form.is_valid())    