from django.shortcuts import render

# Create your views here.

#from generic_views import urls
#from django_tutorial import urls

def index(request):
    return render(request, 'home/index.html', context={})



