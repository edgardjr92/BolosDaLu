# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist

from bolosdaluapp.models.album import Album
from bolosdaluapp.views.abstract_view import AbstractView


__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


class GalleryView(AbstractView):
    def get(self, request):
        try:
            albuns = Album.objects.prefetch_related('fotos').all()
        except ObjectDoesNotExist:
            print 'error'

        return render_to_response('gallery.html', {'albuns': albuns, 'banners': self.get_banners(),
                                                   'contato': self.get_informacoes_contato()},
                                  RequestContext(request))


