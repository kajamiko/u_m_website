from django.db import models


TICKET_VARIETIES_CHOICES=(
	('B', 'Bug'),
	('F', 'Feature')
	)

class Ticket(models.Model):
	variety = models.CharField(max_length=7, choices=TICKET_VARIETIES_CHOICES, blank=False)
	upvotes = models.IntegerField(default=0)
	date_created = models.DateField(auto_now_add=True)
	date_verified = models.DateField(null=True)
	author = models.CharField(max_length=20, blank=True)
	verified = models.BooleanField(default=False)
	status = models.CharField(max_length=6, default='to do')
	issue = models.CharField(max_length=100, blank=False)
	description = models.TextField(blank=True)

	def __str__(self):
		return "Ticket #{0}, type: {1}, {2}, {3} upvotes".format(str(self.id), self.variety, self.status, self.upvotes)


class Comments(models.Model):
	pass