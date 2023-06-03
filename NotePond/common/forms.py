from django import forms
from .models import Note, Tag, Course
from django_select2.forms import Select2MultipleWidget


class NoteForm(forms.ModelForm):
    week = forms.ChoiceField(choices=[(i, i) for i in range(1, 12)], required=False)
    class Meta:
        model = Note
        fields = ['title', 'note_file', 'course', 'week', 'share_code', 'private_code']

    def clean_note_file(self):
        file = self.cleaned_data.get('note_file', False)
        if file:
            if file.content_type not in ['text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/png', 'application/pdf']:
                raise forms.ValidationError("Error. Supported file types: .txt/.docx/.pdf/.png")
            return file
        else:
            raise forms.ValidationError("Error. Could not read uploaded file")

class TagForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False
    )

class search(forms.Form):
    data = forms.CharField(max_length=20)
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(), required=False)
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), required=False)
