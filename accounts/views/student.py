from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms.student import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = "Invalid credentials"
        
        else:
            msg = "Error validating the form"
    
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm(request.POST or None)
    msg = None
    success = False

    if request.method == 'POST':

        if form.is_valid():
            user = form.save()
            user.student.name = form.cleaned_data.get('name')
            user.student.dob = form.cleaned_data.get('dob')
            user.student.gender = form.cleaned_data.get('gender')
            user.student.batch = form.cleaned_data.get('batch')
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            msg = "User created successfully"
            success = True
        else:
            msg = "Error validating the form"

    return render(request, "accounts/register.html", {'form': form, 'msg': msg, 'success': success})

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('login')