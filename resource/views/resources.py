from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.models import course, subject, resource

@login_required(login_url='/login/')
def show_resources(request):
    resources = resource.Resource.objects.all()
    print(resources)
    return render(request, "resource/show.html", {'resources': resources})