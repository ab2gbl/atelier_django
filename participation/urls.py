
from django.urls import path,include
from . import views

urlpatterns = [
    path('course_participation/', views.Course_participation.as_view()),
    path('course_answer/',views.Course_Answer.as_view())
]
