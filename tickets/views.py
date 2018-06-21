from django.shortcuts import render, HttpResponse, redirect
from .models import Ticket


def get_tickets(request):
	results = Ticket.objects.all()
	return render(request, 'ticket_list.html', {'tickets': results})