from django.views.generic import DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from django.http import HttpResponseRedirect

# Create your views here.

def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        redirect_url = f'/games'
        return HttpResponseRedirect(redirect_to=redirect_url)

class UserProfile(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

