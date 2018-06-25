from django.test import TestCase
from .models import Ticket
from django.shortcuts import get_object_or_404

class test_views(TestCase):


	def test_ticket_homepage(self):

		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		homepage = self.client.get('/')
		self.assertEqual(homepage.status_code, 200)
		self.assertTemplateUsed(homepage, 'ticket_list.html')
		self.assertEqual(len(homepage.context['tickets']), 1)

	def test_ticket_detail_page(self):
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		page = self.client.get('/tickets/{0}/'.format(ticket.id))
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, 'ticket_detail.html')

	def test_ticket_detail_page_for_items_doest_exist(self):
		page = self.client.get('/tickets/45/')
		self.assertEqual(page.status_code, 404)

	def test_simple_upvoting(self):

		saved_ticket = Ticket(variety='B', issue='serious issue')
		saved_ticket.save()

		page_upvote = self.client.get('/tickets/upvote/{0}/'.format(saved_ticket.id))
		#page redirecting OK
		self.assertEqual(page_upvote.status_code, 302)
		page= self.client.get('/tickets/{0}/'.format(saved_ticket.id))
		#page returns different __str__, because upvote is working
		self.assertNotEqual(page.context['ticket'], saved_ticket.__str__())

		
	def test_creating_tickets(self):

		page = self.client.get('/tickets/add_ticket/')
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, 'create_ticket.html')

	def test_adding_ticket(self):
		{"issue": "test", "description": "test"}
		page = self.client.post("/tickets/add_ticket/", {"variety": "B", "issue": "test", "description": "test"})
		ticket = get_object_or_404(Ticket, pk=1)
		self.assertEqual(ticket.issue, "test")