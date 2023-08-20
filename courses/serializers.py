from django.conf import settings
from rest_framework import serializers
from .models import Course,Branche,Path
from rest_framework import serializers
from tasks.models import Task
from tasks.serializers import *
#,Title,Text,Picture,Video,File,Question
from django.db import transaction

        
class CoursesSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField()
    tasks = TaskSerializer(many=True, read_only=True, source='course_tasks')
    class Meta:
        model = Course
        fields = [
            "id",
            "branche",
            "name",
            "description",
            "picture",
            "instructor",
            "tasks"
        ]
    def get_instructor(self, instance):
        return instance.instructor.username

class CourseSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, source='course_tasks')
    instructor = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            "branche",
            "name",
            "description",
            "picture",
            "instructor",
            "tasks"
        ]
    def get_instructor(self, instance):
        if instance.instructor:
            return instance.instructor.username
        else :
            return 0
class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branche
        fields = '__all__'   

class BrancheSerializer(serializers.ModelSerializer):
    courses=CoursesSerializer(many=True, read_only=True,source='in_the_branche')
    class Meta:
        model = Branche
        fields = ['path','name','description','picture','courses']  
        
class PathsSerializer (serializers.ModelSerializer):
    chef = serializers.SerializerMethodField()
    class Meta:
        model = Path
        fields = ['name','description','picture','chef']
    def get_chef(self, instance):
        return instance.chef.username

class PathSerializer(serializers.ModelSerializer):
    branches = BranchesSerializer(many=True, read_only=True,source='in_the_path')  
    chef = serializers.SerializerMethodField()
    class Meta:
        model = Path
        fields = ['name','description','picture','chef','branches'] 
    
    def get_chef(self, instance):
        return instance.chef.username
    
    
    
   #################################################

class CreateCourseSerializer(serializers.ModelSerializer):
    tasks = CreateTaskSerializer(many=True,source="course_tasks")
    class Meta:
        model = Course
        fields = ['branche','name', 'description','picture',  'tasks']
        
    @transaction.atomic
    def create(self, validated_data):
        #create course
        branche_id = validated_data.pop('branche')
        name_instace = validated_data.pop('name')
        description_instace = validated_data.pop('description')
        picture_distance = validated_data.pop('picture')
        user = self.context['request'].user
        course = Course.objects.create(branche=branche_id,
                                       name=name_instace,
                                       description=description_instace,
                                       picture=picture_distance,
                                       instructor=user)
        
        #create tasks
        i=0
        tasks_data = validated_data.pop('course_tasks')
        for task_data in tasks_data:
            i+=1
            task_name = task_data.pop('name')
            task_number = task_data.pop('number')
            if task_number != i:
                raise serializers.ValidationError("Task numbers must be in order.")
            task = Task.objects.create(name=task_name,number=task_number,course=course)
            
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
                
        
        return course
