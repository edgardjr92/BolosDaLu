__author__ = 'Edgard JR'

from django.contrib import admin


class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_criacao', 'status')
    list_filter = ('status', 'data_criacao')