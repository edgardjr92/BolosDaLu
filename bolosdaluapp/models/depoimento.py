__author__ = 'edgard.barbosa'
from django.db import models


class Depoimento(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    descricao = models.TextField(max_length=1000, null=False, blank=False)


    def __unicode__(self):
        return self.descricao

    class Meta:
        db_table = 'depoimento'
        app_label = 'bolosdaluapp'