from django.contrib import admin
from resource.models import course, subject, request

admin.site.register(course.Course)
admin.site.register(subject.Subject)
admin.site.register(request.Request)