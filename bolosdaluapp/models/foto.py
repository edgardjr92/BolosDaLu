from bolosdaluapp.utils.util import Util

__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from bolosdaluapp.models.album import Album
from django.db import models

PATH_IMG = "images/uploads/galeria/"


class Foto(models.Model):
    legenda = models.CharField(max_length=100, null=False, blank=False)
    imagem = ImageField(upload_to='images/uploads/galeria',
                        blank=False, null=False)
    imagem_min = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='fotos')

    def save(self, *args, **kwargs):
        if Util.is_new_image(self.imagem):
            path_img_min = Util.create_small_image(self.imagem, 252, 161)
            self.imagem_min = path_img_min

        super(Foto, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.legenda

    class Meta:
        db_table = 'foto'
        app_label = 'bolosdaluapp'