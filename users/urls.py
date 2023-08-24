
from django.urls import path,include
from . import views

urlpatterns = [
    path('instructor/', views.InstructorRegistrationView.as_view()),
    path('developer/', views.DeveloperRegistrationView.as_view()),
    path('company/', views.CompanyRegistrationView.as_view()),
    path('admin/', views.AdminRegistrationView.as_view()),
    #path('register/', views.CustomUserRegistrationView.as_view(), name='register'),
   
    
    
    
]
