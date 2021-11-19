from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.models import course, subject, resource
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login/')
def resources_view(request):
    resources = resource.Resource.objects.all()
    return render(request, "resource/show.html", {'resources': resources})

@login_required
@csrf_exempt
def fetch_resources(request):
    resources = list(resource.Resource.objects.all().values())
    resources = json.dumps(resources, cls=DjangoJSONEncoder)
    return HttpResponse(resources, content_type="application/json")




