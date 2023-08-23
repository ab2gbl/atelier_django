from rest_framework import serializers, validators
from .models import Instructor,Developer,Admin,Company,User
#,Title,Text,Picture,Video,File,Question


       

from rest_framework import serializers

        
class InstructorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Instructor
        fields = ['username', 'password', 'email']  # Include other fields as needed

    def create(self, validated_data):
        password = validated_data.pop('password')
        instructor = Instructor.objects.create(**validated_data)
        instructor.set_password(password)
        instructor.save()
        return instructor

class DeveloperRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Developer
        fields = ['username', 'password', 'email']  # Include other fields as needed

    def create(self, validated_data):
        password = validated_data.pop('password')
        developer = Developer.objects.create(**validated_data)
        developer.set_password(password)
        developer.save()
        return developer
        
class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Admin
        fields = ['username', 'password', 'email']  # Include other fields as needed

    def create(self, validated_data):
        password = validated_data.pop('password')
        admin = Admin.objects.create(**validated_data)
        admin.set_password(password)
        admin.save()
        return admin
        
class CompanyRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Company
        fields = ['username', 'password', 'email']  # Include other fields as needed

    def create(self, validated_data):
        password = validated_data.pop('password')
        company = Company.objects.create(**validated_data)
        company.set_password(password)
        company.save()
        return company
        
from rest_framework import serializers
from .models import User

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)  # This hashes the password
        user.save()
        return user
