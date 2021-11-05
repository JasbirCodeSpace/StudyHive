from django.db import models
from resource.models.course import Course

class Subject(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Subject."""

        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        """Unicode representation of Subject."""
        pass
