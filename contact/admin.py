from django.contrib.admin import AdminSite, ModelAdmin, register
# Register your models here.
from .models import Contact

@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'message')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'name': ('email',)}
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_unpublished']
    list_editable = ('email', 'message')
    list_display_links = ('name',)


