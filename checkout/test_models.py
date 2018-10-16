from django.test import TestCase, RequestFactory
from django.conf import settings
from .models import Order, OrderItem
from tickets.models import Ticket

class TestOrdersModels(TestCase):
     
     def test_creating_order_simple(self):
          
          order_test = Order.objects.create(
               full_name = "some name", 
               phone_number = "0123456789", 
               country = "United Kingdom",
               postcode = "FG4 6HN", 
               town_or_city = "Neverland",
               street_address1 = "some street",
               street_address2 = "SOme building",
               county = "county"
          
          )
          ticket_order = Ticket.objects.create(
               variety = "F",
               upvotes = 0,
               author = "SOmeone",
               status = "to do",
               issue = "blabla",
          
          )
          ticket_order1 = Ticket.objects.create(
               variety = "F",
               upvotes = 0,
               author = "SOmeone",
               status = "to do",
               issue = "blabla",
          
          )
          order_item = OrderItem.objects.create(
               order=order_test,
               ticket=ticket_order,
               donation=5)

               
          order_item2 = OrderItem.objects.create(
               order=order_test,
               ticket=ticket_order1,
               donation=15) 
          print("The cost of item is {0}".format(order_item.get_cost()))
          print(order_item)
          print(order_test)
          
     # def test_creating_order
     