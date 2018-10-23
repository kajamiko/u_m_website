from django.urls import path
from . import views

app_name="checkout"

urlpatterns=[
     path('create_order', views.create_order, name="order_create"),
     path('order_pay/<int:order_id>', views.order_pay, name="order_pay"),
     path('cancel_order/<int:order_id>', views.cancel_order, name="cancel_order")
     ]