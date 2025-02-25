from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from django.shortcuts import redirect


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from django.views.generic import TemplateView


schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/',include('courses.urls')),
    path('challenges/',include('challenges.urls')),
    path('tasks/',include('tasks.urls')),
    path('users/',include('users.urls')),
    path('participations/',include('participation.urls')),
    path('api-token/',obtain_auth_token),
    
    
    
    #documentation
    #path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('schema/',SpectacularAPIView.as_view(),name="schema"),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('',lambda request: redirect('schema/docs/'),)
    
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
