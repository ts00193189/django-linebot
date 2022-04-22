from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.callback),
    path('hello_world', views.hello),

]