# forms.py
from django import forms
from .models import ImageGallery

class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ['title', 'image', 'description']
