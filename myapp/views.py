# views.py
from django.shortcuts import render, redirect
from .forms import ImageGalleryForm
from .models import ImageGallery

def upload_image(request):
    if request.method == 'POST':
        form = ImageGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageGalleryForm()
    return render(request, 'upload_image.html', {'form': form})

def gallery(request):
    images = ImageGallery.objects.all()
    return render(request, 'gallery.html', {'images': images})
