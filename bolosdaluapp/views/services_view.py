from django.core.exceptions import ObjectDoesNotExist
from bolosdaluapp.models.informacoes_contato import InformacoesContato
from bolosdaluapp.models.servico import Servico

__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


def init(request):
    try:
        servicos = Servico.objects.all()
        informacoes_contato = InformacoesContato.objects.get(pk=1)
    except ObjectDoesNotExist:
        print 'error'

    return render_to_response('services.html', {'servicos': servicos, 'contato': informacoes_contato},
                              RequestContext(request))