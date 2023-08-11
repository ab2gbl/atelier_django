from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/',include('courses.urls')),
    path('challenges/',include('challenges.urls')),
    path('tasks/',include('tasks.urls')),
    path('users/',include('users.urls')),
]