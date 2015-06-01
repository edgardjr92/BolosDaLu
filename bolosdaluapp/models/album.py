__author__ = 'edgard.barbosa'
from django.db import models


class Album(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)

    def get_all_fotos(self):
        fotos = self.foto_set.all()

        return fotos

    def get_last_foto(self):
        fotos = self.get_all_fotos()
        last_foto = None

        if (fotos):
            last_foto = fotos.reverse()[0]

        return last_foto

    def get_src_last_foto_min(self):
        if self.get_last_foto():
            src = self.get_last_foto().imagem_min
        else:
            src = '/temp/placeholder-k.png'

        return src

    def get_legenda_last_foto(self):
        if self.get_last_foto():
            legenda = self.get_last_foto().legenda
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