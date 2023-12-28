from django.contrib.admin import *

from .models import Model_request

@register(Model_request)
class Model_requestAdmin(ModelAdmin):

    list_display = ('id', 'name', 'age')
    list_display_links = ('id', 'name', 'age')
    ordering = ('name',)