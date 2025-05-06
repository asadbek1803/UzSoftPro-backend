from django.contrib.admin import AdminSite, ModelAdmin, register
from .models import Service

# Register your models here.

@register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('name', 'description', 'icon', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'icon')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'name': ('description',)}
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_unpublished']
    list_editable = ('description', 'icon')
    list_display_links = ('name',)