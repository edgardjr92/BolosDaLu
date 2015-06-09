from django.core.signals import request_started
from django.dispatch import receiver

__author__ = 'edgard.barbosa'
from django.db import models


class InformacoesContato(models.Model):
    telefone = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=150, null=False, blank=False)

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'informacoes_contato'
        app_label = 'bolosdaluapp'

