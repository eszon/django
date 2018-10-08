from django.contrib import admin
from django.urls import path
from .views import person_list
from .views import persons_new



urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new', persons_new, name='person_new'),


]