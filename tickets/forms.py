from django import forms
from .models import Ticket
from .models import Comment

class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('variety', 'issue', 'description')


class CommentForm(forms.ModelForm):
	model = Comment
	fields = ('author', 'content')