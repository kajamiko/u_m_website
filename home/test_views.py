from django.test import TestCase
from django.test import Client
from django.shortcuts import reverse
from tickets.models import Ticket
import datetime



class TestViews(TestCase):
     
          
     def setUp(self):
          self.client = Client()
          
     def test_homepage(self):
          response = self.client.get(reverse('home:homepage'))
          self.assertEqual(response.status_code, 200)
          # self.assertIn('Your cart is empty', str(response.content))
          
     def test_project_info_page(self):
          response = self.client.get(reverse('home:project_info'))
          self.assertEqual(response.status_code, 200)
          
     def test_stats_page(self):
          """
          Testing statistics page.
          I have created a ticket object to pass, because pygal.DateLine object throws
          an AttributeError error if no data is passed.
          """
          ticket2 = Ticket.objects.create(
               variety='B', 
               issue='ticket2',
               verified = True,
               date_verified=datetime.date.today()
               )
              
          response = self.client.get(reverse('home:stats'))
          self.assertEqual(response.status_code, 200)
          
     def test_stats_for_error(self):
          response = self.client.get(reverse('home:stats'))
          self.assertEqual(response.status_code, 200)
          
     def test_promise(self):
          response = self.client.get(reverse('home:promise'))
          self.assertEqual(response.status_code, 200)