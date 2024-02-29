from rest_framework import serializers
from demo_api.models import Project, User, Article

class ProjectSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()
    about = serializers.CharField()
    concepts = serializers.CharField(max_length=100)
    github = serializers.URLField()
    image = serializers.URLField()

    def create(self, validated_data):
        """
        Creates a new project and takes validated data as input
        """
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing project, takes teh existing object and the validated data as inputs
        """
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.concepts = validated_data.get('concepts', instance.concepts)
        instance.github = validated_data.get('github', instance.github)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance
    

# Simple User Serializer
class UserSerializer(serializers.Serializer):
    """
    User Serializer with the below fields:
        - name {string}: name of the user
        - email {string}: email of the user
        - projects {list}: list of projects created by the user
        - articles {list}: list of articles created by the user
    """
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    about = serializers.CharField()
    email = serializers.EmailField()
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ['name', 'about', 'email', 'projects', 'articles']

    def create(self, validated_data):
        """
        Creates a new user and takes validated data as input
        """
        instance = User.objects.create(
            name=validated_data['name'],
            about=validated_data['about'],
            email=validated_data['email'],
        )
        instance.projects.set(validated_data['projects'])
        instance.articles.set(validated_data['articles'])
        
        return instance
    
    def update(self, instance, validated_data):
        """
        Update an existing user, takes teh existing object and the validated data as inputs
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.about = validated_data.get('about', instance.about)
        instance.projects.set( [validated_data.get('projects', instance.projects)] )
        instance.articles.set( [validated_data.get('articles', instance.articles)] )
        instance.save()

        return instance
    
    
    
# Simple Article Serializer
class ArticleSerializer(serializers.Serializer):
    """
    Article Serializer with the below fields:
        - title {string}: title of the article
        - date {date}: date article was added or modified
        - content {string}: content of the article
        - author {string}: author of the article
        - image {url}: the link to the demo image
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()
    content = serializers.CharField()
    image = serializers.URLField()

    def create(self, validated_data):
        """
        Creates a new article and takes validated data as input
        """
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing article, takes teh existing object and the validated data as inputs
        """
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance