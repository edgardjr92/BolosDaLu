# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from bolosdaluapp.views.abstract_view import AbstractView


__author__ = 'Edgard JR'


class ContactView(AbstractView):
    def get(self, request):
        return render_to_response('contact.html', {'contato': self.get_informacoes_contato()},
                                  RequestContext(request))
