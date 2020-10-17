from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.topics, name = 'topicsFirstApp'),
    # path('topics/<id>', views.topicsDelete, name = 'topicsFirstApp'),
]
