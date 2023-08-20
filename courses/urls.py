
from django.urls import path,include
from . import views

urlpatterns = [
    path('paths/', views.Paths.as_view()),
    path('path/<uuid:pk>/', views.Path.as_view()),
    path('branches/', views.Branches.as_view()),
    path('branche/<uuid:pk>/', views.Branche.as_view()),
    path('courses/', views.Courses.as_view()),
    path('createcourse/', views.CreateCourse.as_view()),
    path('course/<uuid:pk>/', views.Course.as_view()),
]
