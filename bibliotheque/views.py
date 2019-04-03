from django.shortcuts import render
from . import models

last_five = models.Article.objects.all()[:5]

def bibliotheque (request):
    programs = models.Program.objects.all()
    stats = models.Stat.objects.all()
    return render (request, 'bibliotheque/pages/bibliotheque.html', {'programs' : programs, 'stats' : stats, 'last_five' : last_five})