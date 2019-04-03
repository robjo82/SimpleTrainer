#Coding:utf-8
from django import forms
from django.contrib.auth.models import User

class RegisterForm (forms.Form):
    pseudo = forms.CharField(label="Votre pseudo  *", widget=forms.TextInput, required=True)
    email = forms.EmailField(label="Votre adresse mail  *", help_text = "exemple : marie.durant@gmail.com", widget= forms.EmailInput, required=True)
    password = forms.CharField(label="Votre mot de passe  *", widget= forms.PasswordInput, required=True)
    last_name = forms.CharField(label="Votre Nom  *", widget = forms.TextInput, required=True)
    first_name = forms.CharField(label="Votre Prénom  *", widget = forms.TextInput, required=True)
    avatar = forms.ImageField(label="Votre photo de profil", required=False)
    country = forms.CharField(label="Pays", required=False)
    postal_code = forms.IntegerField(label = "Votre Code Postal", required=False)
    town = forms.CharField(label="Ville", required=False)
    phone_number = forms.IntegerField (label = "Votre numéro de téléphone", required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label= "Votre pseudo", widget=forms.TextInput, required=True)
    password = forms.CharField(label="Votre mot de passe", widget=forms.PasswordInput, required=False)