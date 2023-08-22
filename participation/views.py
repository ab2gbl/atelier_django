from django.shortcuts import render

from rest_framework import status,filters,generics
from .serializers import *
from . import models as md

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from .permission import *


# Create your views here.
class Course_participation(generics.ListCreateAPIView):
    queryset = md.Course_Participation.objects.all()
    serializer_class = Course_ParticipationSerializer
    authentication_classes = [TokenAuthentication]
    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = [IsAdminUser]
        if self.request.method in ['POST']:
            self.permission_classes = [IsDeveloper]
        return super().get_permissions()
    
class Course_Answer(generics.CreateAPIView):
    queryset = md.Course_Answer.objects.all()
    serializer_class = Course_AnswerSerializer
    permission_classes=[IsDeveloper]