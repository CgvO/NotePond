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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from common import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="index"),
    path("upload/", views.noteUpload, name="noteUpload"),
    path('search/', views.noteSearch, name='noteSearch'),
    path("view/<int:note_id>/", views.noteView, name="noteView"),
    path('view_pdf/<int:note_id>', views.pdf_view, name='view_pdf'),
    path('download_file/<int:note_id>', views.download_file, name='download_file'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('noteEdit/<int:note_id>', views.noteEdit, name='noteEdit'),
    path('vote/<int:note_id>/<str:vote_type>/', views.vote, name='vote'),
    path('select2/', include("django_select2.urls")),
]
'''
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="index"),
    path("upload/", views.noteUpload, name="noteUpload"),
    path('search/', views.noteSearch, name='noteSearch'),
    path("view/<int:note_id>/", views.noteView, name="noteView"),
    path('view_pdf/<int:note_id>', views.pdf_view, name='view_pdf'),
    path('download_file/<int:note_id>', views.download_file, name='download_file'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('noteEdit/<int:note_id>', views.noteEdit, name='noteEdit'),
    path('vote/<int:note_id>/<str:vote_type>/', views.vote, name='vote'),
    path('select2/', include("django_select2.urls")),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
'''
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

