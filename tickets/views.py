from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Ticket
from .models import Comment
from django.db.models import F
from .forms import TicketForm, CommentForm
from .tickets_upvote import upvote_ticket



def get_tickets(request, variety=''):
	if variety=="features":
		results = Ticket.objects.filter(variety__exact="F").order_by('upvotes', '-date_created')
		
	elif variety=="bugs":
		results = Ticket.objects.filter(variety__exact="B").order_by('upvotes', '-date_created')
		
	else:
		results = Ticket.objects.all().order_by('upvotes', '-date_created')
		
	paginator = Paginator(results, 5)
	try:
		page = request.GET.get('page')
	except PageNotAnInteger:
		page = paginator.page(1)
		
	tickets = paginator.get_page(page)
	return render(request, 'ticket_list.html', {'tickets': tickets})
	

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
			return redirect("tickets:comment_details", comment_id=added_comment.id)
	else:
		form = CommentForm()
		
	
	return render(request, 'ticket_detail.html', {'form': form, 'ticket': result, 'comments': comments, 'comments_quantity': comments_quantity})

@login_required
def upvote_simple(request, ticket_id):
	upvote_ticket(ticket_id)
	return redirect('tickets:ticket_details', ticket_id=ticket_id)
	
@login_required
def create_ticket(request):
	if request.method == 'POST':
		form = TicketForm(request.POST, request.FILES)
		if form.is_valid():
			ticket = form.save()
			return redirect("tickets:ticket_details", ticket.id)
	else:
		form = TicketForm()
	return render(request, 'create_ticket.html', {'form': form})


def comment_details(request, comment_id):
	comment = get_object_or_404(Comment, pk = comment_id)
	return render(request, 'comment_detail.html', {'comment': comment})
	
def search_for_ticket(request):
	results = Ticket.objects.filter(issue__icontains=request.GET['q'])
	paginator = Paginator(results, 5)
	try:
		page = request.GET.get('page')
	except PageNotAnInteger:
		page = paginator.page(1)
		
	tickets = paginator.get_page(page)
	return render(request, 'ticket_list.html', {'tickets': tickets})