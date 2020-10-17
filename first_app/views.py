from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Topic, Accessrecord, Webpage 
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST'])
def topics(request):
    if request.method == 'GET':
        data = Topic.objects.all()
        serializedData = TopicSerializer(data, context={'request': request}, many=True)

        return Response(serializedData.data)

