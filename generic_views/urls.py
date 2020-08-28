from django.urls import path

from . import views

app_name = 'generic-views'

urlpatterns = [
    path('', views.index, name="index" ),
    #here template_name overwriting the template already defined in views, just example
    path('index-generic/', views.IndexGeneric.as_view(template_name = "generic_views/index.html"), name="index-generic"),

    path('my-view/', views.my_view, name='my-view'),
    path('my-view-generic/', views.MyView.as_view(), name='my-view-generic'),

    path('create-book/',views.create_book, name="create-book"),
    path('create-book-generic/', views.CreateBook.as_view(), name="create-book-generic" ),

    path('list-book/',views.list_book, name="list-book"),
    path('list-book-generic/', views.BookList.as_view(), name="list-book-generic"),    

    path('detail-book-id/<int:id>/', views.detail_book_id, name="detail-book-id" ),
    path('detail-book-slug/<slug:slug>/', views.detail_book_slug, name="detail-book-slug" ),
    path('detail-book-generic/<int:pk>/', views.BooksDetail.as_view(), name="detail-book-generic"),

    path('update/<int:id>/', views.update_book, name="update"),
    path('update-generic/<int:pk>/', views.BookUpdate.as_view(), name="update-generic"),

    path('delete/<int:id>/', views.delete_book, name="delete" ),
    path('delete-generic/<int:pk>/', views.BookDelete.as_view(), name="delete-generic"),    

]    
