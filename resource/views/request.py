from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.forms.resource import RequestForm

@login_required(login_url='/login/')
def request_resource(request):
    
    msg = {}
    success = False

    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.student = request.user.student
            form_data.save()
            success = True
            return redirect('home')

        else:
            msg = "Invalid form data"
    else:
        form = RequestForm()

    return render(request, 'resource/request.html', {'form': form, 'msg': msg, 'success': success})
