from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import ConnectForm
from .models import UsersOnline

# Create your views here.

def connect(request):
    users = User.objects.all()
    context = {}

    users = []
    #for user in users:
    #    if user.is_authenticated:
    #    users.append(tuple(user.id,user.username))

    #request.user.is_authenticated

    users = [(1, 'user1'),(2, 'user2'),(4, 'user4'),(10, 'user10'),]
    form = ConnectForm(users=users) 
    #form.new_choices(users=users)

    context['form'] = form

    return render(request, 'chat/set_user.html', context=context)

def talk(request):
    name = request.GET["name"]
    pair = request.GET["pair"]
    context = {}
    context['name'] = name

    user = UsersOnline(name=name)
    user.save()

    context['id'] = user.id

    return render(request, 'chat/talk.html', context=context)

def get_message(request):
    return HttpResponse("hello")

    # add the dictionary during initialization
#    form = BooksForm(request.POST or None)

#    if form.is_valid():
#        form.save()

#    context ={}
    #reset form fields
#    context['form'] = BooksForm()
#    #aditional context data, if needed
#    context['success'] = "True"
#
#    return render(request, "generic_views/create_book.html", context)

