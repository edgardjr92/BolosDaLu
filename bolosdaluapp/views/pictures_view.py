# -*- coding: utf-8 -*-

from bolosdaluapp.models.foto import Foto
from bolosdaluapp.views.abstract_list_view import AbstractListView


__author__ = 'Edgard JR'


class PicturesView(AbstractListView):
    model = Foto
    template_name = 'pictures.html'
    context_object_name = 'pictures'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(PicturesView, self).get_context_data(**kwargs)
        num_pages = context['page_obj'].paginator.page_range
        context['qtd_pages'] = num_pages
        context['banners'] = self.get_banners()
        context['contato'] = self.get_informacoes_contato()

        return context

    def get_queryset(self):
        return Foto.objects.filter(album=self.args[0])
