from django.db import models
from accounts.models.student import Student
from resource.models.course import Course
from resource.models.subject import Subject
from django.utils import timezone

def get_upload_path(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.course.name, instance.subject.code, instance.type, filename)


class Resource(models.Model):

    RESOURCE_TYPE = (
        ('Q', 'Question paper'),
        ('N', 'Notes'),
        ('B', 'Book'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(choices=RESOURCE_TYPE, max_length=1)
    file = models.FileField(upload_to=get_upload_path)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:

        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return f"Resource [{self.student.name}][{self.type}]"
