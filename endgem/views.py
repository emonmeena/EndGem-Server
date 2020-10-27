from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def courses(request):
    if request.method == 'GET':
        courseList = Course.objects.all()

        serializedData = CourseSerializers(courseList, context = {'request': request}, many=True)

        return Response(serializedData.data)

@api_view(['GET'])
def material(request, courseID):
    if request.method == 'GET':
        materialList = Material.objects.filter(course=courseID)

        serializedData = MaterialSerializers(materialList, context = {'request': request}, many=True)

        return Response(serializedData.data)

@api_view(['GET', 'POST'])
def materialList(request):
    if request.method == 'GET':
        materialList = Material.objects.all()

        serializedData = MaterialSerializers(materialList, many=True)
        return Response(serializedData.data)

    elif request.method == 'POST':
        serializedData = MaterialSerializers(data=request.data)

        if serializedData.is_valid():
            serializedData.save()
            return Response(status=HTTP_201_CREATED)

        return Response(serializedData.errors, status = HTTP_400_BAD_REQUEST)     
