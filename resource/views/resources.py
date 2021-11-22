from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.models.resource import Resource
from resource.models.course import Course
from resource.models.subject import Subject
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F


@login_required(login_url='/login/')
def resources_view(request):
    resources = Resource.objects.all()
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    resource_type = {'B': 'Books', 'N':'Notes', 'Q': 'Question papers'}

    return render(request, "resource/show.html", {'resources': resources, 'courses': courses, 'subjects':subjects, 'resource_type': resource_type})

@login_required
@csrf_exempt
def fectch_file_paths(request):

    if request.method != 'POST':
        return HttpResponse(status=400)   

    body = json.loads(request.body.decode("utf-8"))

    filePaths = []
    if body['popular'] == True:
        count = body['count'] if 'count' in body else 4
        resources = Resource.objects.all().order_by('-views')[:count]
    else:
        resources = Resource.objects.all()
    
    for resource in resources:
        res = {'path': resource.file.url, 'pk': resource.pk}
        filePaths.append(res)

    filePaths = json.dumps(filePaths, cls=DjangoJSONEncoder)
    return HttpResponse(filePaths, content_type="application/json")

@login_required
@csrf_exempt
def fetch_resources(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    
    body = json.loads(request.body.decode("utf-8"))

    result = []
    queryset = Resource.objects.all()

    if body['course'] != "all":
        queryset = queryset.filter(course__pk=body['course'])

    if body['subject'] != "all":
        queryset = queryset.filter(subject__pk=body['subject'])

    if body['resource'] != "all":
        queryset = queryset.filter(type=body['resource'])

    for row in queryset:
        res = {}
        res['title'] = row.title
        res['course'] = row.course.name
        res['subject'] = {'code': row.subject.code, 'name': row.subject.name}
        res['type'] = get_resource_type_full_name(row.type)
        res['file'] = row.file.url
        res['timestamp'] = row.timestamp
        res['student'] = {'id': row.student.pk, 'name': row.student.name}
        res['views'] = row.views
        res['pk'] = row.pk
        result.append(res)

    resources = json.dumps(result, cls=DjangoJSONEncoder)
    return HttpResponse(resources, content_type="application/json")

@login_required
@csrf_exempt
def resource_view_count(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    body = json.loads(request.body.decode("utf-8"))
    Resource.objects.filter(pk=body['pk']).update(views = F('views')+1)
    return HttpResponse(request)
    
def get_resource_type_full_name(type):
    if type == 'B':
        return 'Book'
    elif type == 'N':
        return 'Notes'
    elif type == 'Q':
        return 'Question Paper'
    else:
        return 'PPT'


