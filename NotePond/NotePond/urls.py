"""
URL configuration for NotePond project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from common import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'common'
urlpatterns = [
    path("admin/", admin.site.urls),
    path("upload/", views.noteUpload, name="upload"),
    path("", views.home, name="index"),
    path("search/", views.noteSearch, name="search"),
    path("view/<int:note_id>/", views.noteView, name="view"),
    path("pdf/", views.pdf_view, name="pdf"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
