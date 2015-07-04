from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User
from bolosdaluapp.admins.banner_admin import BannerAdmin
from bolosdaluapp.admins.contato_admin import ContatoAdmin
from bolosdaluapp.admins.conteudo_admin import ConteudoAdmin
from bolosdaluapp.admins.depoimento_admin import DepoimentoAdmin
from bolosdaluapp.admins.foto_admin import FotoAdmin
from bolosdaluapp.models.album import Album
from bolosdaluapp.models.banner import Banner
from bolosdaluapp.models.cliente import Cliente
from bolosdaluapp.models.conteudo import Conteudo
from bolosdaluapp.models.depoimento import Depoimento
from bolosdaluapp.models.foto import Foto
from bolosdaluapp.models.contato import Contato
from bolosdaluapp.models.servico import Servico

admin.site.register(Album)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Servico)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Depoimento, DepoimentoAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)