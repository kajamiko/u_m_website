from django.db import models
from tickets.models import Ticket
from decimal import Decimal


class Order(models.Model):
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    country = models.CharField(max_length = 40, blank = False)
    address = models.CharField(max_length=150, blank=False)
    postal_code = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
 
    class Meta:
        ordering = ('-created', )
 
    def __str__(self):
        return 'Order {}'.format(self.id)
 
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
 
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='order_items', on_delete=models.CASCADE)
    donation = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.id)
        
    def get_cost(self):
        return Decimal(self.donation)
    