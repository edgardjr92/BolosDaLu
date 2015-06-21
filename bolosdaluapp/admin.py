from django.contrib import admin

# Register your models here.
from bolosdaluapp.admins.banner_admin import BannerAdmin
from bolosdaluapp.admins.foto_admin import FotoAdmin
from bolosdaluapp.models.album import Album
from bolosdaluapp.models.banner import Banner
from bolosdaluapp.models.cliente import Cliente
from bolosdaluapp.models.conteudo import Conteudo
from bolosdaluapp.models.depoimento import Depoimento
from bolosdaluapp.models.foto import Foto
from bolosdaluapp.models.informacoes_contato import InformacoesContato
from bolosdaluapp.models.servico import Servico

admin.site.register(Album)
admin.site.register(Banner, BannerAdmin)
admin.site.register(InformacoesContato)
admin.site.register(Servico)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Conteudo)
admin.site.register(Depoimento)
admin.site.register(Cliente)