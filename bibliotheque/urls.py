from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.bibliotheque, name='bibliotheque'),
    re_path('notice/(?P<id>[0-9]+)$', views.notice, name='notice'),
]    

#(?P<slug>[-a-zA-Z0-9_]+)$