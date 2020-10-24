from django.db.models import fields
from rest_framework import serializers
from .models import *

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ("pk", "course_name")

class FilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files
        fields = ("pk", "course", "file_name")