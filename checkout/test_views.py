from django.test import Client
from django.shortcuts import reverse
from django.test import TestCase
from django.conf import settings
from tickets.models import Ticket
from django.contrib.auth.models import User
from datetime import date, datetime
from cart.cart import Cart
import stripe
from django.conf import settings

class TestCheckoutView(TestCase):
     
     def setUp(self):
          self.client = Client()
     
     def test_simple_rendering(self):
          """
          This automated test is checking page rendering
          """
          ticket = Ticket(variety='F', issue='some feature')
          ticket.save() 
          self.client.get(reverse('cart:add_to_cart', args=(ticket.id,)))
          session = self.client.session
          response = self.client.get(reverse('checkout:order_create'))
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed('create_oder.html')
          self.assertIn('Payment Details', str(response.content))
          self.assertIn('Back to cart', str(response.content))
     
     def test_get_request_and_pay(self):
          """
          Automated test to send payments
          """
          stripe.api_key = settings.STRIPE_SECRET
          
          token = stripe.Token.create(
            card={
                'number': '4242424242424242',
                'exp_month': '6',
                'exp_year': str(datetime.today().year + 1),
                'cvc': '123',
            }
               )
          ticket = Ticket(variety='F', issue='some feature')
          ticket.save() 
          self.client.get(reverse('cart:add_to_cart', args=(ticket.id,)))
          session = self.client.session
          data= {'full_name': 'test', 'phone_number': 'test', 'country': 'test', 'postcode': 'test',
          'town_or_city': 'test', 'street_address1': 'test', 'county': 'test', 'stripeToken': token.id}
          response = self.client.get(reverse('checkout:order_create'))
          success, transaction visible on my stripe account
          self.client.post(reverse('checkout:order_create'), data=data)
          