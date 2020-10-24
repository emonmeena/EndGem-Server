from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name="Get Courses"),
    path('materials/', views.materials, name="Get Courses"),

]
