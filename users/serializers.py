from rest_framework import serializers
from .models import Instructor,Developer,Admin,Company
#,Title,Text,Picture,Video,File,Question


       

from rest_framework import serializers

        
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
        "password",
        "username",
        "first_name",
        "last_name",
        "email",
        ]

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = [
        "password",
        "username",
        "first_name",
        "last_name",
        "email",
        ]

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = [
        "password",
        "username",
        "first_name",
        "last_name",
        "email",
        ]
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
        "password",
        "username",
        "first_name",
        "last_name",
        "email",
        ]



