# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.shortcuts import render_to_response

from bolosdaluapp.models.conteudo import Conteudo
from bolosdaluapp.views.abstract_view import AbstractView


class AboutView(AbstractView):
    def get(self, request):
        conteudo = self.get_conteudo(-1)

        return render_to_response('about.html', {'conteudo': conteudo, 'banners': self.get_banners(),
                                                 'contato': self.get_informacoes_contato()},
                                  RequestContext(request))


    def get_conteudo(self, pk):
        conteudo = None
        try:
            conteudo = Conteudo.objects.get(pk=pk)
        except ObjectDoesNotExist:
            pass

        return conteudo

