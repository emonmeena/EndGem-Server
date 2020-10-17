from django.db.models import fields
from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ["pk", "top_name"]