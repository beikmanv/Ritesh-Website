# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('gallery/', permanent=True)),
    path('upload/', include('myapp.urls')),
    path('gallery/', include('myapp.urls')),
]



