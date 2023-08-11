from rest_framework import serializers
from .models import Task
#,Title,Text,Picture,Video,File,Question


       

from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","name","number","course","challenge"]

    def validate(self, data):
        course = data.get('course')
        challenge = data.get('challenge')

        if course and challenge:
            raise serializers.ValidationError("A Task cannot have both a Course and a Challenge associated.")
        
        return data

