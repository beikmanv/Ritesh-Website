from django.shortcuts import render, redirect, get_object_or_404
from .models import Image  # Make sure the model name is Image
from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('gallery')
