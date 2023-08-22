from django.db import models
from users.models import Developer
from courses.models import Course
from tasks.models import Question

import uuid

class Course_Participation(models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer,  on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    class Meta:
        unique_together = [['course', 'developer']]
    def __str__(self):
        return f"{self.developer.username} - {self.course.name}"


# Create your models here.
class Course_Answer(models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    participation=models.ForeignKey(Course_Participation, related_name='course_answers',on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE) 
    class Meta:
        unique_together = [['participation', 'question']]  
    
    def __str__(self):
        return f"{self.participation.developer.username} - {self.question}"
        
     