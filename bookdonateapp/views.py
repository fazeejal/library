from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadFile
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')  # Redirect back to the upload page after successful upload
    else:
        form = UploadFileForm()
    files = UploadFile.objects.all()
    return render(request, 'upload.html', {'form': form, 'files': files})

def download_file(request, file_id):
    uploaded_file = UploadFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response
