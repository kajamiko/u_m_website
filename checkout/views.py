import stripe
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from django.contrib import messages
from .forms import OrderCreateForm
from django.conf import settings
from tickets.tickets_upvote import upvote_ticket


stripe.api_key = settings.STRIPE_SECRET

def create_order(request):

     stripe_key= settings.STRIPE_PUBLISHABLE
     cart = Cart(request)
     total = cart.get_total() * 100
     if request.method=='POST':
          form = OrderCreateForm(request.POST, request.FILES)
          if form.is_valid():
               # a form is saved to a variable    
               order = form.save()
          
               try:
                    customer = stripe.Charge.create(
                         amount = total,
                         currency = 'GBP',
                         description = str(order.id),
                         source=request.POST['stripeToken'],
                         )

               except stripe.error.CardError:
                    messages.error(request, "Your card was declined")
                
               if customer:

                    messages.error(request, "You have succesfully paid")
               
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
                    items = OrderItem.objects.filter(order=order)
                    return render(request, 'created.html', {'order': order, 'items': items})
               else:
                    messages.error(request, "Unable to take payment")
          else:
          
               messages.error(request, "Some of your details are incorrect!")
     else:
          if request.user.is_authenticated:
               prof = request.user.profile
               data = {
               'user': request.user,
               'full_name': prof.full_name,
               'phone_number': prof.phone_number, 
               'country': prof.country,
               'postcode': prof.postcode, 
               'town_or_city': prof.town_or_city, 
               'street_address1': prof.street_address1,
               'street_address2': prof.street_address2,
               'county': prof.county}
               
               form = OrderCreateForm(initial=data)

          else:
               form = OrderCreateForm()
               
     return render(request, 'create_order.html', {'form': form, 'total': total, 'stripe_key': stripe_key})