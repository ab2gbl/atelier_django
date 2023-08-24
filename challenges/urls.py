
from django.urls import path,include
from . import views
urlpatterns = []
'''
urlpatterns = [
    path('challenges/', views.Challenges.as_view()),
    #path('tasks/', views.Tasks.as_view()),
    path('challenge/<uuid:pk>/', views.Challenge.as_view()),
    path('createcompetition/', views.CreateCompetition.as_view()),
    path('createjob/', views.CreateJob.as_view()),
    
]

    '''