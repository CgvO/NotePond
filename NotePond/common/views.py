from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Note, Tag, Course
from django.http import FileResponse
from .forms import NoteForm
from django.forms import formset_factory
from .models import *
from .forms import *
from .filter import *
from django.shortcuts import get_object_or_404
import os
# Create your views here.


def home(request):
    return render(request, 'base.html')


def noteSearch(request):
    tags = Tag.objects.all()  # Initialize tags variable with empty queryset
    courses = Course.objects.all()  # Fetch all courses
    notes = Note.objects.all()
    form = search()
    context = {
        'tags': tags,
        'courses': courses,
        'notes': notes,
        'form': form,
    }

    if request.method == 'POST':

        form = search(request.POST)

        if form.is_valid():
            # get the data from the from
            data = form.cleaned_data.get('data')
            tags = request.POST.getlist('tags')
            course = request.POST.get('course')

        # Filter notes based on selected tag and course
        notes = search_files(data, tags, course)
        context = {
            'tags': tags,
            'courses': courses,
            'notes': notes,
            'form': form,
        }
        return render(request, 'noteSearch.html', context)
    else:

        return render(request, 'noteSearch.html', context)


def noteView(request, note_id):
    if request.method == "POST":
        return redirect("noteSearch.html")
    else:
        note = Note.objects.all()[note_id-1]
        return render(request, 'noteView.html', {"note_id": note_id, "note": note})


def download_file(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    file_content = note.file_content
    file_name = f"note_{note_id}.txt"

    response = FileResponse(
        file_content, as_attachment=True, filename=file_name)
    return response


def pdf_view(request, note_id):
    note = Note.objects.all()[note_id-1]
    response = FileResponse(open(note.note_file.path, 'rb'),
                            content_type='application/pdf')
    return response


def noteUpload(request):
    NoteFormSet = formset_factory(
        NoteForm, extra=1)  # Starts with 1 by default
    if request.method == 'POST':
        formset = NoteFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                # Weird saving becuase of many-to-many tag field. Must first create
                # unsaved note with ID to reference in many-to-many connection
                note = form.save(commit=False)
                note.save()

                for tag_name in form.cleaned_data['tags']:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    note.tags.add(tag)

            return redirect('noteSearch')
    else:
        formset = NoteFormSet()

    return render(request, 'noteUpload.html', {'formset': formset})
