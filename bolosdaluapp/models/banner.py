# -*- coding: utf-8 -*-

__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from django.db import models


class Banner(models.Model):
    imagem = ImageField(upload_to='media/images/uploads',
                        blank=False, null=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.legenda


    class Meta:
        db_table = 'banner'
        app_label = 'bolosdaluapp'