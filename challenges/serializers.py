from rest_framework import serializers
from .models import Challenge

from tasks.serializers import TaskSerializer
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
    tasks = TaskSerializer(many=True, read_only=True)  
    
    class Meta:
        model = Challenge
        fields = '__all__'

