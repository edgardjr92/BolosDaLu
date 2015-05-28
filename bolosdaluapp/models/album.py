__author__ = 'edgard.barbosa'
from django.db import models


class Album(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)

    def get_all_fotos(self):
        fotos = self.foto_set.all()

        return fotos

    def get_first_foto(self):
        fotos = self.get_all_fotos()
        first_foto = None

        if (fotos):
            first_foto = fotos.reverse()[0]

        return first_foto

    def get_src_first_foto(self):
        if self.get_first_foto():
            src = self.get_first_foto().imagem
        else:
            src = 'media/temp/placeholder-k.png'

        return src

    def get_legenda_first_foto(self):
        if self.get_first_foto():
            legenda = self.get_first_foto().imagem
        else:
            legenda = 'not contains photos'

        return legenda

    def get_fotos_quantity(self):
        self.fotos_quantity = len(self.get_all_fotos())

        return self.fotos_quantity

    def __unicode__(self):
        return self.titulo

    class Meta:
        db_table = 'album'
        app_label = 'bolosdaluapp'