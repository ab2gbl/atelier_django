from django.http import Http404
from django.shortcuts import render

from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import TaskSerializer#,TextSerializer,TitleSerializer,PictureSerializer,VideoSerializer,FileSerializer,QuestionSerializer

# Create your views here.
class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class Task(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer