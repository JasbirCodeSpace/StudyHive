from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resource.forms.resource import UploadForm

@login_required(login_url='/login/')
def upload_resource(request):
    
    msg = {}
    success = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.student = request.user.student
            form_data.save()
            success = True
            return redirect('home')

        else:
            msg = "Invalid form data"
    else:
        form = UploadForm()

    return render(request, 'resource/upload.html', {'form': form, 'msg': msg, 'success': success})
