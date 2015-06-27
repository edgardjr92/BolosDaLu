__author__ = 'Edgard JR'

from django.contrib import admin


class FotoAdmin(admin.ModelAdmin):
    fields = ('legenda', 'imagem', 'album')
    list_display = ('legenda', 'imagem')

    def get_readonly_fields(self, request, obj=None):
        if not obj is None:
            return ['imagem']
        return []