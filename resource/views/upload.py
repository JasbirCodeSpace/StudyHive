from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def upload_resource(request):
    return render(request, 'resource/upload.html')