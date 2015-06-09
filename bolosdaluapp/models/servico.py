__author__ = 'edgard.barbosa'
from django.db.models import ImageField
from django.db import models


class Servico(models.Model):
    imagem = ImageField(upload_to='images/uploads',
                        blank=False, null=False)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=300)


    def __unicode__(self):
        return self.titulo

    class Meta:
        db_table = 'servico'
        app_label = 'bolosdaluapp'