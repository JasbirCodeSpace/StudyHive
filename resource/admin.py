from django.contrib import admin
from resource.models import course, subject

admin.site.register(course.Course)
admin.site.register(subject.Subject)