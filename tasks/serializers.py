from rest_framework import serializers
from .models import *
#,Title,Text,Picture,Video,File,Question


       

from rest_framework import serializers

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["index","content_type"]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        content_type = representation['content_type']
        
        if content_type == 'title':
            title_content = Title.objects.get(content=instance)
            representation['title'] = title_content.title
        elif content_type == 'text':
            text_content = Text.objects.get(content=instance)
            representation['text'] = text_content.text
        elif content_type == 'picture':
            picture_content = Picture.objects.get(content=instance)
            request = self.context.get('request')
            if request:
                representation['picture_url'] = request.build_absolute_uri(picture_content.picture.url)
        elif content_type == 'video':
            video_content = Video.objects.get(content=instance)
            request = self.context.get('request')
            if request:
                representation['video_url'] = request.build_absolute_uri(video_content.video.url)
        # Add more cases for other content types if needed
        #file
        elif content_type == 'file':
            file_content = File.objects.get(content=instance)
            request = self.context.get('request')
            if request:
                representation['file_url'] = request.build_absolute_uri(file_content.file.url)
        #question
        elif content_type == 'question':
            question_content = Question.objects.get(content=instance)
            representation['question'] = question_content.question  
            representation['solution'] = question_content.solution
            representation['hint'] = question_content.hint
            representation['points'] = question_content.points
        return representation
        
        
class TaskSerializer(serializers.ModelSerializer):
    contents=ContentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ["id","name","number","contents"]

    def validate(self, data):
        course = data.get('course')
        challenge = data.get('challenge')
        if course and challenge:
            raise serializers.ValidationError("A Task cannot have both a Course and a Challenge associated.")
        
        return data

class TasksSerializer(serializers.ModelSerializer):
    contents=ContentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ["id","name","number","course","challenge","contents"]

    def validate(self, data):
        course = data.get('course')
        challenge = data.get('challenge')
        if course and challenge:
            raise serializers.ValidationError("A Task cannot have both a Course and a Challenge associated.")
        
        return data

    

#############################
class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['title']

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['text']

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['picture']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'solution', 'hint', 'points']
############################

'''
class TitleSerializer(serializers.ModelSerializer):
    task=serializers.IntegerField(default=1)
    index = serializers.IntegerField(default=1)
    class Meta:
        model = Title
        fields = ['task','index','title']

    def create(self, validated_data):
        task_id = validated_data.pop('task')
        index = validated_data.pop('index')
        task_instance, _ = Task.objects.get_or_create(number=task_id)
        content = Content.objects.create(task=task_instance, index=index, content_type='title')  # Set the content type
        title = Title.objects.create(content=content, **validated_data)
        return title
'''
class CreateContentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    text = serializers.CharField(style={'base_template': 'textarea.html'},required=False)
    picture = serializers.ImageField(required=False)
    video = serializers.FileField(required=False) 
    file = serializers.FileField(required=False)  
    question = serializers.CharField(required=False)
    solution = serializers.CharField(required=False)
    hint = serializers.CharField(required=False)
    points = serializers.IntegerField(required=False)
    
    class Meta:
        model = Content
        fields = ['content_type', 'index',"title","text","picture","video","file","question","solution","hint","points"]  
    
    def validate(self, attrs):
        content_type = attrs.get('content_type')
        
        if content_type == 'title' and not attrs.get('title'):
            raise serializers.ValidationError({"title": "This field is required for content type 'title'."})
        elif content_type == 'text' and not attrs.get('text'):
            raise serializers.ValidationError({"text": "This field is required for content type 'text'."})
        elif content_type == 'picture' and not attrs.get('picture'):
            raise serializers.ValidationError({"picture": "This field is required for content type 'picture'."})
        elif content_type == 'video' and not attrs.get('video'):
            raise serializers.ValidationError({"video": "This field is required for content type 'video'."})
        elif content_type == 'file' and not attrs.get('file'):
            raise serializers.ValidationError({"file": "This field is required for content type 'file'."})
        
        
        # ... similar checks for other content types ...
        
        return attrs 
      
class CreateTaskSerializer(serializers.ModelSerializer):
    contents = CreateContentSerializer(many=True)

    class Meta:
        model = Task
        fields = ['name', 'number', 'contents']

    def create(self, validated_data):
        contents_data = validated_data.pop('contents')
        task = Task.objects.create(**validated_data)
        
        for content_data in contents_data:
            content_type = content_data.pop('content_type')
            index = content_data.pop('index')
            
            content = Content.objects.create(task=task, index=index, content_type=content_type)
            
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
            
        
        return task
