from django.urls import path
from resource.views import request, upload, resources


urlpatterns = [
    path('', resources.resources_view, name = 'resources'),
    path('fetch/', resources.fetch_resources, name = 'fetch-resources'),
    path('request/', request.request_resource, name='resource-request'),
    path('upload/', upload.upload_resource, name='resource-upload'),
]