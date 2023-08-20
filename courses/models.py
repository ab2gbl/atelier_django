from django.db import models
from users.models import Instructor
import uuid 

class Path (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
        
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(upload_to='photos/paths/')
    chef = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_paths')
    def __str__(self):			
        return self.name

class Branche (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
        
    )
    path = models.ForeignKey(Path,related_name='in_the_path',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(upload_to='photos/branches/')
    def __str__(self):			
        return self.name

class Course (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    branche = models.ForeignKey(Branche,related_name='in_the_branche',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='photos/courses/')
    instructor=models.ForeignKey(Instructor, related_name='created_by',on_delete=models.SET_NULL,null=True)	
    def __str__(self)-> str:			
        return self.name


    
class Path_Instructor (models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    user = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    # You can add more fields here, like roles, permissions, etc.

    def __str__(self):
        return f"{self.user.username} - {self.path.name}"