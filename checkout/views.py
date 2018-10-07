from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm

def create_order(request):
     cart = Cart(request)
     if request.method=='POST':
          form = OrderCreateForm(request.POST)
          if form.is_valid():
               # a form is saved to a variable
               order = form.save()
               for item in cart:
                    OrderItem.objects.create(
                         order=order,
                         ticket=item['ticket'],
                         donation=item['donation']
                         )
               cart.clear()
          return render(request, 'created.html')
     else:
          form = OrderCreateForm()
     return render(request, 'create_order.html', {'form': form})