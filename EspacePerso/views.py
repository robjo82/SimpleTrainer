from django.shortcuts import render
from bibliotheque.models import Article
from . import models
from .models import Profil
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

last_five = Article.objects.all()[:5]


def register (request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        pseudo = form.cleaned_data['pseudo']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        avatar = form.cleaned_data['avatar']
        country = form.cleaned_data['country']
        postal_code = form.cleaned_data['postal_code']
        town = form.cleaned_data['town']
        phone_number = form.cleaned_data['phone_number']
        
        envoi = True
        user = User.objects.create_user(pseudo, email, password)
        user.first_name = first_name
        user.last_name = last_name
        profil = Profil(user = user, avatar = avatar, country = country, postal_code = postal_code, town = town, phone_number = phone_number)
        user.save()
        profil.save()
        
    return render (request, 'EspacePerso/inscription.html', locals(), {'last_five' : last_five})


def connect (request) :
    return render (request, 'EspacePerso/connect.html', {'last_five' : last_five})


@login_required
def personal_space (request):
    profil = Profil.objects.get(user_id = request.user.id)
    return render (request, 'EspacePerso/personal_space.html', {'last_five' : last_five, "profil" : profil})
