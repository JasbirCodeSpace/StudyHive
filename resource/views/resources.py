from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def show_resources(request):
    return HttpResponse(request, "Hello")