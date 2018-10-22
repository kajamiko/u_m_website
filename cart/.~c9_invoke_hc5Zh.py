from django.test import Client
from django.shortcuts import reverse
from django.test import TestCase, RequestFactory
from django.conf import settings
from tickets.models import Ticket
from datetime import date
from .cart import Cart



class TestCartViews(TestCase):
     
     def setUp(self):
          self.client = Client()
          
     def test_view_add(self):
          ticket = Ticket(variety='F', issue='some feature')
          ticket.save()
          response = self.client.get(reverse('cart:add_to_cart', args=(ticket.id,)))
          # redirecting
          self.assertEqual(response.status_code, 302)
          self.assertEqual(dict(response.items())['Location'], '/cart/cart_detail')
          
     def test_removing_form_cart(self):
          
          ticket = Ticket(variety='F', issue='some feature')
          ticket.save() 
          response = self.client.get(reverse('cart:add_to_cart', args=(ticket.id,)))
          session = self.client.session
          self.assertEqual(session[settings.CART_SESSION_ID], {'1': {'donation': 5}})
          response = self.client.get(reverse('cart:cart_remove', args=(ticket.id,)))
          session = self.client.session
          self.assertEqual(session[settings.CART_SESSION_ID], {})
          self.assertEqual(response.status_code, 302)
          
     def test_cart_detail_view_empty(self):
          response = self.client.get(reverse('cart:cart_detail'))
          self.assertTemplateUsed(response, 'detail.html')
          self.assertIn('Your cart is empty', str(response.content))
     
     def test_cart_detail_view_content(self):
          """
          Tests if order total is rendered as expected, and if Checkout button is visible
          """
          ticket = Ticket(variety='F', issue='some feature')
          ticket.save() 
          response = self.client.get(reverse('cart:add_to_cart', args=(ticket.id,)))
          response = self.client.get(reverse('cart:cart_detail'))
          self.assertIn('Your Order Total is', str(response.content))
          self.assertIn('Checkout', str(response.content))
       
     def test_updating_cart_view(self):
          ticket = Ticket(variety='F', issue='some feature')
          ticket.save()
          self.client.get(reverse('cart:add_to_cart', args=(ticket.id,)))
          page = self.client.post(reverse('cart:add_to_cart', args=(str(ticket.id))), data={"donation": 20, 'update': True})
          session = self.client.session
          self.assertEqual(session[settings.CART_SESSION_ID], {'1': {'donation': '20'}})