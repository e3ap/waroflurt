from django.db import models
# from ..Accounts import models
# Create your models here.

class Book(models.Model):
    name = models.CharField(blank= False,max_length=50)
    author = models.CharField(blank= False,max_length=50)
    description = models.TextField(blank= False)
    genre = models.CharField(max_length=50, blank= False)
    # save_1 = models.ForeignKey(Save, on_delete=models.CASCADE)
    # save_2 = models.ForeignKey(Save, on_delete=models.CASCADE)
    # save_3 = models.ForeignKey(Save, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.name}"

class Chapter(models.Model):
    ch_title = models.CharField(blank= False, max_length=20)
    body = models.TextField(blank= False)
    book = models.ForeignKey(Book, blank=False, on_delete=models.CASCADE)
    parent_chapter = models.ForeignKey('self', on_delete=models.CASCADE,blank= True, null=True)
    animation = models.URLField(blank=True)
    sfx = models.URLField(blank=True)
    ch_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Chapter {self.ch_number}: {self.ch_title}"

