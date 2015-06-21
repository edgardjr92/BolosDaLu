# -*- coding: utf-8 -*-
from image_cropping import ImageRatioField

__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from django.db import models


class Banner(models.Model):
    imagem = ImageField(upload_to='media/images/uploads',
                        blank=False, null=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    cropping = ImageRatioField('imagem', '120x100', allow_fullsize=True)


    def __unicode__(self):
        return self.legenda


    class Meta:
        db_table = 'banner'
        app_label = 'bolosdaluapp'