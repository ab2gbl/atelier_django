
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
    path('create_path_instructor/', views.CreatePath_Instructor.as_view()),
    path('path_instructor/<uuid:pk>/', views.Path_Instructor.as_view()),
    path('path_instructors/<str:path_name>/', views.Path_Instructors.as_view()),
    path('instructor_paths/<str:instructor_username>/', views.Instructor_Paths.as_view()),
    
    
]
