from django.shortcuts import render
from . import models, forms
import os
from django.contrib.auth.decorators import login_required
import statistics


last_five = models.Article.objects.all()[:5]

def bibliotheque (request):
    programs = models.Program.objects.all()
    return render (request, 'bibliotheque/bibliotheque.html', locals())

@login_required
def notice (request, id):
    id = id
    program = models.Program.objects.get(id = id)
    user = models.Profil.objects.get(id = request.user.id)

    form = forms.UserFeedbackForm(request.POST or None)
    if form.is_valid():
        user_feedback = form.save(commit = False)
        user_feedback.program_ref = program
        user_feedback.user_ref = user
        user_feedback.save()
    
    return render (request, 'bibliotheque/notice.html', locals())