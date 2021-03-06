from django.shortcuts import render

# Create your views here.

#from generic_views import urls
#from django_tutorial import urls

def index(request):
    return render(request, 'home/index.html', context={})

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#for all generic class-based views the urls are not loaded when the file is imported, so we have to use the lazy form of reverse to load them later when they're available
