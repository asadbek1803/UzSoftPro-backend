from django.contrib.admin import AdminSite, ModelAdmin, register
from .models import Team
# Register your models here.

@register(Team)
class TeamAdmin(ModelAdmin):
    list_display = ('full_name', 'github_link', 'linkedin_link', 'email', 'image', 'created_at', 'updated_at')
    search_fields = ('full_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('full_name', 'github_link', 'linkedin_link', 'email', 'image')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'full_name': ('github_link', 'linkedin_link')}
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_unpublished']
    list_editable = ('github_link', 'linkedin_link', 'email', 'image')
    list_display_links = ('full_name',)