from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "auth1"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='auth1'),
]
  
