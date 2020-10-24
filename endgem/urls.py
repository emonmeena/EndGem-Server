from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name="Course list"),
    # path('courses/<pk>', views.courses, name="Single course"),
    # path('materials/', views.materials, name="Material list"),
    path('materials/<courseID>', views.materials, name="Filtered course materials"),

]
