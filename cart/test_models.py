from django.test import TestCase, RequestFactory
from django.conf import settings
from tickets.models import Ticket
from datetime import date
from .cart import Cart


class TestCartClass(TestCase):
     
     def setUp(self):
          """
          Setting up test case
          """
          self.request = RequestFactory()
          self.request.session = {}
        
        
     def test_init_empty(self):
          """
          Initializing cart
          """
          cart = Cart(self.request)
          self.assertEqual(self.request.session.get(settings.CART_SESSION_ID), {})
        
     def test_cart_len(self):
          """
          Testing __len__() function
          """
          cart = Cart(self.request)
          self.assertEqual(len(cart), 0)
          
     def test_cart_get_total(self):
          """
          Testing if gete_total() gives expected results
          """
          ticket = Ticket(variety='F', issue='some extra feature')
          ticket.save()
          cart = Cart(self.request)
          cart.add(ticket)
          self.assertEqual(cart.get_total(), 5)
          ticket2 = Ticket.objects.create(
               variety = "F",
               upvotes = 0,
               author = "SOmeone",
               status = "to do",
               issue = "blabla",
          
          )
          cart.add(ticket2)
          self.assertEqual(cart.get_total(), 10)
          
     def test_adding_ticket_to_cart(self):
          """
          Testing adding to cart
          """
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
     
     def test_clear_cart(self):
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
     
     # def test_cart_save(self):
     #    ticket = Ticket(variety='F', issue='some extra feature')
     #    ticket.save()
     #    cart = Cart(self.request)
     #    cart.add(ticket)
     #    cart.save()
     #    self.assertIn(ticket, cart)
          