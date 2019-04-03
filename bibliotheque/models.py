#Coding:utf-8
from django.db import models
from django.utils import timezone
 
class Program (models.Model):
    name = models.CharField(max_length = 100, default = "Nom du Programme")
    description = models.TextField(default = "Ceci est la description d'un programme")
    created_at = models.DateTimeField (auto_now = False, auto_now_add=True)
    updated_at = models.DateTimeField (auto_now = True, auto_now_add=False)
    image = models.ImageField (upload_to = 'images', null=True)
    download_file = models.FileField (upload_to = 'executables', null=True)
     
    def __str__(self):
        return self.name
 
 
class Article (models.Model):
    program_ref = models.OneToOneField (Program, on_delete = models.CASCADE)
    name = models.CharField (max_length = 100, default = program_ref.name)
    content = models.TextField (default = "Ceci est le contenu de l'article")
    
    def __str__(self):
        return "Article du programe {}".format (self.program_ref)
    
class Grade (models.Model):
    program_ref = models.ForeignKey (Program, on_delete = models.CASCADE)
    note = models.DecimalField (max_digits = 3, decimal_places = 1, default = 5)
    
class Stat (models.Model):
    program_ref = models.OneToOneField(Program, on_delete = models.CASCADE)
    download_number = models.IntegerField(default = 0)
    favorite_number = models.IntegerField(default = 0)
    avarage_rating = models.IntegerField (default = 5) 
    