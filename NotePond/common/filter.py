from django.db.models import F, Q
from .models import Note

def search_files(data, tags, selected_course, share_code, week):
    notes = Note.objects.all()

    if share_code and share_code != '':
        notes = notes.filter(Q(share_code=share_code))
    else:
        notes = notes.filter(share_code__isnull=True)
    
    if selected_course:
        notes = notes.filter(course__id=selected_course)

    if data:
        notes = notes.filter(title__icontains=data)

    if week:
        notes = notes.filter(week__icontains=week)

    if tags:
        notes = notes.filter(tags__id__in=tags)

    notes = notes.annotate(difference=F('likes') - F('dislikes')).order_by('-difference')

    return notes
