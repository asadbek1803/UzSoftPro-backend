from django.contrib.admin import AdminSite, ModelAdmin, register

# Register your models here.
from .models import Project, Category

@register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('name', 'description', 'category', 'image', 'github_link', 'live_link', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'image', 'github_link', 'live_link')
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
    list_editable = ('description', 'category', 'image')
    list_display_links = ('name',)

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'name': ('slug',)}
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_unpublished']
    list_editable = ('slug',)
    list_display_links = ('name',)
