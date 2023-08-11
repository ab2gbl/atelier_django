from django.http import Http404
from django.shortcuts import render
from .models import Course,Branche,Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import CourseSerializer,CoursesSerializer,PathSerializer,PathsSerializer,BrancheSerializer,BranchesSerializer
#,TextSerializer,TitleSerializer,PictureSerializer,VideoSerializer,FileSerializer,QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
# Path
class Paths(generics.ListCreateAPIView):
    queryset = Path.objects.all()
    serializer_class = PathsSerializer

class Path(generics.RetrieveUpdateDestroyAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
# Branche
class Branches(generics.ListCreateAPIView):
    queryset = Branche.objects.all()
    serializer_class = BranchesSerializer

class Branche(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branche.objects.all()
    serializer_class = BrancheSerializer
# Course.
class Courses(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

class Course(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

