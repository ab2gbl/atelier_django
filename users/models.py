from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Properly hash the password
        user.save(using=self._db)
        return user
    
class User(AbstractUser):
    objects = CustomUserManager()
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DEVELOPER = 'DEVELOPER', 'Developer'
        INSTRUCTOR = 'INSTRUCTOR','Instructor'
        COMPANY = 'COMPANY','Company'
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    base_role=Role.ADMIN 
    role = models.CharField(max_length=50, choices=Role.choices, blank=True)  # Allow the role field to be blank
    points= models.PositiveIntegerField(default=0)
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
    def create_instructor(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        instructor = self.model(username=username, email=email, **extra_fields)
        instructor.set_password(password)  # Hashes the password
        instructor.save(using=self._db)
        return instructor
        
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
    def create_company(self, username, email, password=None, **extra_fields):
        
        company = self.model(username=username, email=email, **extra_fields)
        company.set_password(password)  # Hashes the password
        company.save(using=self._db)
        return company
        
class Company(User):
    base_role = User.Role.COMPANY
    student=CompanyManager()
    class Meta:
        proxy = True
        
        
        
@receiver(post_save, sender=Developer)
def TokenCreateForDeveloper(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=Instructor)
def TokenCreateForInstructor(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        