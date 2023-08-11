from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DEVELOPER = 'DEVELOPER', 'Developer'
        INSTRUCTOR = 'INSTRUCTOR','Instructor'
        COMPANY = 'COMPANY','Company'
    
    base_role=Role.ADMIN 
    role = models.CharField(max_length=50, choices=Role.choices, blank=True)  # Allow the role field to be blank
    
    def save(self, *args, **kwargs):
        if not self.role:  # Check if the role field is empty
            self.role = self.base_role  # Set the default role to ADMIN if not provided
        super().save(*args, **kwargs)

# Admin

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.ADMIN)
        
class Admin(User):
    base_role = User.Role.ADMIN
    student=AdminManager()
    class Meta:
        proxy = True
 
# developer

class DeveloperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.DEVELOPER)
        
class Developer(User):
    base_role = User.Role.DEVELOPER
    student=DeveloperManager()
    
    class Meta:
        proxy = True

#INSTRUCTOR
class InstructorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.INSTRUCTOR)
        
class Instructor(User):
    base_role = User.Role.INSTRUCTOR
    student=InstructorManager()
    class Meta:
        proxy = True

# COMPANY

class CompanyManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.COMPANY)
        
class Company(User):
    base_role = User.Role.COMPANY
    student=CompanyManager()
    class Meta:
        proxy = True