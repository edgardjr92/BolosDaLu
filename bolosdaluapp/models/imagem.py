__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from django.db import models


class Imagem(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False)
    imagem = ImageField(upload_to='C:/Users/edgard.barbosa/PycharmProjects/BolosDaLu/static/media/images/uploads', blank=True, null=True)

    def __unicode__(self):
        return self.descricao

    class Meta:
        db_table = 'imagem'
        app_label = 'bolosdaluapp'