from rest_framework import serializers
from .models import *

from tasks.serializers import *
from django.db import transaction
#,Title,Text,Picture,Video,File,Question


       

from rest_framework import serializers

class ChallengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

    def validate(self, data):
        instructor = data.get('instructor')
        company = data.get('company')
        challenge_type = data.get('challenge_type')

        if instructor and company:
            raise serializers.ValidationError("A Challenge cannot have both an Instructor and a Company associated.")
        
        if challenge_type=='COMPETITION' and not instructor:
            raise serializers.ValidationError("A competition need an Instructor.")
        
        if challenge_type=='JOB' and not company:
            raise serializers.ValidationError("A job need a Company.")
        
        
        return data
    
class ChallengeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True,source="challenge_tasks")  
    
    class Meta:
        model = Challenge
        fields = ["id","name","description","picture","max_participants","challenge_type","instructor","company","tasks"]



class CreateCompetitionSerializer(serializers.ModelSerializer):
    tasks = CreateTaskSerializer(many=True,source="challenge_tasks")
    class Meta:
        model = Competition
        fields = ['name', 'description','picture','max_participants',  'tasks']
        
    @transaction.atomic
    def create(self, validated_data):
        #create course
        name_instace = validated_data.pop('name')
        description_instace = validated_data.pop('description')
        picture_distance = validated_data.pop('picture')
        max_participants_distance = validated_data.pop('max_participants') 
        user = self.context['request'].user
        challenge = Competition.objects.create(name=name_instace,
                                       description=description_instace,
                                       picture=picture_distance,
                                       max_participants=max_participants_distance,
        instructor=user)
        
        #create tasks
        i=0
        tasks_data = validated_data.pop('challenge_tasks')
        for task_data in tasks_data:
            i+=1
            task_name = task_data.pop('name')
            task_number = task_data.pop('number')
            if task_number != i:
                raise serializers.ValidationError("Task numbers must be in order.")
            task = Task.objects.create(name=task_name,number=task_number,challenge=challenge)
            
            # create content
            j=0
            contents_data = task_data.pop('contents')
            for content_data in contents_data:
                j+=1
                content_type = content_data.pop('content_type')
                index = content_data.pop('index')
                if index != j:
                    raise serializers.ValidationError("contents indexes must be in order.")
                content = Content.objects.create(task=task, index=index, content_type=content_type)
                #title
                if content_type == 'title':
                    title_data = content_data.pop('title')
                    Title.objects.create(content=content, title=title_data)
                #text
                elif content_type == 'text':
                    text_data = content_data.pop('text')
                    Text.objects.create(content=content, text=text_data)
                #picture
                elif content_type == 'picture':
                    picture_data = content_data.pop('picture')
                    Picture.objects.create(content=content, picture=picture_data)
                #video
                elif content_type == 'video':
                    video_data = content_data.pop('video')
                    Video.objects.create(content=content, video=video_data)
                #file
                elif content_type == 'file':
                    file_data = content_data.pop('file')
                    File.objects.create(content=content, file=file_data)
                #question
                elif content_type == 'question':
                    question_data = content_data.pop('question')
                    solution_data = content_data.pop('solution')
                    hint_data = content_data.pop('hint')
                    points_data = content_data.pop('points')
                    Question.objects.create(content=content, question=question_data,solution=solution_data,hint=hint_data,points=points_data)
                
        
        return challenge



class CreateJobSerializer(serializers.ModelSerializer):
    tasks = CreateTaskSerializer(many=True,source="challenge_tasks")
    class Meta:
        model = Job
        fields = ['name', 'description','picture','max_participants',  'tasks']
        
    @transaction.atomic
    def create(self, validated_data):
        #create course
        name_instace = validated_data.pop('name')
        description_instace = validated_data.pop('description')
        picture_distance = validated_data.pop('picture')
        max_participants_distance = validated_data.pop('max_participants') 
        user = self.context['request'].user
        challenge = Job.objects.create(name=name_instace,
                                       description=description_instace,
                                       picture=picture_distance,
                                       max_participants=max_participants_distance,
        company=user)
        
        #create tasks
        i=0
        tasks_data = validated_data.pop('challenge_tasks')
        for task_data in tasks_data:
            i+=1
            task_name = task_data.pop('name')
            task_number = task_data.pop('number')
            if task_number != i:
                raise serializers.ValidationError("Task numbers must be in order.")
            task = Task.objects.create(name=task_name,number=task_number,challenge=challenge)
            
            # create content
            j=0
            contents_data = task_data.pop('contents')
            for content_data in contents_data:
                j+=1
                content_type = content_data.pop('content_type')
                index = content_data.pop('index')
                if index != j:
                    raise serializers.ValidationError("contents indexes must be in order.")
                content = Content.objects.create(task=task, index=index, content_type=content_type)
                #title
                if content_type == 'title':
                    title_data = content_data.pop('title')
                    Title.objects.create(content=content, title=title_data)
                #text
                elif content_type == 'text':
                    text_data = content_data.pop('text')
                    Text.objects.create(content=content, text=text_data)
                #picture
                elif content_type == 'picture':
                    picture_data = content_data.pop('picture')
                    Picture.objects.create(content=content, picture=picture_data)
                #video
                elif content_type == 'video':
                    video_data = content_data.pop('video')
                    Video.objects.create(content=content, video=video_data)
                #file
                elif content_type == 'file':
                    file_data = content_data.pop('file')
                    File.objects.create(content=content, file=file_data)
                #question
                elif content_type == 'question':
                    question_data = content_data.pop('question')
                    solution_data = content_data.pop('solution')
                    hint_data = content_data.pop('hint')
                    points_data = content_data.pop('points')
                    Question.objects.create(content=content, question=question_data,solution=solution_data,hint=hint_data,points=points_data)
                
        
        return challenge
