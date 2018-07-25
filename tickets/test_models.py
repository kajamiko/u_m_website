from django.test import TestCase
from .models import Ticket
from .models import Comment
from datetime import date


class test_tickets(TestCase):

	def test_simplest(self):
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		self.assertEqual(ticket.id, 1)
		self.assertEqual(ticket.variety, 'B')
		self.assertEqual(ticket.issue, 'serious issue')
		self.assertEqual(ticket.upvotes, 0)
		self.assertFalse(ticket.verified)
		self.assertEqual(ticket.status, 'to do')
		self.assertEqual(ticket.date_created, date.today())
		self.assertFalse(ticket.date_verified)
		self.assertEqual(ticket.__str__(), "Ticket #{0}, type: {1}, {2}, {3} upvotes".format(str(ticket.id), ticket.variety, ticket.status, ticket.upvotes ))
		
	def test_comment(self):
		ticket = Ticket(variety='B', issue='serious issue')
		ticket.save()
		comment = Comment(ticket=ticket, author='test_author', title='test_tile', content='test_comment')
		comment.save()
		self.assertEqual(comment.id, 1)
		self.assertEqual(comment.author, 'test_author')
		self.assertEqual(comment.date_published, date.today())
		self.assertEqual(comment.__str__(), "{0} - {1} - {2}".format(comment.title, comment.date_published, comment.author) )