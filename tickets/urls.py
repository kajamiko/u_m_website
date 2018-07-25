from django.urls import path
from . import views

urlpatterns=[
path('issue_tracker/', views.get_tickets, name="all_tickets"),
path('<int:ticket_id>/', views.ticket_details, name="ticket_details"),
path('upvote/<int:ticket_id>/', views.upvote_simple, name="upvote_simple"),
path('add_ticket/', views.create_ticket, name="add_ticket"),
path('comment/<int:comment_id>', views.comment_details, name="comment_details"),
]