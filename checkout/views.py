from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm
from tickets.tickets_upvote import upvote_ticket

def create_order(request):
     if request.method=='POST':
          form = OrderCreateForm(request.POST, request.FILES)
          if form.is_valid():
               # a form is saved to a variable
               order = form.save()
               # tu is_paid
               items = OrderItem.objects.filter(order=order)
          return render(request, 'created.html', {'order': order, 'items': items})
     else:
          form = OrderCreateForm()
     return render(request, 'create_order.html', {'form': form})
     
def is_paid(request, order_id):
     cart = Cart(request)
     order = get_object_or_404(Order, pk=order_id)
     for item in cart:
          OrderItem.objects.create(
                         order=order,
                         ticket=item['ticket'],
                         donation=item['donation']
                         )
          upvote_ticket(item['ticket'].id)
          cart.clear()
     order.paid = True
     order.save()
     return True