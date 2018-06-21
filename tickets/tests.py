from django.test import TestCase
from .models import Ticket
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

