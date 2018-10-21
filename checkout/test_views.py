from django.test import Client
from django.shortcuts import reverse
from django.test import TestCase
from django.conf import settings
from tickets.models import Ticket
from datetime import date
from cart.cart import Cart