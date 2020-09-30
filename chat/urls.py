from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('connect/', views.connect, name="connect" ),
    path('talk/', views.talk, name="talk" ),
    path('get_message/', views.get_message, name="get_message" ),
]    

