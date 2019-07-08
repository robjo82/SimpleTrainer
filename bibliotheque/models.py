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

    stat_ref = models.OneToOneField('Stat', on_delete = models.CASCADE, null=True)
    operating_system_ref = models.OneToOneField('OperatingSystem', on_delete = models.CASCADE, null=True) 

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
    
class OperatingSystem (models.Model):
    program_ref = models.ForeignKey (Program, on_delete = models.CASCADE, null=True)
    Windows10 = models.BooleanField (default=True)
    OldVersionsWindows = models.BooleanField (default=True)
    Linux = models.BooleanField (default=True)
    MacOS = models.BooleanField (default=True)
    Android = models.BooleanField (default=True)
    IOS = models.BooleanField (default=True)
    WindowsPhone = models.BooleanField (default=True)

    def __str__(self):
        return "Systèmes d'exploitations sur lesquels le programme {} fonctionne.".format(self.program_ref)

class Stat (models.Model):
    program_ref = models.ForeignKey(Program, on_delete = models.CASCADE, null=True)
    download_number = models.IntegerField(default = 0)

    def __str__(self):
        return "Stat du programme {}".format(self.program_ref)

class UserFeedback (models.Model):
    user_ref = models.ForeignKey(Profil, on_delete = models.CASCADE, null=True)
    program_ref = models.ForeignKey (Program, on_delete = models.CASCADE, null = True)
    overall_site_note = models.IntegerField (default = 5, verbose_name='note générale attibuée au site')
    site_accessibility = models.IntegerField (default = 5, verbose_name='accessibilité du site')
    site_usefulness = models.IntegerField (default = 5, verbose_name="facilité d'utilisation du site")
    what_functionality_would_you_like_on_the_site = models.TextField (null=True, verbose_name='quelle fonctionalité voudriez-vous ajouter au site ?')
    other_comment_on_the_site = models.TextField (null=True, verbose_name='autre commentaire sur le site')
    overall_app_note = models.IntegerField (default = 5, verbose_name= "note générale de l'application")
    ease_of_setting_up_the_app = models.IntegerField (default = 5, verbose_name="facilité de paramétrage de l'application")
    utility_of_record = models.IntegerField (default = 5, verbose_name="utilité de la notice")
    understand_of_record = models.IntegerField (default = 5, verbose_name="compréhension de la notice")
    app_functionnality = models.IntegerField (default = 5, verbose_name="fonctionalité de l'application")
    what_functionality_would_you_like_on_the_app = models.TextField (null=True, verbose_name="quelle fonctionalité voudriez-vous ajouter sur l'application  ?")
    other_comment_on_the_app = models.TextField (null=True, verbose_name="autre commentaire sur l'application")
    other_message = models.TextField (null=True, verbose_name='autre message')
