from django.contrib.admin import *

from .models import ClientRequest

@register(ClientRequest)
class ClientRequestAdmin(ModelAdmin):

    list_display = ('id', 'name', 'phone')
    list_display_links = ('id', 'name', 'phone')
    ordering = ('name',)