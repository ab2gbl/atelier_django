
from django.urls import path,include
from . import views

urlpatterns = [
    path('challenges/', views.Challenges.as_view()),
    #path('tasks/', views.Tasks.as_view()),
    path('challenge/<int:pk>', views.Challenge.as_view()),
    
    
]
