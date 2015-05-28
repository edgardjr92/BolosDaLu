from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from BolosDaLu import settings
from bolosdaluapp.views import index_view, about_view, services_view, gallery_view, testimonials_view, contact_view

admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'BolosDaLu.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', index_view.init),
                       url(r'^sobre/', about_view.init),
                       url(r'^servicos/', services_view.init),
                       url(r'^galeria/', gallery_view.init),
                       url(r'^depoimentos/', testimonials_view.init),
                       url(r'^contato/', contact_view.init),
                       url(r'^fotos/([0-9]{1}/)', contact_view.init),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document.root': settings.MEDIA_ROOT}),
    )
