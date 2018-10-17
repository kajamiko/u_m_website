from django.shortcuts import get_object_or_404
from django.test import TestCase
from .models import Ticket
from .tickets_upvote import upvote_ticket



class TestUpvoting(TestCase):
     
     def test_ticket_upvote(self):
          ticket = Ticket(variety='B', issue='serious issue')
          ticket.save()
          upvote_ticket(ticket.id)
          ticket = get_object_or_404(Ticket, pk=1)
          self.assertEqual(ticket.upvotes, 1)