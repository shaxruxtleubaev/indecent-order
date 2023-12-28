from django.contrib.admin import *

from .models import (
    Advantages,
    About_us
)

@register(Advantages)
class AdvantagesAdmin(ModelAdmin):

    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    ordering = ('title',)

@register(About_us)
class About_usAdmin(ModelAdmin):

    list_display = ('id', 'years')
    list_display_links = ('id', 'years')
    ordering = ('id',)