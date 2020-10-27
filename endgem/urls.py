from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name="Course list"),
    # path('courses/<pk>', views.courses, name="Single course"),
    # path('materials/', views.materials, name="Material list"),
    path('materials/', views.materialList, name="Upload course material"),
    path('materials/', views.materialList, name="Get course material"),
    path('materials/<courseID>', views.material, name="Filtered course materials for one course with pk"),

]
