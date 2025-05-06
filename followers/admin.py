from django.contrib.admin import AdminSite, ModelAdmin, register
# Register your models here.

from .models import Follower

@register(Follower)
class FollowerAdmin(ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    search_fields = ('email',)
    list_filter = ('is_subscribed', )
    ordering = ('-created_at',)
    list_per_page = 10
    