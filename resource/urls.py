from django.urls import path
from resource.views import request, upload, resources


urlpatterns = [
    path('', resources.resources_view, name = 'resources'),
    path('resource-views/', resources.resource_view_count, name = 'resource-views'),
    path('fetch/', resources.fetch_resources, name = 'fetch-resources'),
    path('request/', request.request_resource, name='resource-request'),
    path('upload/', upload.upload_resource, name='resource-upload'),
    path('paths/', resources.fectch_file_paths, name='fetch-file-paths'),
]