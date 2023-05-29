from django.db.models import Q
from .models import Note

def search_files(data, selected_tags, selected_course):
    notes = Note.objects.all()

    if selected_tags and selected_tags != ['']:
        notes = notes.filter(tags__name__in=selected_tags)

    if selected_course:
        notes = notes.filter(course__id=selected_course)

    if data:
        notes = notes.filter(title__icontains=data)

    return notes
