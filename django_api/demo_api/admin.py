from django.contrib import admin
from demo_api.models import Project, User, Article

# Register your models here.
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Article)