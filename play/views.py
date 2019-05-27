from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from BooksAdmin.models import Book, Chapter
from .models import Save
from .forms import CreateSaveForm, AdminCreateSave
from BooksAdmin.forms import CreateBookForm, CreateChapterForm

# Create your views here.

class Games(ListView, FormView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books_list'
    form_class = CreateBookForm
    success_url = reverse_lazy('games_list')

    def get_queryset(self):
        return Book.objects.all()

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            self.object = None
            form = CreateBookForm(request.POST)
            if form.is_valid():
                form.save(commit=True)

class Saves(LoginRequiredMixin, ListView, FormView):
    model = Save
    template_name = 'saves.html'
    context_object_name = 'saves'
    form_class = CreateSaveForm
    success_url = reverse_lazy('games_list')


    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            saves = Save.objects.filter(book=self.kwargs['pk'])
        else:
            saves = Save.objects.filter(player = self.request.user.id).filter(book=self.kwargs['pk'])
        # import pdb
        # pdb.set_trace()S
        return saves

    def post(self, request, *args, **kwargs):
        self.object = None
        form = CreateSaveForm(request.POST)
        book = Book.objects.get(id = self.kwargs['pk'])
        if form.is_valid() and len(Save.objects.filter(book = book))<3:
            new_save = form.save(commit = False)
            new_save.player = request.user
            new_save.book = Book.objects.get(id = self.kwargs['pk'])
            new_save.current_chapter = Chapter.objects.get(book= new_save.book, ch_number=1)
            # import pdb
            # pdb.set_trace()
            new_save.save()
        return super() .post(request, *args, **kwargs)



class GamePlay(LoginRequiredMixin, DetailView):
    model = Save
    template_name = 'gameplay.html'
    context_object_name = 'save'


    def get_context_data(self, object_list = None, **kwargs):
        # import pdb; pdb.set_trace()
        context = super(GamePlay, self).get_context_data(**kwargs)
        context['next_chapters'] = Chapter.objects.all().filter(parent_chapter=self.get_object().current_chapter)
        return context

    def post(self, request, *args, **kwargs):
        form_value = (self.request.POST.get('new_chapter'))
        new_chapter = Chapter.objects.get(id = form_value)
        obj = Save.objects.get(id=kwargs['pk'])
        obj.current_chapter = new_chapter
        obj.save()
        redirect_url = f'/games/play/save/{obj.id}'
        print(redirect_url)
        return redirect(redirect_url)


class DeleteSave(LoginRequiredMixin, DeleteView):
    model = Save
    success_url = reverse_lazy('games_list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.request.user.is_superuser or self.request.user == self.object.players:
            return self.render_to_response(context)
        else:
            redirect_url = f'/games/'
            return redirect(redirect_url)


class UpdateSave (LoginRequiredMixin, UpdateView):
    model = Save
    fields = '__all__'
    template_name = 'save_update_form.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user == self.object.players:
            self.object = self.get_object()
            return super().get(request, *args, **kwargs)
        else:
            redirect_url = f'/games/'
            return redirect(redirect_url)