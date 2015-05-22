__author__ = 'edgard.barbosa'
from django.db import models


class Album(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)


    def __unicode__(self):
        return self.titulo

    class Meta:
        db_table = 'album'
        app_label = 'bolosdaluapp'