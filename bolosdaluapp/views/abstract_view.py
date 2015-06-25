from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from bolosdaluapp.models.banner import Banner

from bolosdaluapp.models.contato import Contato


__author__ = 'Edgard JR'


class AbstractView(View):

    def get_banners(self):
        banners = Banner.objects.all().order_by('pk')

        return banners

    def get_informacoes_contato(self):
        informacoes = None
        try:
            informacoes = Contato.objects.get(pk=-1)
        except ObjectDoesNotExist:
            pass

        return informacoes

