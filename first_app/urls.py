from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name = 'courses'),
    path('files/', views.files, name = 'all files'),
    # path('files/<int:pk>', views.files, name = 'specific files'),
]
