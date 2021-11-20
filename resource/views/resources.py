from django.contrib.auth import login
from django.db import reset_queries
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.models import course, subject, resource
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login/')
def resources_view(request):
    resources = resource.Resource.objects.all()
    courses = course.Course.objects.all()
    subjects = subject.Subject.objects.all()
    resource_type = {'B': 'Books', 'N':'Notes', 'Q': 'Question papers'}
    return render(request, "resource/show.html", {'resources': resources, 'courses': courses, 'subjects':subjects, 'resource_type': resource_type})

@login_required
@csrf_exempt
def fetch_resources(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    
    body = json.loads(request.body.decode("utf-8"))

    result = []
    queryset = resource.Resource.objects.all()

    if body['course'] != "all":
        queryset = queryset.filter(course__pk=body['course'])

    if body['subject'] != "all":
        queryset = queryset.filter(subject__pk=body['subject'])

    if body['resource'] != "all":
        queryset = queryset.filter(type=body['resource'])

    for row in queryset:
        res = {}
        res['course'] = row.course.name
        res['subject'] = {'code': row.subject.code, 'name': row.subject.name}
        res['type'] = get_resource_type_full_name(row.type)
        res['file'] = row.file.url
        res['timestamp'] = row.timestamp
        res['student'] = {'id': row.student.pk, 'name': row.student.name}
        result.append(res)

    resources = json.dumps(result, cls=DjangoJSONEncoder)
    return HttpResponse(resources, content_type="application/json")

def get_resource_type_full_name(type):
    if type == 'B':
        return 'Book'
    elif type == 'N':
        return 'Notes'
    elif type == 'Q':
        return 'Question Paper'
    else:
        return 'PPT'


