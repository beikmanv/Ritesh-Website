# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('gallery/', views.gallery, name='gallery'),
]
