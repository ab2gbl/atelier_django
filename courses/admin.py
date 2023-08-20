from django.contrib import admin
from .models import *

admin.site.register(Path)
admin.site.register(Branche)
admin.site.register(Course)
admin.site.register(Path_Instructor)

