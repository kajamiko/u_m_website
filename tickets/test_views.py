from django.test import TestCase
from django.test import Client
from .models import Ticket

class test_views(TestCase):

	def setUp(self):
		self.client = Client()

	def test_ticket_homepage(self):

		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		homepage = self.client.get('/')
		self.assertEqual(homepage.status_code, 200)
		self.assertTemplateUsed(homepage, 'ticket_list.html')
		self.assertEqual(len(homepage.context['tickets']), 1)

	def test_ticket_detail(self):
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		page = self.client.get('/tickets/{0}/'.format(ticket.id))
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, 'ticket_detail.html')


	def test_simple_upvoting(self):

		saved_ticket = Ticket(variety='B', issue='serious issue')
		saved_ticket.save()

		page = self.client.get('/tickets/upvote/{0}/'.format(saved_ticket.id))
		#self.assertEqual(page.status_code, 200)
		print(page.context)
		
