from django.db import models
from django.contrib.auth.models import User


class Profil (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    avatar = models.ImageField(null = True, blank = True, upload_to = "avatars")
    country = models.CharField(max_length = 50, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    town = models.CharField(max_length = 50, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return "Profil de {}".format(self.user.username)
