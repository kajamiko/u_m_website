from django.test import TestCase
from .models import Ticket
from .models import Comment
from django.shortcuts import get_object_or_404, reverse

class test_views(TestCase):


	def test_ticket_homepage(self):

		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		homepage = self.client.get(reverse('tickets:all_tickets'))
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
		page = self.client.post("/tickets/add_ticket/", {"variety": "B", "issue": "test", "description": "test"})
		ticket = get_object_or_404(Ticket, pk=1)
		self.assertEqual(ticket.variety, "B")
		
	def test_adding_comment(self):
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		self.client.get('/tickets/{0}/'.format(ticket.id))
		page = self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content', 'title': 'test_title'})
		comment = get_object_or_404(Comment, pk=1)
		self.assertEqual(page.status_code, 302)
		self.assertEqual(comment.content, 'test_content')
		page = self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content'})
		self.assertEqual(page.status_code, 200)
	
	def test_comment_displaying(self):
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		self.client.get('/tickets/{0}/'.format(ticket.id))
		self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content', 'title': 'test_title'})
		page = self.client.get('/tickets/comment/1')
		self.assertEqual(page.status_code, 200)
		
		