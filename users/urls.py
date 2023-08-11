
from django.urls import path,include
from . import views

urlpatterns = [
    path('instructor/', views.Instructor.as_view()),
    path('developer/', views.Developer.as_view()),
    path('company/', views.Company.as_view()),
    path('admin/', views.Admin.as_view()),
    
    
]
