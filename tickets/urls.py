from django.urls import path
from . import views

urlpatterns=[
path('', views.get_tickets, name="all_tickets"),
]