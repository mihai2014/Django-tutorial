from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Books
from .forms import BooksForm

def index(request):
    return render(request, 'generic_views/index.html', context={})

class IndexGeneric(TemplateView):
   template_name = "generic_views/index.html"

def my_view(request):
    if request.method == 'GET':
        # <view logic> 
        return HttpResponse('result')

class MyView(View):
    def get(self, request):
        # <view logic> 
        return HttpResponse('result')

#see !! /home/mihai/all/data/work2020/django/dj_test/product for slug field
def create_book(request):

    # add the dictionary during initialization
    form = BooksForm(request.POST or None)

    if form.is_valid():
        form.save()

    context ={}
    #reset form fields
    context['form'] = BooksForm()
    #aditional context data, if needed
    context['success'] = "True"

    return render(request, "generic_views/create_book.html", context)

#default template: geeks/templates/geeks/books_form.html
class CreateBook(CreateView):

    # specify the model for create view
    model = Books

    # specify the fields to be displayed
    fields = ['title', 'description']

    success_url="/generic-views/create-book-generic/"

    #aditional context data, if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "True"
        return context

def list_book(request):

    context ={}

    # add the dictionary during initialization 
    context["dataset"] = Books.objects.all()

    return render(request, "generic_views/list_book.html", context)

#default template : geeks/templates/geeks/book_list.html
class BookList(ListView):

    #modify default context_object_name
    #context_object_name = 'all_books_list'

    # specify the model for list view 
    model = Books

#custom querys

#class BooksList2(ListView):
#
#    context_object_name = 'selected_geeks_list'
#    queryset = GeeksModel.objects.filter(title__startswith='book')
#    template_name = 'generic-views/books_by_title.html'

#class BooksList3(ListView):
#
#    template_name = 'generic-views/books_by_description.html'
#
#    def get_queryset(self):
#        return Book.objects.filter(description__contains="motorcycle")


# pass id attribute from urls
def detail_book(request, id):
    context ={}

    # add the dictionary during initialization
    context["data"] = Books.objects.get(id = id)

    return render(request, "generic_views/detail_view.html", context)

#default template: geeks/templates/geeks/books_detail.html
class BooksDetail(DetailView):
    # specify the model to use
    model = Books


def update_book(request, id):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Books, id = id)

    # pass the object as instance in form
    form = BooksForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/generic-views/detail-book/"+str(id))

    # add form dictionary to context
    context["form"] = form

    return render(request, "generic_views/update_book.html", context)

#default template_name : geeks/templates/geeks/books_form.html
class BookUpdate(UpdateView):
    # specify the model you want to use
    model = Books

    # specify the fields
    fields = [
        "title",
        "description"
    ]

    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    # success_url ="/geeks/detail/1"

    def get_success_url(self):
        #title = self.request.POST['title']
        #return reverse_lazy()
        #return reverse('geeks:detail', kwargs={
        #'pk': self.object.pk,})
        return f"/generic-views/detail-book-generic/{self.object.pk}"

def delete_book(request, id):
    context ={}

    # fetch the object related to passed id 
    obj = get_object_or_404(Books, id = id)


    if request.method =="POST":
        # delete object 
        obj.delete()
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/generic-views/list-book/")

    return render(request, "generic_views/delete_book.html", context)


#default template_name : geeks/templates/geeks/book_confirm_delete.html
class BookDelete(DeleteView):
    # specify the model you want to use
    model = Books

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/generic-views/list-book-generic/"


