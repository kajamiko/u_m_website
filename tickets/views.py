from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Ticket
from django.db.models import F
from .forms import TicketForm


def get_tickets(request):
	results = Ticket.objects.all()
	return render(request, 'ticket_list.html', {'tickets': results})

def ticket_details(request, ticket_id):
	result = get_object_or_404(Ticket, pk=ticket_id)
	return render(request, 'ticket_detail.html', {'ticket': result})

def upvote_simple(request, ticket_id):
	ticket = get_object_or_404(Ticket, pk=ticket_id)	
	ticket.upvotes = F('upvotes') + 1
	ticket.save()
	return redirect('ticket_details', ticket.id)

def create_ticket(request):

	if request.method == 'POST':
		form = TicketForm(request.POST, request.FILES)
		if form.is_valid():
			ticket = form.save()
			return redirect(ticket_details, ticket.id)
	else:
		form = TicketForm()
	return render(request, 'create_ticket.html', {'form': form})
