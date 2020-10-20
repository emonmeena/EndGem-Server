from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.topic_names, name = 'topic names'),
    path('topics/<pk>', views.topic_details, name = 'topic details'),
]
