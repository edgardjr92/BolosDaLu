# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.utils.decorators import classonlymethod

from bolosdaluapp.views.abstract_view import AbstractView


__author__ = 'Edgard JR'


class ContactView(AbstractView):
    def get(self, request):
        return render_to_response('contact.html', {'contato': self.get_informacoes_contato()},
                                  RequestContext(request))

    @classonlymethod
    def send_email(cls, request):
        view = ContactView()

        if request.POST and view._valid_form(request):
            name = request.POST.get('nome')
            from_email = request.POST.get('email')
            subject = request.POST.get('assunto')
            msg = request.POST.get('msg')
            html = get_template('email.html')

            d = Context({'nome': name, 'email': from_email, 'assunto': subject, 'mensagem': msg})

            html_content = html.render(d)

            try:
                email = EmailMessage(subject=subject, body=html_content, to=['santoos.ed@gmail.com'])
                email.content_subtype = 'html'

                if 'arquivo' in request.FILES:
                    file = request.FILES['arquivo']
                    email.attach(file.name, file.read(), file.content_type)

                email.send()
                messages.success(request, 'Seu email foi enviado com sucesso, logo entraremos em contato.')
            except Exception:
                messages.error(request, 'Falha ao envar o email, tente novamente mais tarde.')

        else:
            messages.warning(request, 'Verifique se todos os campos estão preenchidos.')

        return HttpResponseRedirect('/contato/')


    def _valid_file(self, content_type):
        is_valid = False

        if content_type:
            if content_type == 'image/jpeg' or content_type == 'image/png':
                is_valid = True

        return is_valid

    def _valid_form(self, request):
        is_valid = True
        name = request.POST.get('nome')
        from_email = request.POST.get('email')
        subject = request.POST.get('assunto')
        msg = request.POST.get('msg')

        if not name or not from_email or not subject or not msg:
            is_valid = False

        if 'arquivo' in request.FILES:
            file = request.FILES['arquivo']

            if not self._valid_file(str(file.content_type)):
                is_valid = False

        return is_valid







