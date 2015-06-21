# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.utils.decorators import classonlymethod
from bolosdaluapp.models.depoimento import Depoimento
from bolosdaluapp.views.abstract_view import AbstractView


__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


class TestimonialsView(AbstractView):
    def get(self, request):
        return render_to_response('testimonials.html',
                                  {'depoimentos': self.get_depoimentos(), 'banners': self.get_banners(),
                                   'contato': self.get_informacoes_contato()},
                                  RequestContext(request))

    @classonlymethod
    def add(self, request):
        alert_msg = 'success'
        if request.POST:
            name = request.POST.get('nome')
            email = request.POST.get('email')
            msg = request.POST.get('mensagem')

            depoimento = Depoimento()
            depoimento.nome = name
            depoimento.email = email
            depoimento.descricao = msg

            try:
                depoimento.save()
            except Exception:
                alert_msg = 'error'

        return HttpResponse(json.dumps(alert_msg), content_type='application/json')


    def get_depoimentos(self):
        return Depoimento.objects.filter(status='APROVADO').order_by('-data_criacao')





