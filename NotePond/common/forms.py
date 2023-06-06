from django import forms

from .models import Note, Tag, Course
from django_select2.forms import Select2MultipleWidget


class NoteForm(forms.ModelForm):
    week = forms.ChoiceField(choices=[(i, i) for i in range(1, 12)], required=False)
    class Meta:
        model = Note
        fields = ['title', 'note_file', 'course', 'week', 'share_code', 'password']
    
    def clean_note_file(self):
        file = self.cleaned_data.get('note_file', False)
        if file:
            if file.content_type not in ['text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/png', 'application/pdf']:
                raise forms.ValidationError("Error. Supported file types: .txt/.docx/.pdf/.png")
            return file
        else:
            raise forms.ValidationError("Error. Could not read uploaded file")

class TagForm(forms.Form):
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'select2', 'data-tags': 'true'}),
        required=False,
        label="Tags: (seperate with commas)"
    )

    def clean_tags(self):
        # The value will be a comma separated string of tag names
        tag_names = self.cleaned_data.get('tags', '')
        tags = []
        for name in tag_names.split(','):
            # Get or create the tag by name
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        return tags

class search(forms.Form):
    share_code = forms.IntegerField(required=False)
    data = forms.CharField(max_length=20, required=False)
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), required=False)
    week = forms.IntegerField(required=False)
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(), required=False)
    
class EditForm(forms.ModelForm):
    week = forms.ChoiceField(choices=[(i, i) for i in range(1, 12)], required=False)
    class Meta:
        model = Note
        fields = ['title', 'note_file', 'course', 'week', 'share_code', 'password']
    

class PasscodeForm(forms.Form):
    passcode = forms.CharField(label='Passcode', widget=forms.PasswordInput)
    