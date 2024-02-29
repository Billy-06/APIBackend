# From Django
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

#  From my project
from demo_api.permissions import *
from demo_api.models import Project, User, Article
from demo_api.serializers import ProjectSerializer, UserSerializer, ArticleSerializer
# Form rest_framework
from rest_framework.authtoken.models import Token
# from rest_framework.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import schemas, viewsets, permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# From Python Libraries
import json
import secrets

json_renderer = JSONRenderer()
json_parser = JSONParser()

def homepage(request):
    return HttpResponse("<h2>Homepage</h2>")

class SignUpAPI(APIView):
    def post(self, request):
        
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Optionally, you can log in the user after registration
        # authenticate(request, username=username, password=password)
        # login(request, user)

        return Response({'success': 'User created successfully', "user": { "email": user.email, "username": user.username }}, status=status.HTTP_201_CREATED)

class LoginAPI(APIView):
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        print(f"username {username}, password: {password}")

        # 1. Option One: Using simple Authentication
        # find the user with the given username
        # user = userList.filter(name=username).first()

        # if user:
        #     if user.password == password:
        #         return Response({'token': secrets.token_urlsafe(16)}, status=200)
        #     else:
        #         return Response({'error': 'Invalid credentials'}, status=400)
        
        # 2. Option Two: Using Django's built-in authentication
        
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            print('Password matches')
            # user = authenticate(username=username, password=password)
            # token, _ = Token.objects.get_or_create(user=user_confirmed)
            # return Response({'token': token.key})
            token = secrets.token_urlsafe(16)
            return Response({'token': token})
        else:
            print('Password does not match')
            return Response({'error': 'Invalid credentials'}, status=400)
        

# Class-based Project Details views implementing, GET, PUT, and DELETE methods
class ProjectDetails(APIView):
    """
    Class-based view to retrieve, update, or delete a single project
    """
    permission_classes = [ProjectPermission]

    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

# Class-based Project List views implementing, GET, and POST methods
class ProjectList(APIView):
    """
    Class-based view to retrieve all projects
    """
    permission_classes = [ProjectPermission]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Class-based User Details views implementing, GET, PUT, and DELETE methods
class UserDetails(APIView):
    """
    Class-based view to retrieve, update, or delete a single user
    """
    permission_classes = [UserPermission]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

# Class-based User List views implementing, GET, and POST methods
class UserList(APIView):
    """
    Class-based view to retrieve all users
    """
    permission_classes = [UserPermission]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class-based Article Details views implementing, GET, PUT, and DELETE methods
class ArticleDetails(APIView):
    """
    Class-based view to retrieve, update, or delete a single article
    """
    permission_classes = [ArticlePermission]

    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Class-based Article List views implementing, GET, and POST methods
class ArticleList(APIView):
    """
    Class-based view to retrieve all articles
    """
    permission_classes = [ArticlePermission]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

