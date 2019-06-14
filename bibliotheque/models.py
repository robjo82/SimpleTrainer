#Coding:utf-8
from django.db import models
from django.utils import timezone
from EspacePerso.models import Profil
 
class Program (models.Model):
    name = models.CharField(max_length = 100, default = "Nom du Programme")
    description = models.TextField(default = "Ceci est la description d'un programme")
    created_at = models.DateTimeField (auto_now = False, auto_now_add=True)
    updated_at = models.DateTimeField (auto_now = True, auto_now_add=False)
    image = models.ImageField (upload_to = 'images', null=True)
    download_file = models.FileField (upload_to = 'executables', null=True)
    slug = models.SlugField (default="programme_{}".format(id))
    youtube_code = models.TextField(null=True)
     
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
    program_ref = models.ForeignKey(Program, on_delete = models.CASCADE)
    user_ref = models.ForeignKey(Profil, on_delete = models.CASCADE)
    download_number = models.IntegerField(default = 0)
    overall_site_note = models.IntegerField (default = 5)
    site_accessibility = models.IntegerField (default = 5)
    site_usefulness = models.IntegerField (default = 5)
    what_functionality_would_you_like_on_the_site = models.TextField (null=True)
    other_comment_on_the_site = models.TextField (null=True)
    overall_app_note = models.IntegerField (default = 5)
    ease_of_setting_up_the_app = models.IntegerField (default = 5)
    utility_of_record = models.IntegerField (default = 5)
    understand_of_record = models.IntegerField (default = 5)
    app_functionnality = models.IntegerField (default = 5)
    what_functionality_would_you_like_on_the_app = models.TextField (null=True)
    other_comment_on_the_app = models.TextField (null=True)
    other_message = models.TextField (null=True)
