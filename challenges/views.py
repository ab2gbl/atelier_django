from django.http import Http404
from django.shortcuts import render

from .models import Challenge
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import ChallengeSerializer,ChallengesSerializer
#,TextSerializer,TitleSerializer,PictureSerializer,VideoSerializer,FileSerializer,QuestionSerializer

# Create your views here.
class Challenges(generics.ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengesSerializer
class Challenge(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

