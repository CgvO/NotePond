from django.db import models

class Tag(models.Model):
    name = models.SlugField(max_length=200, unique=True, help_text="Enter a tag name")

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Enter a course name")

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    share_code = models.PositiveIntegerField(null=True, blank=True)
    private_code = models.PositiveIntegerField(null=True, blank=True)
    note_file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='notes')
    course = models.ForeignKey(
        Course, null=True, blank=True, on_delete=models.CASCADE, related_name='notes')
    week = models.PositiveIntegerField(null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title