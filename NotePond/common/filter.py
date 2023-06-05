from django.db.models import F
from .models import Note

def search_files(data, selected_tags, selected_course,share_code, week):
    notes = Note.objects.all()

    if selected_tags and selected_tags != ['']:
        notes = notes.filter(tags__name__in=selected_tags)

    if selected_course:
        notes = notes.filter(course__id=selected_course)

    if data:
        notes = notes.filter(title__icontains=data)

    if share_code:
        notes = notes.filter(share_code__icontains=share_code)

    if week:
        notes = notes.filter(week__icontains=week)

    notes = notes.annotate(difference=F('likes') - F('dislikes')).order_by('-difference')

    return notes
