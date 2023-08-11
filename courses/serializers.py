from django.conf import settings
from rest_framework import serializers
from .models import Course,Branche,Path
from rest_framework import serializers
from tasks.models import Task
from tasks.serializers import TaskSerializer
#,Title,Text,Picture,Video,File,Question


        
class CoursesSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            "branche",
            "name",
            "description",
            "picture",
            "instructor",
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
        return instance.instructor.username
      
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