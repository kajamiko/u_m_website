from django.test import TestCase, RequestFactory
from django.conf import settings
from tickets.models import Ticket
from datetime import date
from .cart import Cart

class TestCart(TestCase):
     
     def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}
        
        
     def test_init_empty(self):
        cart = Cart(self.request)
        self.assertEqual(self.request.session.get(settings.CART_SESSION_ID), {})
        
     def test_adding_ticket(self):
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
          cart_items = []
          print(len(cart))
          cart.remove(ticket2)
          print(len(cart))