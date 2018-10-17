from django.urls import path
from . import views

app_name='tickets'

urlpatterns=[
path('issue_tracker/', views.get_tickets, name="all_tickets"),
path('issue_tracker/<str:variety>', views.get_tickets, name="get_features"),
path('issue_tracker/<str:variety>', views.get_tickets, name="get_bugs"),
path('<int:ticket_id>/', views.ticket_details, name="ticket_details"),
path('upvote/<int:ticket_id>/', views.upvote_simple, name="upvote_simple"),
path('add_ticket/', views.create_ticket, name="add_ticket"),
path('comment/<int:comment_id>', views.comment_details, name="comment_details"),
path('search', views.search_for_ticket, name="search"),
]