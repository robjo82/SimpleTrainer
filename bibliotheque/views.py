from django.shortcuts import render
from . import models, forms
import os
from django.contrib.auth.decorators import login_required


last_five = models.Article.objects.all()[:5]

def bibliotheque (request):
    programs = models.Program.objects.all()
    stats = models.Stat.objects.all()
    return render (request, 'bibliotheque/bibliotheque.html', {'programs' : programs, 'stats' : stats, 'last_five' : last_five})

@login_required
def notice (request, id):
    id = id
    program = models.Program.objects.get(id = id)
    user = models.Profil.objects.get(id = request.user.id)

    form = forms.StatForm(request.POST or None)
    if form.is_valid():
        stat = form.save(commit = False)
        stat.program_ref = program
        stat.user_ref = user
        stat.save()
    
    return render (request, 'bibliotheque/notice.html', locals())