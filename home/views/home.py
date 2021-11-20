from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.models.resource import Resource

@login_required(login_url='/login/')
def index(request):
    popular_resources = get_popular_resources()
    return render(request, 'home/index.html', {'popular_resources': popular_resources})

def get_popular_resources(count=4):
    resources = Resource.objects.all().order_by('-views')[:count]
    return resources



