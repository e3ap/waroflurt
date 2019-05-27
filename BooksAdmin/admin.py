from django.contrib import admin
from .models import Book, Chapter
from play import models

# Register your models here.

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(models.Save)