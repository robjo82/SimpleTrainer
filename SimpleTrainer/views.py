#Coding:utf-8
from django.shortcuts import render
from bibliotheque import models
from django.contrib.auth.models import User
from EspacePerso.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


last_five = models.Article.objects.all()[:5]

def index (request):
    article = models.Article.objects.all()    
    return render (request, 'pages/index.html', {'article' : article, 'last_five' : last_five})

def contact (request):
    return render (request, 'pages/contact.html', {'last_five' : last_five})

def a_propos (request):
    return render (request, 'pages/a_propos.html', {'last_five' : last_five})

def handler404 (request, exeception):
    return render (request, 'erreurs/404.html', {'last_five' : last_five}, status=404)

def handler500 (request):
    return render (request, 'erreurs/500.html', {'last_five' : last_five}, status=500)

def handler403 (request, exeception):
    return render (request, 'erreurs/403.html', {'last_five':last_five}, status=403)

def handler400 (request, exeception):
    return render (request, 'erreurs/400.html', {'last_five':last_five}, status=400)

def menu (request):
    return render (request, 'layouts/_nav.html', {'last_five' : last_five})

'''def test(request, id):
	return render(request, 'pages/test.html', {'id': id})'''