from django.http import Http404
from django.shortcuts import render

from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import *#,TextSerializer,TitleSerializer,PictureSerializer,VideoSerializer,FileSerializer,QuestionSerializer

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
# Create your views here.
class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    
class Task(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class Content(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class Title(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
