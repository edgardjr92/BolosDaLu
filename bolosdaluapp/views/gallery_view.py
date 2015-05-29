import json
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from bolosdaluapp.models.album import Album
from bolosdaluapp.models.foto import Foto
from bolosdaluapp.models.informacoes_contato import InformacoesContato

__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


def init(request):
    try:
        informacoes_contato = InformacoesContato.objects.get(pk=-1)
        albuns = Album.objects.all()
    except ObjectDoesNotExist:
        print 'error'

    return render_to_response('gallery.html', {'albuns': albuns, 'contato': informacoes_contato},
                              RequestContext(request))


def fotos(request, id):
    if id:
        fotos = serializers.serialize('json', Foto.objects.filter(album=int(id)))
    else:
        return HttpResponseRedirect("/")

    return HttpResponse(fotos, content_type='application/json')

