from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
path('logout/', views.logout, name='logout'),
path('login/', views.login, name='login'),
path('register/', views.registration, name='register'),
path('account_view/', views.account_view, name='your_account')
]