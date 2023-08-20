
from django.urls import path,include
from . import views

urlpatterns = [
    path('tasks/', views.Tasks.as_view()),
    path('task/<int:pk>', views.Task.as_view()),
    path('title/',views.Title.as_view()),
    path('content/',views.Content.as_view()),
    path('createtask/',views.CreateTask.as_view())
]
