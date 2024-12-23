from django.urls import path
from django.contrib import admin
from . import views

# Define a list of url patterns

urlpatterns = [
    path('admin/', views.admin, name="admin"),
    path('', views.index, name="index"),
    path('schedule/', views.schedule, name='schedule'),
]
