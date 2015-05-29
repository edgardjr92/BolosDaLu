# -*- coding: utf-8 -*-
__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from django.db import models

PRIMEIRO = 1
SEGUNDO = 2
TERCEIRO = 3
QUARTO = 4

POSICAO = ((PRIMEIRO, '1º'), (SEGUNDO, '2º'), (TERCEIRO, '3º'), (QUARTO, '4º'))


class Banner(models.Model):
    imagem = ImageField(upload_to='media/images/uploads',
                        blank=False, null=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    posicao = models.CharField(choices=POSICAO, max_length=2, null=False, blank=False)


    def __unicode__(self):
        return self.legenda


    class Meta:
        db_table = 'banner'
        app_label = 'bolosdaluapp'