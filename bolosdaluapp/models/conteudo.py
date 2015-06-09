from django.core.signals import request_started
from django.db.models import ImageField
from django.dispatch import receiver

__author__ = 'edgard.barbosa'
from django.db import models


class Conteudo(models.Model):
    descricao = models.TextField(max_length=2000, null=False, blank=False)
    imagem = ImageField(upload_to='images/uploads',
                        blank=False, null=False)


    def __unicode__(self):
        return self.descricao

    class Meta:
        db_table = 'conteudo'
        app_label = 'bolosdaluapp'
