from django.test import TestCase, RequestFactory
from django.conf import settings
from .models import Order, OrderItem
from tickets.models import Ticket

class TestOrdersModels(TestCase):
     
     
     def test_creating_order_and_str_function(self):
          """
          Function is testing creating an order with 2 order items and returning their __str__(), and
          Order.return_items(), which returns a list of tickets' titles.
          """
          
          order_test = Order.objects.create(
               full_name = "some name", 
               phone_number = "0123456789", 
               country = "United Kingdom",
               postcode = "FG4 6HN", 
               town_or_city = "Neverland",
               street_address1 = "some street",
               county = "county"
          
          )
          ticket_order = Ticket.objects.create(
               variety = "F",
               issue = "ticket0"
          )
          ticket_order1 = Ticket.objects.create(
               variety = "F",
               issue = "ticket1",
          
          )
          order_item = OrderItem.objects.create(
               order=order_test,
               ticket=ticket_order,
               donation=5)

          order_item2 = OrderItem.objects.create(
               order=order_test,
               ticket=ticket_order1,
               donation=15) 
          self.assertEqual("order id is 1, ticket's id is 1 - ticket0", str(order_item))
          self.assertEqual(str(order_test), 'Order #1, for 2 item(s), total cost of 20.00.')
          self.assertEqual(['ticket0', 'ticket1'],order_test.return_items())
  
          
     def test_order_functions(self):
          """
          Tests other inner Order functions
          """
          order_test = Order.objects.create(
               full_name = "some name", 
               phone_number = "0123456789", 
               country = "United Kingdom",
               postcode = "FG4 6HN", 
               town_or_city = "Neverland",
               street_address1 = "some street",
               county = "county"
          
          )
          ticket1 = Ticket.objects.create(
               variety = "F",
               issue = "ticket0"
          )
          ticket2 = Ticket.objects.create(
               variety = "F",
               issue = "ticket1",
          
          )
          order_item1 = OrderItem.objects.create(
               order=order_test,
               ticket=ticket1,
               donation=5)

          order_item2 = OrderItem.objects.create(
               order=order_test,
               ticket=ticket1,
               donation=15) 
          
          self.assertEqual(order_test.get_total_cost(), 20)
          self.assertEqual(order_test.get_items_quantity(), 2)