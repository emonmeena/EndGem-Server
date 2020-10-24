from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST'])
def courses(request):
    if request.method == 'GET':
        courseList = Course.objects.all()

        serializedData = CourseSerializers(courseList, context = {'request': request}, many=True)

        return Response(serializedData.data)

@api_view(['GET', 'POST'])
def materials(request):
    if request.method == 'GET':
        materialList = Material.objects.all()

        serializedData = MaterialSerializers(materialList, context = {'request': request}, many=True)

        return Response(serializedData.data)
