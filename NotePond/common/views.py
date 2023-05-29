from django.shortcuts import render, redirect

from .forms import NoteForm
from django.forms import formset_factory

# Create your views here.


def home(request):
    return render(request, 'base.html')


def noteSearch(request):
    if request.method == 'GET':
        # Get the selected tags from the request
        tags = request.GET.getlist('tag')

        # Query the notes based on the selected tags
        notes = Note.objects.filter(tags__name__in=tags).distinct()

        context = {
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
            for key, tag_name in request.POST.items():
                if key.startswith('tag-'):
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    note.tags.add(tag)
            for form in formset:
                # Weird saving becuase of many-to-many tag field. Must first create
                # unsaved note with ID to reference in many-to-many connection
                note = form.save(commit=False)
                note.save()
                form.save_m2m()

            return redirect('noteSearch.html')
    else:
        formset = NoteFormSet()

    return render(request, 'noteUpload.html', {'formset': formset})
