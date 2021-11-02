from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class RegisterForm(UserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('N', 'Prefer not to say'),
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ), required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ), required=True
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full name",
                "class": "form-control"
            }
        ), required=True
    )

    dob = forms.DateField(
        widget=forms.DateTimeInput(
            attrs={
                "placeholder":"DOB",
                "class":"form-control",
                'type': 'date'
            }
        ), required=True
    )

    gender = forms.CharField(
        widget=forms.Select(
            choices=GENDER_CHOICES,
            attrs={
                "placeholder": "Gender",
                "class": "form-control"
            }
        ), required=True
    )

    batch = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Batch",
                "class": "form-control"   
            }
        ), required=True
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ), required=True
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ), required=True
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'gender', 'dob', 'batch', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Account with this email already exist.")
        return email
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        return cleaned_data

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder":"Username",
                "class":"form-control"
            }
        ), required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "placeholder":"Password",
                "class":"form-control"
            }
        ), required = True
    )

    class Meta:
        model = User
        fields = ("username", "password")