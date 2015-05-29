from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.shortcuts import render_to_response

from bolosdaluapp.models.conteudo import Conteudo
from bolosdaluapp.models.informacoes_contato import InformacoesContato


def init(request):
    try:
        conteudo = Conteudo.objects.get(pk=-1)
        informacoes_contato = InformacoesContato.objects.get(pk=-1)
    except ObjectDoesNotExist:
        print 'error'

    return render_to_response('about.html', {'conteudo': conteudo, 'contato': informacoes_contato},
                              RequestContext(request))