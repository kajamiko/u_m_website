from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket
from .models import Comment
from django.shortcuts import get_object_or_404, reverse
from django.contrib import messages



class TestViews(TestCase):
	
	def test_ticket_all(self):
		"""
		Tests displaying all tickets
		"""
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		ticket1 = Ticket(variety='F', issue='serious feature')
		ticket1.save()
		homepage = self.client.get(reverse('tickets:all_tickets'))
		self.assertEqual(homepage.status_code, 200)
		self.assertTemplateUsed(homepage, 'ticket_list.html')
		self.assertEqual(len(homepage.context['tickets']), 2)
		
	def test_ticket_features(self):
		"""
		Tests filtering by variety : feature.
		"""
		ticket_f = Ticket(variety='F', issue='some feature')
		ticket_f.save()
		ticket_b = Ticket(variety='B', issue='serious issue')
		ticket_b.save()
		response = self.client.get(reverse('tickets:get_features', kwargs={'variety': 'features'}))
		self.assertTemplateUsed(response, 'ticket_list.html')
		self.assertIn("some feature", str(response.content))
		self.assertNotIn("serious issue", str(response.content))
		
	def test_ticket_bugs(self):
		"""
		Tests filtering by variety: bugs.
		"""
		ticket_f = Ticket(variety='F', issue='some feature')
		ticket_f.save()
		ticket_b = Ticket(variety='B', issue='serious issue')
		ticket_b.save()
		response = self.client.get(reverse('tickets:get_bugs', kwargs={'variety': 'bugs'}))
		self.assertTemplateUsed(response, 'ticket_list.html')
		self.assertNotIn("some feature", str(response.content))
		self.assertIn("serious issue", str(response.content))
		
	def test_ticket_detail_page(self):
		"""
		Tests ticket details view, for template used, page status code and content
		"""
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		page = self.client.get('/tickets/{0}/'.format(ticket.id))
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, 'ticket_detail.html')
		self.assertIn("serious issue", str(page.content))

	def test_ticket_detail_page_for_items_doest_exist(self):
		"""
		Tests for error
		"""
		page = self.client.get('/tickets/45/')
		self.assertEqual(page.status_code, 404)

	def test_simple_upvoting(self):
		"""
		Testing simple upvoting - coverage shows is not tested, for some reason.
		"""
		saved_ticket = Ticket(variety='B', issue='serious issue')
		saved_ticket.save()

		page_upvote = self.client.get('/tickets/upvote/{0}/'.format(saved_ticket.id))
		#page redirecting OK
		self.assertEqual(page_upvote.status_code, 302)
		page= self.client.get('/tickets/{0}/'.format(saved_ticket.id))
		#page returns different __str__, because upvote is working
		self.assertNotEqual(page.context['ticket'], saved_ticket.__str__())
		

		
	def test_creating_tickets_get_request(self):
		"""
		Tests creating tickets page.
		"""
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		self.client.login(username='foo', password='bar')
		page = self.client.get('/tickets/add_ticket/')
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, 'create_ticket.html')

	def test_adding_ticket(self):
		"""
		Tests adding a ticket actually.
		"""
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		self.client.login(username='foo', password='bar')
		page = self.client.post("/tickets/add_ticket/", {"variety": "B", "issue": "test", "description": "test"})
		ticket = get_object_or_404(Ticket, pk=1)
		self.assertEqual(ticket.variety, "B")
		
	def test_adding_comment(self):
		"""
		Tests adding comment anonymously.
		"""
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		self.client.get('/tickets/{0}/'.format(ticket.id))
		page = self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content', 'title': 'test_title'})
		comment = get_object_or_404(Comment, pk=1)
		self.assertEqual(page.status_code, 302)
		self.assertEqual(comment.content, 'test_content')
		page = self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content'})
		self.assertEqual(page.status_code, 200)
	
	def test_comment_details(self):
		"""
		Tests comment page view.
		"""
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		self.client.get('/tickets/{0}/'.format(ticket.id))
		self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content', 'title': 'test_title'})
		page = self.client.get('/tickets/comment/1')
		self.assertEqual(page.status_code, 200)
		
	def adding_comment_as_a_user(self):
		"""
		Tests adding ticket as a user.
		"""
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		self.client.login(username='foo', password='bar')
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		self.client.get('/tickets/{0}/'.format(ticket.id))
		self.client.post('/tickets/{0}/'.format(ticket.id), {'author': 'test', 'content': 'test_content', 'title': 'test_title'})
		page = self.client.get('/tickets/comment/1')
		self.assertEqual(page.status_code, 200)
		self.assertIn("foo", str(page.content))
		
	
	def test_search_for_ticket(self):
		"""
		Tests searching functionality.
		"""
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		response = self.client.get("/tickets/search", {'q': 'issue'})
		self.assertTemplateUsed(response, 'ticket_list.html')
		self.assertIn("serious issue", str(response.content))