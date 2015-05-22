from django.contrib import admin

# Register your models here.
from bolosdaluapp.models.album import Album
from bolosdaluapp.models.imagem import Imagem
from bolosdaluapp.models.informacoes_contato import InformacoesContato
from bolosdaluapp.models.pagina import Pagina

admin.site.register(Album)
admin.site.register(Imagem)
admin.site.register(InformacoesContato)
admin.site.register(Pagina)