# -*- coding: utf-8 -*-
from bolosdaluapp.models.servico import Servico
from bolosdaluapp.views.abstract_view import AbstractView

__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


class ServicesView(AbstractView):
    def get(self, request):
        servicos = self.get_all_services()

        return render_to_response('services.html', {'servicos': servicos, 'banners': self.get_banners(), 'contato': self.get_informacoes_contato()},
                                  RequestContext(request))

    def get_all_services(self):
        return Servico.objects.all()