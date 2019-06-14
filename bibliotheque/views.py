from django.shortcuts import render
from . import models, forms
import os

last_five = models.Article.objects.all()[:5]

def bibliotheque (request):
    programs = models.Program.objects.all()
    stats = models.Stat.objects.all()
    return render (request, 'bibliotheque/bibliotheque.html', {'programs' : programs, 'stats' : stats, 'last_five' : last_five})

def notice (request, id):
    program = models.Program.objects.get(id = id)
    #path_to_remove = '/executables'
    #download_file = os.path.relpath(program.download_file, path_to_remove)
    form = forms.StatForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render (request, 'bibliotheque/notice.html', {'last_five' : last_five, 'program' : program})