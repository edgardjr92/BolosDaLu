__author__ = 'edgard.barbosa'
from django.db import models

STATUS = (('PENDENTE', 'Pendente'),
          ('APROVADO', 'Aprovado'))


class Depoimento(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    descricao = models.TextField(max_length=1000, null=False, blank=False)
    status = models.CharField(choices=STATUS, null=False, max_length=9, default=STATUS[0][0])
    data_criacao = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return self.descricao

    class Meta:
        db_table = 'depoimento'
        app_label = 'bolosdaluapp'