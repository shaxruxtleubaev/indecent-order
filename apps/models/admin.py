from django.contrib.admin import *

from .models import (
    Languages,
    Visa,
    OtherImages,
    Models
)

@register(Languages)
class LanguagesAdmin(ModelAdmin):

    list_display = ('id', 'language')
    list_display_links = ('id', 'language')
    ordering = ('language',)

@register(Visa)
class VisaAdmin(ModelAdmin):
    
    list_display = ('id', 'visa')
    list_display_links = ('id', 'visa')
    ordering = ('visa',)

@register(OtherImages)
class OtherImagesAdmin(ModelAdmin):

    list_display = ('id',)
    list_display_links = ('id',)
    ordering = ('-id',)

@register(Models)
class ModelsAdmin(ModelAdmin):

    list_display = ('id', 'name', 'age')
    list_display_links = ('id', 'name', 'age')
    ordering = ('name',)