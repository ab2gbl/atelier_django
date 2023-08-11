from django.shortcuts import render

from .models import Instructor,Admin,Developer,Company
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import InstructorSerializer,AdminSerializer,DeveloperSerializer,CompanySerializer#,TextSerializer,TitleSerializer,PictureSerializer,VideoSerializer,FileSerializer,QuestionSerializer

# Create your views here.
class Instructor(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
class Admin(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
class Developer(generics.CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
class Company(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
