from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    note_file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    course = models.ForeignKey(
        Course, null=True, blank=True, on_delete=models.SET_NULL)
    week = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
