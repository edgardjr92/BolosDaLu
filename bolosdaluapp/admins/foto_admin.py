__author__ = 'Edgard JR'

from django.contrib import admin


class FotoAdmin(admin.ModelAdmin):
    fields = ('legenda', 'imagem', 'album')
    list_display = ('legenda', 'imagem', 'data_postagem')
    list_filter = ('album', 'data_postagem')

    def get_readonly_fields(self, request, obj=None):
        if not obj is None:
            return ['imagem']
        return []