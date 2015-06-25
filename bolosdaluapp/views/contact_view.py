# -*- coding: utf-8 -*-
from PIL import Image
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import classonlymethod

from bolosdaluapp.views.abstract_view import AbstractView


__author__ = 'Edgard JR'


class ContactView(AbstractView):
    def get(self, request):
        return render_to_response('contact.html', {'contato': self.get_informacoes_contato()},
                                  RequestContext(request))

    @classonlymethod
    def send_email(cls, request):
        alert_msg = 'success'
        view = ContactView()

        if request.POST and view._valid_form(request):
            name = request.POST.get('nome')
            from_email = request.POST.get('email')
            subject = request.POST.get('assunto')
            msg = request.POST.get('msg')

            try:
                email = EmailMessage(subject=subject, body=msg, to=['santoos.ed@gmail.com'])

                if 'arquivo' in request.FILES:
                    file = request.FILES['arquivo']
                    email.attach(file.name, file.read(), file.content_type)

                email.send()
            except Exception:
                alert_msg = 'error'

        else:
            alert_msg = 'error'

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







