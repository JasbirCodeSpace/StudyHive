from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Student(models.Model):
    """Student profile model"""

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('N', "Prefer not to say")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False, null = True)
    gender = models.CharField(choices= GENDER_CHOICES, max_length=50, null = True)
    batch = models.IntegerField(null = True)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return f"Student [{self.user.username}]"

    
    @receiver(post_save, sender=User)
    def create_user_student(sender, instance, created, **kwargs):
	    if created:
		    Student.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_student(sender, instance, **kwargs):
	    instance.student.save()
    
    def get_absolute_url(self):
        return reverse("student-view", kwargs={"user": self.user.username})
    
