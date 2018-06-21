from django.db import models


TICKET_VARIETIES_CHOICES=(
	('B', 'Bug'),
	('F', 'Feature')
	)

class Ticket(models.Model):
	variety = models.CharField(max_length=1, choices=TICKET_VARIETIES_CHOICES, blank=False)
	upvotes = models.IntegerField(default=0)
	date_created = models.DateField(auto_now_add=True)
	date_verified = models.DateField(null=True)
	author = models.CharField(max_length=20, blank=True)
	verified = models.BooleanField(default=False)
	status = models.CharField(max_length=6, default='to do')
	issue = models.CharField(max_length=100, blank=False)
	description = models.TextField(blank=True)

	def __str__(self):
		return "{0}, {1}, {2}".format(str(self.id), self.issue, self.status)
