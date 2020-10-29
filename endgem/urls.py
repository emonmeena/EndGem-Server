from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name="Course list"),
    # path('courses/<pk>', views.courses, name="Single course"),
    # path('materials/', views.materials, name="Material list"),
    path('materials/', views.materialList, name="Upload/Get course material"),
    path('materials/topgems/<pk>', views.top_gems, name="Get top_gems"),
    path('materials/<courseID>', views.material, name="Filtered course materials for one course with pk"),

]
