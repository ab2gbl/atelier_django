from django.db import models
from django.core.exceptions import ValidationError
from courses.models import Course
from challenges.models import Challenge

class Task(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    course = models.ForeignKey(Course, related_name="course_tasks", on_delete=models.CASCADE, null=True, blank=True)
    #courses = models.ForeignKey(Course, related_name="course_tasks1", on_delete=models.CASCADE, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, related_name="challenge_tasks", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):			
        return self.name
    class Meta:
        # Define the unique_together constraint to ensure uniqueness of number within the same course or challenge
        unique_together = [['number', 'course'], ['number', 'challenge']]
    def save(self, *args, **kwargs):
        if self.course and self.challenge:
            raise ValueError("A Task cannot have both a Course and a Challenge associated.")
        super(Task, self).save(*args, **kwargs) 
    
class Title (models.Model):
    title = models.CharField(max_length=50)
    index = models.IntegerField()
    task = models.ForeignKey(Task, verbose_name=("of_task"), on_delete=models.CASCADE,null=True,default=None,blank=True)
    def __str__(self):		 	
        return self.task.name + '.' + str(self.index) +'('+self.title+')'
    
class Text (models.Model):
    text = models.TextField()
    index = models.IntegerField()
    task = models.ForeignKey(Task, verbose_name=("of_task"), on_delete=models.CASCADE,null=True,default=None,blank=True)
    def __str__(self):		 	
        return self.task.name + '.' + str(self.index)
    
class Picture (models.Model):
    picture = models.ImageField(upload_to='photos/')
    index = models.IntegerField()
    task = models.ForeignKey(Task, verbose_name=("of_task"), on_delete=models.CASCADE,null=True,default=None,blank=True)
    def __str__(self):		 	
        return self.task.name + '.' + str(self.index)
    
class Video (models.Model):
    video = models.FileField(upload_to='videos/') 
    index = models.IntegerField()
    task = models.ForeignKey(Task, verbose_name=("of_task"), on_delete=models.CASCADE,null=True,default=None,blank=True)
    def __str__(self):		 	
        return self.task.name + '.' + str(self.index)
    
class File (models.Model):
    file =  models.FileField(upload_to='files/') 
    index = models.IntegerField()
    task = models.ForeignKey(Task, verbose_name=("of_task"), on_delete=models.CASCADE,null=True,default=None,blank=True)
    def __str__(self):		 	
        return self.task.name + '.' + str(self.index)
    
class Question (models.Model):
    question = models.TextField()
    solution = models.CharField(max_length=100)
    hint = models.TextField()
    points = models.IntegerField(default=0)
    index = models.IntegerField()
    task = models.ForeignKey(Task, verbose_name=("of_task"), on_delete=models.CASCADE,null=True,default=None,blank=True)
    def __str__(self):		 	
        return self.task.name + '.' + str(self.index)
    