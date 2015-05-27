__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from bolosdaluapp.models.album import Album
from django.db import models


class Foto(models.Model):
    legenda = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=300)
    imagem = ImageField(upload_to='media/images/uploads/galeria',
                        blank=False, null=False)
    album = models.ForeignKey(Album)


    def __unicode__(self):
        return self.legenda

    class Meta:
        db_table = 'foto'
        app_label = 'bolosdaluapp'