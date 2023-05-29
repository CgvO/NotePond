from django.shortcuts import render, redirect
from .forms import NoteForm
from django.forms import formset_factory
from .filter import search_files
from .forms import search
from .models import *
from django.http import FileResponse
# Create your views here.
def home(request):
    return render(request, 'base.html')

def noteSearch(request):
    if request.method == "POST":
        form = search(request.POST)
        if form.is_valid():
            #get the data from the from
            data = form.cleaned_data.get('data')

            notes = search_files(data)
        
        return render(request, 'noteSearch.html', {"data": data, "notes": notes})
    else:
        form = search()
        return render(request, 'noteSearch.html', {"form": form})

def noteView(request, note_id):
    if request.method == "POST":
        return redirect("noteSearch.html")
    else:

        return render(request, 'noteView.html', {"note_id":note_id,})
    
def pdf_view(request, note_id):
    note = Note.objects.all()[note_id-1]
    return FileResponse(open(note.note_file.path, 'rb'), content_type='application/pdf')

def noteUpload(request):
    NoteFormSet = formset_factory(NoteForm, extra=1) # Starts with 1 by default
    if request.method == 'POST':
        formset = NoteFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                # Weird saving becuase of many-to-many tag field. Must first create 
                # unsaved note with ID to reference in many-to-many connection
                note = form.save(commit=False)
                note.save() 
                form.save_m2m()
            return redirect('noteSearch.html')
    else:
        formset = NoteFormSet()
    
    return render(request, 'noteUpload.html', {'formset' : formset})
