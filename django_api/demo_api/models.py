from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

# Project Class Definition
class Project(models.Model):
    """
    Model class representing a project with the below fields:
     - name {string}: name of the project
     - date {date}: date project was added or modified
     - about {string}: What the project is about
     - concepts {string}: concepts covered in the project
     - github {url}: github url
     - image {url}: the link to the demo image
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    about = models.TextField(blank=False, null=False)
    concepts = models.CharField(max_length=200) # Separate values  using the '|' or '\'
    github = models.URLField(blank=False, null=False)
    image = models.URLField(blank=False, null=False)

    class Meta:
        ordering = ['date']
        verbose_name = 'Project'

    def __str__(self) -> str:
        return f"{self.name}"
    
# User Class Definition
class User(AbstractBaseUser, models.Model):
    """
    Model class representing a user with the below fields:
     - username {string}: username of the user
     - email {string}: email of the user
     - password {string}: password of the user
     - projects {list}: list of projects created by the user
     - articles {list}: list of articles created by the user
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    about = models.TextField(blank=False, null=False, default="About section not yet provided")
    password = models.CharField(max_length=100, blank=False, null=False)
    projects = models.ManyToManyField(Project, blank=True)
    articles = models.ManyToManyField('Article', blank=True)
    # is_staff = False
    # is_superuser = False

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        "username",
        "email",
        "password"
    ]

    class Meta:
        ordering = ['username']
        verbose_name = 'User'

    def __str__(self) -> str:
        return f"{self.username}"
    
# Article Class Definition
class Article(models.Model):
    """
    Model class representing an article with the below fields:
     - title {string}: title of the article
     - date {date}: date article was added or modified
     - content {string}: content of the article
     - author {string}: author of the article
     - image {url}: the link to the demo image
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image = models.URLField(blank=False, null=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        ordering = ['date']
        verbose_name = 'Article'

    def __str__(self) -> str:
        return f"{self.title}"