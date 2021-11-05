from django.db import models

class Course(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of Course."""
        return f"Course [{self.name}]"
