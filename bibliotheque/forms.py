#Coding: utf-8
from django import forms 
from .models import UserFeedback

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        exclude = ('program_ref', 'user_ref')
       
