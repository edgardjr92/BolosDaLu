__author__ = 'Edgard JR'

from django.contrib import admin


class ConteudoAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False