from django.db import models
from django.core.exceptions import ValidationError
from courses.models import Course
from challenges.models import Challenge
import uuid

class Task(models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
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

class Content(models.Model):
    TYPE_CHOICES = [
        ('title','Title'),
        ('text', 'Text'),
        ('picture', 'Picture'),
        ('video', 'Video'),
        ('file','File'),
        ('question','Question')
        # Add more content types if needed
    ]
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    task = models.ForeignKey(Task, related_name="contents", on_delete=models.CASCADE)
    content_type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    index = models.IntegerField()
    
    class Meta:
        unique_together = ('task', 'index')
    
    def __str__(self):
        return f"Content {self.index} of Task {self.task.name}"
    
class Title (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    title = models.CharField(max_length=50)
    content = models.OneToOneField(Content, on_delete=models.CASCADE,related_name="content_title")
    def __str__(self):		 	
        return str(self.content)
    def save(self, *args, **kwargs):
        if self.content.content_type!='title' :
            raise ValueError("The content is not of type Title")
        super(Title, self).save(*args, **kwargs) 
    
class Text (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    text = models.TextField()
    content = models.OneToOneField(Content, on_delete=models.CASCADE,related_name="content_text")
    def __str__(self):		 	
        return str(self.content)
    def save(self, *args, **kwargs):
        if self.content.content_type!='text' :
            raise ValueError("The content is not of type Text")
        super(Text, self).save(*args, **kwargs) 
    
class Picture (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    picture = models.ImageField(upload_to='photos/')
    content = models.OneToOneField(Content, on_delete=models.CASCADE,related_name="content_picture")
    def __str__(self):		 	
        return str(self.content)
    def save(self, *args, **kwargs):
        if self.content.content_type!='picture' :
            raise ValueError("The content is not of type Picture")
        super(Picture, self).save(*args, **kwargs) 
    
class Video (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    video = models.FileField(upload_to='videos/') 
    content = models.OneToOneField(Content, on_delete=models.CASCADE,related_name="content_video")
    def __str__(self):		 	
        return str(self.content)
    def save(self, *args, **kwargs):
        if self.content.content_type!='video' :
            raise ValueError("The content is not of type Video")
        super(Video, self).save(*args, **kwargs) 
    
class File (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    file =  models.FileField(upload_to='files/') 
    content = models.OneToOneField(Content, on_delete=models.CASCADE,related_name="content_file")
    def __str__(self):		 	
        return str(self.content)
    def save(self, *args, **kwargs):
        if self.content.content_type!='file' :
            raise ValueError("The content is not of type File")
        super(File, self).save(*args, **kwargs) 
    
class Question (models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    question = models.TextField()
    solution = models.CharField(max_length=100)
    hint = models.TextField()
    points = models.IntegerField(default=0)
    content = models.OneToOneField(Content, on_delete=models.CASCADE,related_name="content_question")
    def __str__(self):		 	
        return str(self.content)
    def save(self, *args, **kwargs):
        if self.content.content_type!='question' :
            raise ValueError("The content is not of type Question")
        super(Question, self).save(*args, **kwargs) 
    
