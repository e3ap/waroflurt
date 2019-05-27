from django import forms
from .models import Book, Chapter


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

class CreateChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = '__all__'
