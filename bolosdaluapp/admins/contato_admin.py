__author__ = 'Edgard JR'

from django.contrib import admin


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'email', 'endereco')