from django.http import Http404
from django.shortcuts import render
from .models import Course,Branche,Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import *
from rest_framework.response import Response
from .models import Course
from . import models as md

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from .permission import *
    

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
class Courses(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    
   
class CreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInPath]
    
class Course(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication]
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthorOrChefOrAdmin]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

#Path_Instructors
class CreatePath_Instructor(generics.CreateAPIView):
    queryset = Path_Instructor.objects.all()
    serializer_class = Path_InstructorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsChefOrAdminCreate]

class Path_Instructor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Path_Instructor.objects.all()
    serializer_class = Path_InstructorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsChefOrAdmin]


class Path_Instructors(generics.ListAPIView):
    serializer_class = Path_InstructorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        path_name = self.kwargs['path_name']
        return md.Path_Instructor.objects.filter(path__name=path_name)


class Instructor_Paths(generics.ListAPIView):
    serializer_class = Path_InstructorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        instructor_username = self.kwargs['instructor_username']
        return md.Path_Instructor.objects.filter(instructor__username=instructor_username)

