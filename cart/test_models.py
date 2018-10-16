from django.test import TestCase, RequestFactory
from django.conf import settings
from tickets.models import Ticket
from datetime import date
from .cart import Cart


class TestCartModels(TestCase):
     
     def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}
        
        
     def test_init_empty(self):
        cart = Cart(self.request)
        self.assertEqual(self.request.session.get(settings.CART_SESSION_ID), {})
        
     def test_cart_len(self):
          cart = Cart(self.request)
          self.assertEqual(len(cart), 0)
          
          
     def test_adding_ticket_to_cart(self):
          ticket = Ticket(variety='F', issue='some extra feature')
          ticket.save()
          ticket2 = Ticket.objects.create(
               variety = "F",
               upvotes = 0,
               author = "SOmeone",
               status = "to do",
               issue = "blabla",
          
          )
          cart = Cart(self.request)
          cart.add(ticket)
          cart.add(ticket2)
          self.assertEqual(len(cart), 2)
          self.assertEqual(cart.get_total(), 10)
     
     def test_updating_cart(self):
          ticket = Ticket(variety='F', issue='some extra feature')
          ticket.save()
          cart = Cart(self.request)
          cart.add(ticket)
          cart.add(ticket, donation = 15, update=True)
          self.assertEqual(len(cart), 1)
          self.assertEqual(cart.get_total(), 15)
          
     def test_removing_from_cart(self):
          ticket = Ticket(variety='F', issue='some extra feature')
          ticket.save()
          cart = Cart(self.request)
          cart.add(ticket)
          cart.remove(ticket)
          self.assertEqual(len(cart), 0)
          self.assertEqual(cart.get_total(), 0)
     
     def clear_cart(self):
          ticket = Ticket.objects.create(
               variety = "F",
               upvotes = 0,
               author = "SOmeone",
               status = "to do",
               issue = "blabla",
          
          )
          cart = Cart(self.request)
          cart.add(ticket)
          self.assertEqual(len(cart), 1)
          cart.clear()
          self.assertEqual(len(cart), 0)