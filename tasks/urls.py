
from django.urls import path,include
from . import views

urlpatterns = [
    path('tasks/', views.Tasks.as_view()),
    path('task/<int:pk>', views.Task.as_view()),
    
    
]
