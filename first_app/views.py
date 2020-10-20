from decimal import Context
from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .models import Topic
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST'])
def topic_names(request):
    if request.method == 'GET':
        data = Topic.objects.all()
        serializedData = TopicSerializer(data, context={'request': request}, many=True)

        return Response(serializedData.data)

    elif request.method == 'POST':
        serializedData = TopicSerializer(data = request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializedData.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def topic_details(request, pk):
    try:
        topic_name = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializedData = TopicSerializer(topic_name, data=request.data, context={'request': request})
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=HTTP_204_NO_CONTENT)

        return Response(serializedData.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                    
