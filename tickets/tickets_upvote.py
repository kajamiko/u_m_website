from django.shortcuts import get_object_or_404
from .models import Ticket
from django.db.models import F

def upvote_ticket(ticket_id):
     try:
          ticket = get_object_or_404(Ticket, pk=ticket_id)	
          ticket.upvotes = F('upvotes') + 1
          ticket.save()
          return True
     except Exception as e:
          return e
	