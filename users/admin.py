from django.contrib import admin
from .models import User,Admin,Developer,Instructor,Company

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)

admin.site.register(Developer)
admin.site.register(Instructor)
admin.site.register(Company)