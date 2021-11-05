from django import forms
from resource.models import request, course, subject

class Request(forms.ModelForm):

    RESOURCE_TYPE = (
        ('Q', 'Question paper'),
        ('N', 'Notes'),
        ('B', 'Book'),
    )

    course = forms.ModelChoiceField(queryset=course.Course.objects.all(),
            widget=forms.Select(
                attrs={
                    "placeholder":"Course",
                    "class":"form-control",
                }
        ),required=True)

    subject = forms.ModelChoiceField(queryset=subject.Subject.objects.all(),
            widget=forms.Select(
                attrs={
                    "placeholder":"Subject",
                    "class":"form-control",
                }
        ),required=True)

    type = forms.ChoiceField(choices=RESOURCE_TYPE,
            widget=forms.Select(
                attrs={
                    "placeholder":"Resource Type",
                    "class":"form-control",
                }
        ),required=True)

    class Meta:
        model = request.Request
        fields = ('course', 'subject', 'type')

