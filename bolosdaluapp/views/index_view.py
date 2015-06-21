# -*- coding: utf-8 -*-
from bolosdaluapp.views.abstract_view import AbstractView

__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


class IndexView(AbstractView):
    def get(self, request):
        return render_to_response('index.html', {'banners': self.get_banners(), 'contato': self.get_informacoes_contato()},
                                  RequestContext(request))