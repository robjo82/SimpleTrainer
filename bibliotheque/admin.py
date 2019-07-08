from django.contrib import admin
from .models import Program, Article, Stat, Grade, OperatingSystem, UserFeedback

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
    list_display = ('program_ref', 'download_number')
    list_filter = ('program_ref', 'download_number')
    ordering = ('program_ref', )
    search_fields = ('program_ref', 'download_number')

class GradeAdmin (admin.ModelAdmin):
    list_display = ('program_ref', 'note')
    list_filter = ('program_ref', 'note')
    ordering = ('program_ref', )
    search_fields = ('program_ref', 'note')

class OperatingSystemAdmin (admin.ModelAdmin):
    list_display = ('program_ref','Windows10', 'OldVersionsWindows', 'Linux', 'MacOS', 'IOS', 'WindowsPhone', 'Android')
    list_filter = ('program_ref','Windows10', 'OldVersionsWindows', 'Linux', 'MacOS', 'IOS', 'WindowsPhone', 'Android')
    ordering = ('program_ref', )
    search_fields = ('program_ref', )

class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('program_ref', 'user_ref') 
    list_filter = ('program_ref', 'user_ref') 
    ordering = ('program_ref', )
    search_fields = ('program_ref', )          

admin.site.register (Program, ProgramAdmin)
admin.site.register (Article, ArticleAdmin)
admin.site.register (Stat, StatAdmin)
admin.site.register (Grade, GradeAdmin)
admin.site.register (OperatingSystem, OperatingSystemAdmin)
admin.site.register (UserFeedback, UserFeedbackAdmin)
