from django.db import models
from django.contrib.auth.models import User


TICKET_VARIETIES_CHOICES=(
	('B', 'Bug'),
	('F', 'Feature')
	)
TICKET_STATUS_CHOICES = (
	('to do', 'To do'),
	('doing', 'Doing'),
	('done', 'Done')
	)

class Ticket(models.Model):
	variety = models.CharField(max_length=7, choices=TICKET_VARIETIES_CHOICES, blank=False)
	upvotes = models.IntegerField(default=0)
	date_created = models.DateField(auto_now_add=True)
	# date_created.editable = True
	date_verified = models.DateField(null=True)
	date_start_dev = models.DateField(null=True,blank=True)
	date_done = models.DateField(null=True,  blank=True)
	author = models.CharField(max_length=20, blank=True)
	verified = models.BooleanField(default=False)
	status = models.CharField(max_length=6, choices=TICKET_STATUS_CHOICES, default='to do')
	issue = models.CharField(max_length=100, blank=False)
	description = models.TextField(blank=True)
	
	def get_updates(self):
		
		return [self.date_verified, self.date_start_dev, self.date_done]
	
	def __str__(self):
		return "Ticket #{0}, type: {1}, {2}, {3} upvotes".format(str(self.id), self.variety, self.status, self.upvotes)


class Comment(models.Model):
	ticket = models.ForeignKey(Ticket, null=False, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	author = models.CharField(max_length=20, blank=False)
	title = models.CharField(max_length=40, blank = False)
	content = models.TextField(blank = False)
	date_published = models.DateField(auto_now_add=True)
	
	
	class Meta:
		ordering = ["-date_published"]
	def __str__(self):
		return "{0} - {1} - {2}".format(self.title, self.date_published, self.author)