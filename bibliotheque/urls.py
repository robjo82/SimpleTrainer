from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bibliotheque, name='bibliotheque'),
    path(, views.notice, name='notice'),
]    

#(?P<slug>[-a-zA-Z0-9_]+)$