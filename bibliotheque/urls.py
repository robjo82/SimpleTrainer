from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bibliotheque, name='bibliotheque'),
    path('notice/<slug:slug>', views.notice, name='notice'),
]    