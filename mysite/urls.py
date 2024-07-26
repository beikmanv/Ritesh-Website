# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('gallery/', permanent=True)),
    path('', include('myapp.urls')),  # This includes the URLs from myapp
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
