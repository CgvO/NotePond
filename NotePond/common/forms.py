from django import forms
from .models import Note, Tag, Course


class NoteForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), required=False)
    week = forms.ChoiceField(choices=[(i, i)
                             for i in range(1, 12)], required=False)

    class Meta:
        model = Note
        fields = ['title', 'note_file', 'course', 'week', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
