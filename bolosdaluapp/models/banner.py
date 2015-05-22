__author__ = 'edgard.barbosa'
from bolosdaluapp.models.imagem import Imagem
from django.db import models


class Banner(models.Model):
    imagens = models.ManyToManyField(Imagem)


    def __unicode__(self):
      pass


    class Meta:
        db_table = 'banner'
        app_label = 'bolosdaluapp'