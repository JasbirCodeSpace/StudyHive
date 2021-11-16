from django.urls import path
from resource.views import request, upload, resources


urlpatterns = [
    path('', resources.show_resources, name = 'resources'),
    path('request/', request.request_resource, name='resource-request'),
    path('upload/', upload.upload_resource, name='resource-upload'),
]