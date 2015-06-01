__author__ = 'Edgard JR'

from django.contrib import admin


class FotoAdmin(admin.ModelAdmin):
    fields = ('legenda', 'imagem', 'album')
    list_display = ('legenda', 'imagem')