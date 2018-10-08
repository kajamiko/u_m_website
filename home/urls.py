from django.urls import path
from . import views

app_name='home'

urlpatterns=[
     path('homepage', views.homepage, name='homepage'),
     path('project_info/', views.project_info, name="project_info"),
     path('our_promise/', views.promise, name="promise"),
     path('stats/', views.show_stats, name="show_stats"),
     ]