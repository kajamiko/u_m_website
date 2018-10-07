from django.urls import path, include
from . import views

app_name='cart'

urlpatterns=[
     path('add_to_cart/<int:ticket_id>/', views.add_to_cart, name="add_to_cart"),
     path('cart_detail', views.cart_detail, name="cart_detail"),
     path('cart_remove<int:ticket_id>', views.cart_remove, name="cart_remove"),
     ]