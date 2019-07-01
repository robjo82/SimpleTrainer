from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.bibliotheque, name='bibliotheque'),
    path('notice/<int:id>', views.notice, name='notice'),
]    