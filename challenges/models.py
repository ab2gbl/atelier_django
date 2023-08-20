from django.db import models
from users.models import Instructor,Company
import uuid
# Create your models here.
class Challenge (models.Model):
    
    class Type(models.TextChoices):
        JOB = 'JOB', 'Job'
        COMPETITION = 'COMPETITION', 'Competition'
    base_type=Type.COMPETITION
    
    id=models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
        
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(upload_to='photos/courses/')
    instructor=models.ForeignKey(Instructor, related_name='competition_of',on_delete=models.CASCADE,null=True,blank=True)	
    company=models.ForeignKey(Company, related_name='job_of',on_delete=models.CASCADE,null=True,blank=True)	
    max_participants=models.IntegerField()
    challenge_type = models.CharField(max_length=50, choices=Type.choices, blank=True)  # Allow the role field to be blank
    
    def __str__(self):			
        return self.name

    def save(self, *args, **kwargs):
        if self.instructor and self.company:
            raise ValueError("A Challenge cannot have both a instructor and a company associated.")
        if not self.challenge_type:  # Check if the role field is empty
            self.challenge_type = self.base_type
        super(Challenge, self).save(*args, **kwargs) 

class JobManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(challenge_type=Challenge.Type.JOB)

class Job(Challenge):
    base_type = Challenge.Type.JOB
    objects = JobManager()

    class Meta:
        proxy = True
    

class CompetitionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(challenge_type=Challenge.Type.COMPETITION)

class Competition(Challenge):
    base_type = Challenge.Type.COMPETITION
    objects = CompetitionManager()

    class Meta:
        proxy = True
