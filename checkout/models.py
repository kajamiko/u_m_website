from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket


class Order(models.Model):
    """
    Order details class, some of which can be stored in Profile 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length = 40, blank = False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=60, blank=False)
    street_address2 = models.CharField(max_length=60, blank=True)
    county = models.CharField(max_length=20, blank=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
 
    class Meta:
        ordering = ('-created', )
 
    def __str__(self):
        return 'Order #{0}, for {2} item(s), total cost of {1}.'.format(self.id, self.get_total_cost(), self.get_items_quantity())
 
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_items_quantity(self):
        return sum(1 for item in self.items.all())
        
    def return_items(self):
        
        return list(item.ticket.issue for item in self.items.all())
 
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='order_items', on_delete=models.CASCADE)
    donation = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return 'order id is {0}, ticket is {1} - {2}'.format(self.order.id, self.ticket.id, self.ticket.issue)
        
    def get_cost(self):
        return self.donation
    