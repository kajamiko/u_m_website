from django.test import TestCase
from .forms import CartAddTicketForm
from django.contrib.auth.models import User


class TestTicketForm(TestCase):
     
     
     def test_for_updating(self):
          """
          Normal, as from a real view
          """
          form = CartAddTicketForm({'donation': 20, 'update': True})
          self.assertTrue(form.is_valid())
          
     def test_for_update_with_no_donation_value(self):
          """
          Donation value is required
          """
          form = CartAddTicketForm({'update': True})
          self.assertFalse(form.is_valid())
          
     def test_for_add_with_no_update(self):
          """
          Update is not required, as it is also an add form
          """
          form = CartAddTicketForm({'donation': 20})
          self.assertTrue(form.is_valid())