__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    imagem = ImageField(upload_to='media/images/uploads',
                        blank=False, null=False)

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'cliente'
        app_label = 'bolosdaluapp'