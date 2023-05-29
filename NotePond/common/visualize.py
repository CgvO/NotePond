from .models import Note, Tag, Course


def show_document_contents(note):
    note = Note.objects.filter(title=note)
    return note

