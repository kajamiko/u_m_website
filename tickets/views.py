from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Ticket
from .models import Comment
from django.db.models import F
from .forms import TicketForm, CommentForm
from .tickets_upvote import upvote_ticket
from django.contrib import messages



def get_tickets(request, variety=''):
	"""
	View returning tickets: either all of them, or filtered by variety.
	"""
	if variety=="features":
		results = Ticket.objects.filter(variety__exact="F").filter(verified__exact=True).order_by('upvotes', '-date_created')
		
	elif variety=="bugs":
		results = Ticket.objects.filter(variety__exact="B").filter(verified__exact=True).order_by('upvotes', '-date_created')
		
	else:
		results = Ticket.objects.all().filter(verified__exact=True).order_by('upvotes', '-date_created')
		
	paginator = Paginator(results, 5)
	try:
		page = request.GET.get('page')
	except PageNotAnInteger:
		page = paginator.page(1)
		
	tickets = paginator.get_page(page)
	return render(request, 'ticket_list.html', {'tickets': tickets})
	

def ticket_details(request, ticket_id):
	"""
	Page displaying ticket's details and comments related.
	Contains also adding comments logic.
	"""
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
		if request.user.is_authenticated:
			data = {'user': request.user, 'author': request.user.username }
			form = CommentForm(initial=data)
		else:		
			form = CommentForm()
	
	return render(request, 'ticket_detail.html', {'form': form, 'ticket': result, 'comments': comments, 'comments_quantity': comments_quantity})

@login_required
def upvote_simple(request, ticket_id):
	"""
	Upvoting 'bug' tickets, only login required.
	"""
	upvote_ticket(ticket_id)
	return redirect('tickets:ticket_details', ticket_id=ticket_id)

	
@login_required
def create_ticket(request):
	"""
	Displays adding ticket form, and adding ticket logic. Only for logged in users.
	"""
	if request.method == 'POST':
		form = TicketForm(request.POST, request.FILES)
		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.author = request.user.username
			ticket.save()
			return redirect("tickets:ticket_details", ticket.id)
	else:
		form = TicketForm()
	return render(request, 'create_ticket.html', {'form': form})


def comment_details(request, comment_id):
	"""
	Comment details and editing view.
	"""
	comment = get_object_or_404(Comment, pk = comment_id)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			updated_comment = form.save(commit=False)
			updated_comment.ticket = comment.ticket
			updated_comment.author = request.user.username
			updated_comment.save()
			return redirect("tickets:comment_details", comment_id=updated_comment.id)
	else:
		if request.user.is_authenticated:
			data = {'user': request.user, 'author': request.user.username, 'title': comment.title, 'content': comment.content }
			form = CommentForm(initial=data)
	return render(request, 'comment_detail.html', {'comment': comment, 'form': form})
	
def search_for_ticket(request):
	"""
	View containing logic for searching through tickets.
	"""
	results = Ticket.objects.filter(issue__icontains=request.GET['q']).order_by('-date_created')
	paginator = Paginator(results, 5)
	try:
		page = request.GET.get('page')
	except PageNotAnInteger:
		page = paginator.page(1)
	
	tickets = paginator.get_page(page)
	return render(request, 'ticket_list.html', {'tickets': tickets})