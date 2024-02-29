# Django Rest API

```bash
createsuperuser --username=admin --email=admin@admin.com
```

`password=admin`

## 0. Package installation

**Django Installation** - If you haven't installed Django yet:

```bash
pip install django
```

**Django REST Framework** - For Django REST Framework (DRF), a powerful toolkit for building Web APIs:

```bash
pip install djangorestframework
```

```bash
pip install django-rest-swagger
```

## 1. Understanding RESTful API Principles and Django REST Framework

```python
# Sample Django REST framework view demonstrating REST principles
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SampleAPIView(APIView):
    def get(self, request):
        # Retrieve data from model or other source
        data = {'message': 'This is a GET request'}
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Process incoming data and create resource
        # ... (code to handle POST request)
        return Response({'message': 'Resource created'}, status=status.HTTP_201_CREATED)
    
    # Implement other HTTP methods: PUT, PATCH, DELETE as required
```

## 2. Building Robust API Endpoints

### Authentication and Permissions

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AuthenticatedAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # ... (methods and logic requiring authentication)
```

### Data Serialization (Using DRF Serializers)

```python
from rest_framework import serializers

class SampleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    class Meta:
        model = YourModel
        fields = ['id', 'name', 'email']
    
    def create(self, validated_data):
        return YourModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
```

## 3. Implementing Advanced Features

### Pagination and Filtering

```python
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# In your view
class PaginatedAPIView(APIView):
    pagination_class = CustomPagination
    
    def get(self, request):
        queryset = YourModel.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        # ... (return paginated data)
```

### Tests

```bash
    >>> from demo_api.models import Project
    >>> from demo_api.serializers import ProjectSerializer
    >>> from rest_framework.renderers import JSONRenderer
    >>> from rest_framework.parsers import JSONParser     
    >>> 
    >>> project = Project(name="Coding Django",about="working with DJango API", concepts="Swagger API, REST API, Serializer", github="https://github.com", image="https://home.com/image.png")
    >>> project_0 = Project(name="React Frontend",about="Configuring Frontend Developemnt", concepts="Axios library, Sending Crud requests", github="https://github.com", image="https://home.com/image.png")             
    >>>
    >>> project.save()
    >>> project_0.save() 
    >>> 
    >>> project_slz = ProjectSerializer(project)
    >>> project_0_slz = ProjectSerializer(project_0) 
    >>>
    >>> project_slz.data
    {'name': 'Coding Django', 'date': '2023-12-22T22:53:17.656437Z', 'about': 'working with DJango API', 'concepts': 'Swagger API, REST API, Serializer', 'github': 'https://github.com', 'image': 'https://home.com/image.png'}
    >>> project_0_slz.data 
    {'name': 'React Frontend', 'date': '2023-12-22T22:53:23.286949Z', 'about': 'Configuring Frontend Developemnt', 'concepts': 'Axios library, Sending Crud requests', 'github': 'https://github.com', 'image': 'https://home.com/image.png'}
    >>>
    >>> jsonRenderer  = JSONRenderer()     
    >>> jsonParser  = JSONParser()     
    >>>
    >>> project_content = jsonRenderer.render(project_slz.data)  
    >>> project_0_content = jsonRenderer.render(project_0_slz.data) 
    >>>
    >>> project_content
    b'{"name":"Coding Django","date":"2023-12-22T22:53:17.656437Z","about":"working with DJango API","concepts":"Swagger API, REST API, Serializer","github":"https://github.com","image":"https://home.com/image.png"}'
    >>> project_0_content 
    b'{"name":"React Frontend","date":"2023-12-22T22:53:23.286949Z","about":"Configuring Frontend Developemnt","concepts":"Axios library, Sending Crud requests","github":"https://github.com","image":"https://home.com/image.png"}'
```

```bash
    >>> import io
    >>>
    >>> input_stream = io.BytesIO(project_content) 
    >>> input_stream_0 = io.BytesIO(project_0_content) 
    >>>
    >>> pjt_data = jsonParser.parse(input_stream) 
    >>> pjt_0_data = jsonParser.parse(input_stream_0) 
    >>>
    >>> pjt_data
    {'name': 'Coding Django', 'date': '2023-12-22T22:53:17.656437Z', 'about': 'working with DJango API', 'concepts': 'Swagger API, REST API, Serializer', 'github': 'https://github.com', 'image': 'https://home.com/image.png'}
    >>> pjt_0_data 
    {'name': 'React Frontend', 'date': '2023-12-22T22:53:23.286949Z', 'about': 'Configuring Frontend Developemnt', 'concepts': 'Axios library, Sending Crud requests', 'github': 'https://github.com', 'image': 'https://home.com/image.png'}
    >>>  
    >>> project_slz = ProjectSerializer(data=pjt_data) 
    >>> project_0_slz = ProjectSerializer(data=pjt_0_data) 
    >>>
    >>> project_slz.is_valid()                             
    True
    >>> project_0_slz.is_valid() 
    True
    >>>
    >>> project_slz.validated_data
    OrderedDict({'name': 'Coding Django', 'date': datetime.datetime(2023, 12, 22, 22, 53, 17, 656437, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'about': 'working with DJango API', 'concepts': 'Swagger API, REST API, Serializer', 'github': 'https://github.com', 'image': 'https://home.com/image.png'})
    >>> project_slz.save()        
    <Project: Project object (3)>
    >>> project_0_slz.validated_data 
    OrderedDict({'name': 'React Frontend', 'date': datetime.datetime(2023, 12, 22, 22, 53, 23, 286949, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'about': 'Configuring Frontend Developemnt', 'concepts': 'Axios library, Sending Crud requests', 'github': 'https://github.com', 'image': 'https://home.com/image.png'})
    >>> project_0_slz.save() 
    <Project: Project object (4)>
    >>>
```

### File Uploads

Handling file uploads in the `FileUploadView`:

```python
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        # Handle the file, e.g., save it to the server or process it
        # For instance:
        # file_path = handle_uploaded_file(file_obj)
        return Response({'message': 'File uploaded successfully'}, status=status.HTTP_200_OK)
```

## 4. Optimizing API Performance

### Caching Strategies

Using caching in the `CachedAPIView`:

```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel
from .serializers import SampleSerializer

class CachedAPIView(APIView):
    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request):
        queryset = MyModel.objects.all()
        serializer = SampleSerializer(queryset, many=True)
        return Response(serializer.data)
```
