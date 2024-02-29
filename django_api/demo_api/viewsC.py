from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import schemas
from rest_framework.response import Response
from rest_framework.views import APIView

from demo_api.models import Project, User, Article
from demo_api.serializers import ProjectSerializer, UserSerializer, ArticleSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 

import json

json_renderer = JSONRenderer()
json_parser = JSONParser()

def homepage(request):
    return HttpResponse("<h2>Homepage</h2>")

# class ProjectDetails(APIView):



@api_view(['GET', 'PUT', 'DELETE'])
def project_details(request, pk):
    """
    View function to retrieve a single project
    """

    try:
        project = Project.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ProjectSerializer(project, many=False)
        json_data = json_renderer.render(serializer.data)
        # return HttpResponse(json_data)
        return Response(json_data)
    
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=204)
    
    else:
        return HttpResponse(status=400)
    

@api_view(['GET', 'POST'])
def project_list(request):
    """
    View function to retrieve all projects
    """
    json_renderer = JSONRenderer()

    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        json_data = json_renderer.render(serializer.data)

        return HttpResponse(json_data)
    
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = json_renderer.render(serializer.data)
            return HttpResponse(json_data, status=201)
        return HttpResponse(serializer.errors, status=400)
    
    else:
        return HttpResponse(status=400)
    

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    """
    View function to retrieve a single user
    """

    try:
        user = User.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        json_data = json_renderer.render(serializer.data)
        return HttpResponse(json_data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = json_parser.parse(serializer.data)
            return HttpResponse(json_data, status=201)
        
        return HttpResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
    
    else:
        return HttpResponse(status=400)


@api_view(['GET', 'POST'])
def user_list(request):
    """
    View function to retrieve all users
    """
    try:
        users = User.objects.all()
    except:
        return HttpResponse(status=404)
    

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        json_data = json_renderer.render(serializer.data)

        return HttpResponse(json_data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = json_parser.parse(serializer.data)
            return HttpResponse(json_data, status=201)
        return HttpResponse(serializer.errors, status=400)
    
    else:
        return HttpResponse(status=400)
    

@api_view(['GET', 'PUT', 'DELETE'])
def article(request, pk):
    """
    View function to retrieve a single article
    """

    try:
        article = Article.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article, many=False)
        json_data = json_renderer.render(serializer.data)
        return HttpResponse(json_data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = json_parser.parse(serializer.data)
            return HttpResponse(json_data)
        return HttpResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
    
    else:
        return HttpResponse(status=400)
    

@api_view(['GET', 'POST'])
def article_list(request):
    """
    View function to retrieve all articles
    """
    
    try:
        articles = Article.objects.all()
    except:
        return HttpResponse(status=404)
    

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        json_data = json_renderer.render(serializer.data)

        return HttpResponse(json_data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = json_parser.parse(serializer.data)
            return HttpResponse(json_data, status=201)
        return HttpResponse(serializer.errors, status=400)
    
    else:
        return HttpResponse(status=400)