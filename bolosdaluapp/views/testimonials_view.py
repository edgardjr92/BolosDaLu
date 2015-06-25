# -*- coding: utf-8 -*-
import json

from django.http.response import HttpResponse
from django.utils.decorators import classonlymethod

from bolosdaluapp.models.depoimento import Depoimento
from bolosdaluapp.views.abstract_list_view import AbstractListView


__author__ = 'Edgard JR'


class TestimonialsView(AbstractListView):
    model = Depoimento
    template_name = 'testimonials.html'
    queryset = Depoimento.objects.filter(status='APROVADO').order_by('-data_criacao')
    context_object_name = 'depoimentos'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(TestimonialsView, self).get_context_data(**kwargs)
        num_pages = context['page_obj'].paginator.page_range
        context['qtd_pages'] = num_pages
        context['banners'] = self.get_banners()
        context['contato'] = self.get_informacoes_contato()

        return context

    # @classonlymethod
    # def page(self, request, page):
    #     depoimentos = TestimonialsView.queryset
    #     paginator = Paginator(depoimentos, TestimonialsView.paginate_by)
    #
    #     if request.is_ajax() and page:
    #         depoimentos = serializers.serialize('json', paginator.page(page))
    #
    #     return HttpResponse(depoimentos, content_type='application/json')

    @classonlymethod
    def add(cls, request):
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
