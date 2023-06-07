from django.shortcuts import render, redirect
from .models import Note, Tag, Course
from django.http import FileResponse, HttpResponse
from .forms import NoteForm
from django.forms import formset_factory
from .models import *
from .forms import *
from .filter import *
from django.shortcuts import get_object_or_404
import os
from docx2pdf import convert
# Create your views here.


def home(request):
    return render(request, 'base.html')


def noteSearch(request):
    tags = Tag.objects.all()  # Initialize tags variable with empty queryset
    courses = Course.objects.all()  # Fetch all courses
    notes = Note.objects.all()
    share_code = Note.share_code
    week = Note.week
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
            data = request.POST.get('data')
            tags = request.POST.getlist('tags')
            course = request.POST.get('course')
            share_code = request.POST.get('share_code')
            week = request.POST.get('week')
            notes = search_files(data, tags, course, share_code, week)

        # Filter notes based on selected tag and course
        
        context = {
            'tags': tags,
            'courses': courses,
            'notes': notes,
            'form': form,
            'share_code' : share_code
        }
        return render(request, 'noteSearch.html', context)
    else:

        return render(request, 'noteSearch.html', context)

def noteView(request, note_id):
        note = get_object_or_404(Note, id=note_id)
        tags = note.tags.all()
        form = NoteForm(instance=note)
        if request.method == 'POST':
            password_form = PasscodeForm(request.POST)
            if password_form.is_valid():
                passcode = password_form.cleaned_data['passcode']
            
                # Implement your passcode validation logic here
                passcode = int(passcode)
                if passcode == note.password: 
                    print() 
                    request.session['authenticated'] = True
                    return redirect('noteEdit', note_id=note_id)
                else:
                    password_form = PasscodeForm()
                    return render(request, 'noteView.html', {"note_id": note_id, "note": note, "tags": tags,"form": form, "password_form":password_form})

        else:
            password_form = PasscodeForm()
            return render(request, 'noteView.html', {"note_id": note_id, "note": note, "tags": tags,"form": form, "password_form":password_form})

def vote(request, note_id, vote_type):
    note = get_object_or_404(Note, id=note_id)
    if vote_type == "upvote":
        note.likes += 1
    if vote_type == "downvote":
        note.dislikes += 1
    note.save()
    return redirect('noteView', note_id=note_id)

def noteEdit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=note)
        tag_form = TagForm(request.POST)
        tag_delete = TagDelete(request.POST, note=note)
        print("form",tag_delete.is_valid())
        if form.is_valid() and tag_form.is_valid():
            tags = tag_form.cleaned_data['tags'] 
            tags_list = tags.split(',')
            print(tags_list)
            form.save()
            #selected_tags = tag_delete.cleaned_data['tags']
            for tag in tags_list:
                # Check if the tag already exists
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                note.tags.add(tag_obj)  
        return redirect('noteView', note_id=note_id)
    else:
        form = EditForm(instance=note)
        tag_form = TagForm()
        tag_delete = TagDelete(note=note)
        return render(request, 'noteEdit.html', {"form": form, "note_id": note_id, "tag_form":tag_form,"tag_delete": tag_delete })

def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('noteSearch')

def download_file(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    file = note.note_file  # Assuming 'file' is the FileField in your model
    if file:
        response = FileResponse(file)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
        return response
    else:
        return HttpResponse("File not found.")

def pdf_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.note_file.path.split(".")[-1] == "pdf":

        response = FileResponse(open(note.note_file.path, 'rb'),
                                content_type='application/pdf')
        return response
    elif note.note_file.path.split(".")[-1] == "docx":
        convert(note.note_file.path)
        
        response = FileResponse(open(note.note_file.path.split(".")[0] + ".pdf", 'rb'),
                        content_type='application/pdf')
        return response
        
    elif note.note_file.path.split(".")[-1] == "png":

        return FileResponse(open(note.note_file.path, 'rb'),
                                content_type='image/png')
    elif note.note_file.path.split(".")[-1] == "txt":

        return FileResponse(open(note.note_file.path, 'rb'),
                                content_type='text/plain')

def noteUpload(request):
    NoteFormSet = formset_factory(NoteForm, extra=1)
    tag_form = TagForm(request.POST or None)
    if request.method == 'POST':
        formset = NoteFormSet(request.POST, request.FILES, prefix='note')
        if formset.is_valid() and tag_form.is_valid():
            tags = tag_form.cleaned_data['tags']
            tags_list = tags.split(',')
            for form in formset:
                if form.has_changed():
                    note = form.save(commit=False)
                    note.save()
                    for tag in tags_list:
                        # Check if the tag already exists
                        tag_obj, created = Tag.objects.get_or_create(name=tag)
                        note.tags.add(tag_obj)
            return redirect('noteSearch')
    else:
        formset = NoteFormSet(prefix='note')
    return render(request, 'noteUpload.html', {'formset': formset, 'tag_form': tag_form})