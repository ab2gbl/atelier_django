from django.conf import settings
from rest_framework import serializers

from tasks.serializers import QuestionSerializer
from .models import *
from rest_framework.response import Response
 
#########################################################
class Course_ParticipationSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    course = serializers.CharField(read_only=True)
    course_name = serializers.CharField(write_only=True)
    developer = serializers.CharField(read_only=True)
    is_finished = serializers.BooleanField(read_only=True)
    class Meta:
        model = Course_Participation
        fields = ['id', 'course','course_name' ,'developer','is_finished' ,'tasks']
    def create(self, validated_data):
        course_name = validated_data.pop('course_name')
        course = Course.objects.get(name=course_name)
        developer = user = self.context['request'].user
        participation, created = Course_Participation.objects.get_or_create(course=course, developer=developer)

        return participation
    
    def get_course(self,instance):
        return instance.course.name
    def get_developer(self,instance):
        return instance.developer.username
    def get_tasks(self, instance):
        tasks = instance.course.course_tasks.all()
        ordered_tasks = sorted(tasks, key=lambda task: task.id)
        task_data = []

        for task in ordered_tasks:
            answers = Course_Answer.objects.filter(participation=instance, question__content__task=task)
            answers_data = []

            for answer in answers:
                question_data = QuestionSerializer(answer.question).data
                answers_data.append(question_data)

            task_data.append({
                'task': task.id,
                'task_name': task.name,
                'answers': answers_data
            })

        return task_data


class Course_AnswerSerializer(serializers.ModelSerializer):
    answer= serializers.CharField(write_only=True)
    #task = serializers.UUIDField(read_only=True,source='question.content.task.id')
    question_id= serializers.UUIDField(write_only=True)
    message=serializers.CharField(read_only=True)
    class Meta:
        model = Course_Answer
        fields = ['question_id','answer','message']
    
    def create(self, validated_data):
        user = self.context['request'].user
        question_id = validated_data['question_id']
        question= Question.objects.get(id=question_id)
        
        existing_answer = Course_Answer.objects.filter(participation__developer=user, question=question).first()
        if existing_answer:
            return {"message" : "You already answered this question."}

        answer=validated_data['answer']
        if (answer!=question.solution):
            return {"message" : "Incorrect answer"}
        
        course = question.content.task.course
        developer = user = self.context['request'].user
        participation, created = Course_Participation.objects.get_or_create(course=course, developer=developer)
        course_answer=Course_Answer.objects.create(participation=participation,question=question)
        user.points += question.points
        user.save()
        answer_count = participation.course_answers.count()
        
        tasks = course.course_tasks.all()
        question_count = sum(task.contents.filter(content_type='question').count() for task in tasks)
        if question_count==answer_count :
            participation.is_finished=True
            participation.save()
            return {"message": "Congratulations! You completed the course with all correct answers."}
             
        
        return {"message": "Correct answer"}
         
    
    