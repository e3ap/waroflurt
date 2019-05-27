from django.shortcuts import render
from .forms import CreateBookForm, CreateChapterForm
from django.views.generic import DetailView, CreateView, FormView, UpdateView, DeleteView
from .models import Book, Chapter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.



class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('games_list')


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_update_form.html'
