from django.http import Http404
from django.shortcuts import render

from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,filters,generics
from .serializers import *

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from .permission import *
# Create your views here.
class Challenges(generics.ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengesSerializer
class Challenge(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class CreateCompetition(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CreateCompetitionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInstructor]
    
class CreateJob(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = CreateJobSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCompany]