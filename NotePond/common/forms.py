from django import forms
from .models import Note, Tag, Course
from django_select2.forms import Select2MultipleWidget


class NoteForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), required=False)
    week = forms.ChoiceField(choices=[(i, i)
                             for i in range(1, 12)], required=False)

    class Meta:
        model = Note
        fields = ['title', 'note_file', 'course', 'week', 'tags']
        widgets = {
            'tags': Select2MultipleWidget(),
        }

class search(forms.Form):
    data = forms.CharField(max_length=20)
