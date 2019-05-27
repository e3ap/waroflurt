from django.db import models
from BooksAdmin.models import Book, Chapter
from django.contrib.auth.models import User

# Create your models here.


class Save(models.Model):
    name = models.CharField(blank = False, max_length=20)
    book = models.ForeignKey(Book, blank = False, on_delete=models.CASCADE)
    player = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    current_chapter = models.ForeignKey(Chapter, blank=False, on_delete=models.CASCADE)