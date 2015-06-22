from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView

from bolosdaluapp.models.banner import Banner
from bolosdaluapp.models.informacoes_contato import InformacoesContato


__author__ = 'Edgard JR'


class AbstractListView(ListView):

    def get_banners(self):
        banners = Banner.objects.all().order_by('pk')

        return banners

    def get_informacoes_contato(self):
        informacoes = None
        try:
            informacoes = InformacoesContato.objects.get(pk=-1)
        except ObjectDoesNotExist:
            pass

        return informacoes

