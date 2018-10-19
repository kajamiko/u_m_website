from django.urls import path
from . import views
from . import chart_view

app_name='home'

urlpatterns=[
     path('homepage', views.homepage, name='homepage'),
     path('project_info/', views.project_info, name="project_info"),
     path('our_promise/', views.promise, name="promise"),
     path('stats/', chart_view.StatsView.as_view(), name="stats"),
     path('for_devs/', views.developers_section, name='developers_section'),
     ]