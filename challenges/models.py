from django.db import models
from users.models import Instructor,Company

# Create your models here.
class Challenge (models.Model):
    class Type(models.TextChoices):
        JOB = 'JOB', 'Job'
        COMPETITION = 'COMPETITION', 'Competition'
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(upload_to='photos/courses/')
    instructor=models.ForeignKey(Instructor, related_name='competition_of',on_delete=models.CASCADE,null=True,blank=True)	
    company=models.ForeignKey(Company, related_name='job_of',on_delete=models.CASCADE,null=True,blank=True)	
    max_participants=models.IntegerField()
    challenge_type = models.CharField(max_length=50, choices=Type.choices, blank=False)  # Allow the role field to be blank
    
    def __str__(self):			
        return self.name

    def save(self, *args, **kwargs):
        if self.instructor and self.company:
            raise ValueError("A Challenge cannot have both a instructor and a company associated.")
        super(Challenge, self).save(*args, **kwargs) 