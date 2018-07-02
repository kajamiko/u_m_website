from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Ticket
from .models import Comment
from django.db.models import F
from .forms import TicketForm, CommentForm


def get_tickets(request):
	results = Ticket.objects.all()
	return render(request, 'ticket_list.html', {'tickets': results})

def ticket_details(request, ticket_id):
	result = get_object_or_404(Ticket, pk=ticket_id)
	
	comments = Comment.objects.filter(ticket__exact=result)
	comments_quantity = len(comments)
	# adding comment logic
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			added_comment = form.save(commit=False)
			added_comment.ticket = result
			added_comment.save()
			return redirect(ticket_details, result.id)
	else:
		form = CommentForm()
	return render(request, 'ticket_detail.html', {'form': form, 'ticket': result, 'comments': comments, 'comments_quantity': comments_quantity})

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
