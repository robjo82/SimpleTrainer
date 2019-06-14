#Coding: utf-8
from django import forms 
from .models import Stat

class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = '__all__'
       
