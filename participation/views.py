from django.shortcuts import render

from rest_framework import status,filters,generics
from .serializers import *
from . import models as md

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from .permission import *
from rest_framework.decorators import permission_classes, authentication_classes

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample,OpenApiResponse
from drf_spectacular.types import OpenApiTypes

# Create your views here.
@extend_schema(
    description='this api allows to the user to participate or get his participation, and the admin to get all courses participations' ,
            
    request=Course_ParticipationSerializer,
    responses={
        200: OpenApiResponse(
            description="course participation of user",
            examples=[
                    OpenApiExample(
                        'Example 1',
                        summary='response example',
                        description="""
                            We have on this participation:
                            - The course and the developer first.
                            - `is_finished` indicates whether the developer has finished the course or not yet.
                            - Then, the tasks of this course.
                            - For each task, there are the questions that the developer has already answered.
                            """,
                        value={
                            "id": "Course_participation uuid",
                            "course": "course name",
                            "developer": "developer",
                            "is_finished": False,
                            "tasks": [
                                {
                                    "task": "task_id_here",
                                    "task_name": "1-1-3-1",
                                    "answers": [
                                        {
                                            "question": "qst",
                                            "solution": "slt",
                                            "hint": "hint",
                                            "points": 15
                                        }
                                    ]
                                }
                            ]
                        }
                    ),
                    
                ],
            response= Course_ParticipationSerializer
        )
    }
    
)
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

@extend_schema(
    description="This api allow to the developer to answer a question of a course that it he didn't aswer before",
    responses={
        201:OpenApiResponse(
            description="""
            The response can be one of 3 messages:
            - "You already answered this question."
            - "message" : "Incorrect answer"
            - "Congratulations! You completed the course with all correct answers."
            - "Correct answer"
            """,
            response=Course_AnswerSerializer
        )
    }
)   
class Course_Answer(generics.CreateAPIView):
    queryset = md.Course_Answer.objects.all()
    serializer_class = Course_AnswerSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsDeveloper]