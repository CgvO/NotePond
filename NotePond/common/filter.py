from django.db.models import Q
from .models import Note

def search_files(search_results):
    """
    files = Note.objects.filter(
        Q(title__icontains=search_results) | Q(tags__name__icontains=search_results)
    )
    return files
    """
    return Note.objects.all()


