from django.urls import path
from resource.views import request, upload

urlpatterns = [
    path('request/', request.request_resource, name='resource-request'),
    path('upload/', upload.upload_resource, name='resource-upload'),
]