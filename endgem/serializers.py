from django.db.models import fields
from rest_framework import serializers
from .models import *

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("pk", "name")

class MaterialSerializers(serializers.ModelSerializer):

    class Meta:
        model =  Material
        fields = ("pk", "name", "course") 
