#Coding: utf-8
from django import forms 
from .models import Stat

class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        exclude = ('program_ref', 'user_ref', 'download_number')
       
