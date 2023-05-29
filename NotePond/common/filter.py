from django.db.models import Q
from .models import Note

def search_files(data, selected_tags, selected_course):
    """
    files = Note.objects.filter(
        Q(title__icontains=search_results) | Q(tags__name__icontains=search_results)
    )
    return files
    """
    """
    notes = Note.objects.filter(
            Q(tags__id__in=selected_tags) & Q(course__id=selected_course)
        ).distinct()
    """
    return Note.objects.all()


