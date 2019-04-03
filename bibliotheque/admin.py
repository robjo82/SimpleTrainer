from django.contrib import admin
from .models import Program, Article, Stat, Grade

class ProgramAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('created_at', 'updated_at',)
    search_fields = ('name', 'description', 'created_at', 'updated_at')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('program_ref', 'name', 'content')
    list_filter = ('program_ref', 'name', 'content')
    ordering = ('program_ref', )
    search_fields = ('program_ref', 'name', 'content')

class StatAdmin(admin.ModelAdmin):
    list_display = ('program_ref', 'download_number', 'favorite_number', 'avarage_rating')
    list_filter = ('program_ref', 'download_number', 'favorite_number', 'avarage_rating')
    ordering = ('program_ref', )
    search_fields = ('program_ref', 'download_number', 'favorite_number', 'avarage_rating')

class GradeAdmin (admin.ModelAdmin):
    list_display = ('program_ref', 'note')
    list_filter = ('program_ref', 'note')
    ordering = ('program_ref', )
    search_fields = ('program_ref', 'note')
          

admin.site.register (Program, ProgramAdmin)
admin.site.register (Article, ArticleAdmin)
admin.site.register (Stat, StatAdmin)
admin.site.register (Grade, GradeAdmin)
