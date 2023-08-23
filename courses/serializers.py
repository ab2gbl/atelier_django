from django.conf import settings
from rest_framework import serializers
from .models import *
from rest_framework import serializers
from tasks.models import Task
from tasks.serializers import *
#,Title,Text,Picture,Video,File,Question
from django.db import transaction
from users.serializers import InstructorRegistrationSerializer

        
class CoursesSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField(read_only=True)
    #tasks = TaskSerializer(many=True, read_only=True, source='course_tasks')
    class Meta:
        model = Course
        fields = [
            "id",
            "branche",
            "name",
            "description",
            "picture",
            "instructor",
            #"tasks"
        ]
    def get_instructor(self, instance):
        return instance.instructor.username

class CourseSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, source='course_tasks')
    instructor = serializers.SerializerMethodField(read_only=True)
    branche = serializers.PrimaryKeyRelatedField(queryset=Branche.objects.all(), required=False)
    name=serializers.CharField(required=False)
    description=serializers.CharField(required=False)
    picture=serializers.ImageField(required=False)
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
    chef_username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Path
        fields = ['id','name','description','picture','chef','chef_username']
    def get_chef_username(self, instance):
        return instance.chef.username
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.context['request'].method in ('GET', 'PUT', 'PATCH'):
            data.pop('chef')
        return data
    
    def create(self, validated_data):
        path=Path.objects.create(**validated_data)
        path_instructor_data = {
            'instructor': path.chef,  
            'path': path
        }
        Path_Instructor.objects.create(**path_instructor_data)
        return path   

class PathSerializer(serializers.ModelSerializer):
    branches = BranchesSerializer(many=True, read_only=True,source='in_the_path')  
    chef_username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Path
        fields = ['id','name','description','picture','chef','chef_username','branches'] 
    def get_chef_username(self, instance):
        return instance.chef.username
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.context['request'].method in ('GET', 'PUT', 'PATCH'):
            data.pop('chef')
        return data

    
   
    
#################################################

class CreateCourseSerializer(serializers.ModelSerializer):
    tasks = CreateTaskSerializer(many=True,source="course_tasks")
    branche_id=serializers.UUIDField(write_only=True)
    branche=serializers.UUIDField(read_only=True)
    class Meta:
        model = Course
        fields = ['branche','branche_id','name', 'description','picture',  'tasks']
        
    @transaction.atomic
    def create(self, validated_data):
        #create course
        branche_id = validated_data.pop('branche_id')
        branche=Branche.objects.get(id=branche_id)
        name_instace = validated_data.pop('name')
        description_instace = validated_data.pop('description')
        picture_distance = validated_data.pop('picture')
        user = self.context['request'].user
        course = Course.objects.create(branche=branche,
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

class Path_InstructorSerializer(serializers.ModelSerializer):
    instructor_username = serializers.CharField(write_only=True)
    instructor = serializers.CharField(read_only=True)
    
    path = serializers.CharField(read_only=True)
    path_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = Path_Instructor
        fields = ['id','instructor','instructor_username','path','path_name']  
    def get_instructor(self, instance):
        return instance.instructor.username
    def get_path(self, instance):
        return instance.path.name
    def create(self, validated_data):
        instructor_username = validated_data.pop('instructor_username')
        path_name = validated_data.pop('path_name')

        instructor = Instructor.objects.get(username=instructor_username)
        path = Path.objects.get(name=path_name)

        path_instructor,created = Path_Instructor.objects.get_or_create(instructor=instructor,path=path)
        return path_instructor
    
#########################################################