from django import forms
from .models import Note, Tag, Course

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note_file', 'course', 'week', 'tags']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }