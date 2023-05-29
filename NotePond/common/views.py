from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Note, Tag, Course

from .forms import NoteForm
from django.forms import formset_factory
from .models import *

# Create your views here.


def home(request):
    return render(request, 'base.html')


def noteSearch(request):
    tags = Tag.objects.all()  # Initialize tags variable with empty queryset
    courses = Course.objects.all()  # Fetch all courses
    
    if request.method == 'POST':
        selected_tags = request.POST.getlist('tags')
        selected_course = request.POST.get('course')
        
        # Filter notes based on selected tag and course
        notes = Note.objects.filter(
            Q(tags__id__in=selected_tags) & Q(course__id=selected_course)
        ).distinct()
    else:
        notes = []

    context = {
        'tags': tags,
        'courses': courses,
        'notes': notes,
    }
    return render(request, 'noteSearch.html', context)





def noteView(request):
    return render(request, 'noteView.html')


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

                for key, tag_name in request.POST.items():
                    if key.startswith('tag-'):
                        print(f"key: {key}, name: {tag_name}")
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        note.tags.add(tag)

            return redirect('noteSearch')
    else:
        formset = NoteFormSet()

    return render(request, 'noteUpload.html', {'formset': formset})
