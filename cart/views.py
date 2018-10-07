from django.shortcuts import render, redirect, get_object_or_404
from tickets.models import Ticket
from .cart import Cart
from .forms import CartAddTicketForm


def add_to_cart(request, ticket_id):
     cart = Cart(request)
     ticket = get_object_or_404(Ticket, id=ticket_id)
     if request.method == 'POST':
          update_form = CartAddTicketForm(request.POST)
          if update_form.is_valid():
               cd=update_form.cleaned_data
               cart.add(ticket=ticket,
                         donation = cd['donation'],
                         update=cd['update'])
     else:
          cart.add(ticket=ticket)
     return redirect('cart:cart_detail')

                    
def cart_remove(request, ticket_id):
     cart = Cart(request)
     ticket = get_object_or_404(Ticket, id=ticket_id)
     cart.remove(ticket)
     return redirect('cart:cart_detail')
     
def cart_detail(request):
     cart = Cart(request)
     for item in cart:
          item['update_donation_form'] = CartAddTicketForm(initial={'donation': item['donation'], 'update': True})
     # print(len(cart))
     return render(request, 'detail.html', {'cart': cart})