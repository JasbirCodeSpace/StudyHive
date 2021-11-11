from django.db import models
from accounts.models.student import Student
from resource.models.course import Course
from resource.models.subject import Subject
from django.utils import timezone

class Request(models.Model):

    RESOURCE_TYPE = (
        ('Q', 'Question paper'),
        ('N', 'Notes'),
        ('B', 'Book'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(choices=RESOURCE_TYPE, max_length=1)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for Request."""

        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        """Unicode representation of Request."""
        return f"Request [{self.student.name}][{self.type}]"
