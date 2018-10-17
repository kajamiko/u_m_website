from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order

# class TestAccountsModels(TestCase):
     
#      user_test = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
#      order_test = Order.objects.create(
#                profile = user_test.profile,
#                full_name = "some name", 
#                phone_number = "0123456789", 
#                country = "United Kingdom",
#                postcode = "FG4 6HN", 
#                town_or_city = "Neverland",
#                street_address1 = "some street",
#                street_address2 = "SOme building",
#                county = "hampshire"
          
#           )
#      user_test.profile.get_orders()