from django.contrib import admin
from .models import Profil


class ProfilAdmin (admin.ModelAdmin):
    list_display = ('user', 'avatar', 'country', 'postal_code', 'town', 'phone_number')
    list_filter = ('country', 'postal_code', 'town')
    search_fields = ('country', 'postal_code', 'town', 'phone_number')

admin.site.register(Profil, ProfilAdmin)
